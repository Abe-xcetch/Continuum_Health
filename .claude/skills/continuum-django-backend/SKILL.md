---
name: continuum-django-backend
description: Use when writing, structuring or reviewing Continuum's Django/Python backend: project layout, models, services, DRF APIs, migrations, settings, security and Celery tasks.
---

# Continuum: Django backend conventions

Adapted from ECC (github.com/affaan-m/ECC, MIT): django-patterns, django-security, database-migrations, django-celery, python-patterns and the common + python rule packs. Changed where ECC's generic advice doesn't fit a PostgreSQL clinical-records system.

## Stack
- Python 3.12+, Django (current LTS), PostgreSQL, Django REST Framework for the API layer.
- Server-rendered UI lives in the same project (see continuum-frontend). DRF is for mobile apps, integrations and other JSON needs.
- Celery + Redis only when a task truly needs to be async (SMS reminders, report generation, imports).
- Tooling: ruff (lint + import sort), black, mypy (django-stubs), pytest-django, factory_boy, bandit, pip-audit.

## Project layout
```
continuum/
├── config/
│   ├── settings/{base,development,test,production}.py
│   ├── urls.py  asgi.py  wsgi.py  celery.py
├── apps/
│   └── <domain_app>/            # one app per domain area, not per technical layer
│       ├── models.py            # or models/ package when >400 lines
│       ├── querysets.py         # custom QuerySets
│       ├── services.py          # business logic (writes)
│       ├── selectors.py         # read/query logic
│       ├── forms.py  views.py  urls.py
│       ├── api/                 # serializers.py, views.py, urls.py, permissions.py
│       ├── templates/<app>/
│       ├── tasks.py             # Celery tasks, if any
│       └── tests/
├── templates/  static/
├── manage.py  pyproject.toml
```
- Organise by domain, not by type. Files 200-400 lines typical, 800 hard ceiling. Functions under ~50 lines, nesting no deeper than 4.
- Split settings; every secret and host-specific value comes from environment variables (django-environ). Fail at startup if a required one is missing.

## Where logic goes
- **Views / viewsets are thin**: parse input, check permission, call a service or selector, return a response.
- **services.py**: all writes and business rules, wrapped in `transaction.atomic` when more than one row changes. Type-annotated, keyword-only arguments for clarity.
- **selectors.py / QuerySets**: reusable reads (`.active()`, `.for_facility(f)`), always with `select_related`/`prefetch_related` where relations are used.
- **Signals**: avoid for business logic (hidden side effects). Acceptable for cross-cutting concerns like audit logging; document every receiver.
- Plain-data objects passed between layers use frozen dataclasses. ECC's "never mutate" rule applies to these, not to Django model instances.

## Models
- Custom user model from day one (`AUTH_USER_MODEL`), email login.
- Every model: `created_at`, `updated_at`; `created_by`/`updated_by` where a person makes the change.
- Use `UUIDField` public identifiers in URLs and APIs; never expose sequential IDs.
- Clinical and patient records: `on_delete=models.PROTECT`, never `CASCADE`. Use soft delete / status fields rather than hard deletes.
- Use `TextChoices`/`IntegerChoices` for coded values; `DecimalField` for measured quantities, never float.
- Declare `indexes` and `constraints` (CheckConstraint, UniqueConstraint) in `Meta` so the database enforces rules, not just forms.

## DRF API
- Separate serializers for read vs create/update when fields differ.
- Validation in serializers/forms at the boundary; domain rules re-checked in services.
- Default permission `IsAuthenticated` plus object-level/role permissions; never `AllowAny` except login/health endpoints.
- Pagination on every list endpoint; throttling configured globally.
- Keep DRF's standard error format; version under `/api/v1/`. Generate an OpenAPI schema (drf-spectacular).

## Migrations (PostgreSQL)
1. Every schema change is a migration; never alter the database by hand.
2. Migrations are immutable once applied anywhere shared; fix forward with a new migration.
3. Schema and data migrations are separate files.
4. New columns on existing tables are nullable or have a default; add NOT NULL after backfill.
5. Indexes on large tables: `AddIndexConcurrently` in a non-atomic migration.
6. Renames and drops use expand-contract: add new → backfill → switch code → drop old in a later release.
7. Data migrations use `apps.get_model`, never direct model imports, and are reversible or explicitly marked irreversible.

## Security checklist (every change)
- No secrets in code; `.env` never committed.
- `DEBUG=False`, HTTPS redirect, secure + HttpOnly cookies, HSTS, CSP, X-Frame-Options in production.
- ORM only; `raw()`/`extra()` only with parameters. Never `|safe` or `mark_safe` on user input; use `format_html`.
- CSRF stays on; no `csrf_exempt` without written justification.
- File uploads: validate type and size, store outside web root, serve through an authorised view.
- Every view and endpoint has an explicit permission check; test the "wrong user" case.
- Logs carry request IDs and user IDs, never patient names, phone numbers or clinical values. Use `logging`, never `print()`.
- Run `python manage.py check --deploy`, `bandit -r apps`, `pip-audit` before release.

## Celery tasks
- Pass primary keys, never model instances.
- Tasks are idempotent: re-fetch with `select_for_update()` and check status before acting.
- Set `acks_late=True`, soft time limits, retries with backoff for network calls; beat on a single node.
- Never call `.apply()`/`.get()` synchronously in a request.

## Python style
- PEP 8 via black + ruff; type hints on all function signatures.
- Catch specific exceptions; chain with `raise ... from e`; never bare `except`.
- Named constants for thresholds and limits; no magic numbers.
- No mutable default arguments; `is None`, `isinstance`, explicit imports.
