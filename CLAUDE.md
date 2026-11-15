# CLAUDE.md

Guidance for Claude Code when working in this repository.

## 1. Project

**Continuum Health** is a system for managing patients with sickle cell disease (SCD).
The first deployment is a pilot in Kenya.

**PRD and docs:** none in the repo yet. The `continuum-dev-workflow` skill asks every
plan to cite "the Continuum PRD section it implements", so the PRD must be added
(suggested location: `docs/prd.md`) before feature work starts. Until then, ask the
user which requirement a feature implements.

## 2. Stack (decided; don't revisit without asking)

- **Backend:** Python 3.12+, Django (current LTS), PostgreSQL, Django REST Framework for APIs
  (for mobile, integrations and other JSON needs; the main UI is server-rendered).
- **Frontend:** Django templates + HTMX + Alpine.js + Tailwind CSS. HTMX, Alpine and
  Tailwind are bundled locally, with no CDN in production.
- **Async:** Celery + Redis only where a task truly needs it (SMS reminders, reports, imports).
- **Tooling:** pytest-django, factory_boy, ruff, black, mypy (django-stubs).
  Bandit and pip-audit are used for security checks.

## 3. Development environment

- Windows 11, PowerShell as the primary shell. Write commands for PowerShell
  (`.venv\Scripts\Activate.ps1`, `$env:VAR = "x"`, no `&&` in Windows PowerShell 5.1).
- Paths use backslashes in instructions meant for the user; keep code paths portable.
- Tests run against a local PostgreSQL, not SQLite.

## 4. How to work

- **Always follow the `continuum-dev-workflow` skill** for every feature, bug fix or refactor:
  1. Plan first: map the work to the PRD and list models, migrations, permissions,
     screens and endpoints. Wait for approval on data-model or permission changes.
  2. Tests first (RED → GREEN → REFACTOR). Bug fixes start with a failing test that
     reproduces the bug.
  3. Review the diff as if seeing it fresh.
  4. Produce the **CONTINUUM VERIFICATION REPORT** before any commit or release.
     Never mark a check as passed without running it.
- **Apply `continuum-django-backend`** to all Python/Django code: layout, models, services,
  selectors, DRF, migrations, security and Celery.
- **Apply `continuum-frontend`** to all templates, HTMX, Alpine.js and Tailwind work.
- Use conventional commits (`feat:`, `fix:`, `test:` …). Commit only when asked.

## 5. Hard rules

- **No real patient data, ever.** Fixtures, tests, seed data, screenshots and examples use
  synthetic data only. Never commit real patient data.
- **No secrets in code.** All secrets come from environment variables, and `.env` is never committed.
- **Never log patient identifiers** (names, phone numbers, national IDs, clinical values).
  Logs carry request IDs and user IDs only.
- **Clinical records are never hard-deleted.** Use soft delete or status fields, and
  `on_delete=models.PROTECT` on clinical and patient relations.
- **Ask before changing the data model or permissions:** new or changed models and fields,
  migrations, roles, and access rules.
- Every view and endpoint has an explicit permission check, tested for both allowed and denied cases.
- Use UUIDs in URLs and APIs, never sequential IDs.

## 6. Current state (as of 2026-11-15)

**Exists:**
- An empty git repo on `main` with no commits yet.
- `.claude/skills/`: the three project skills (`continuum-dev-workflow`,
  `continuum-django-backend`, `continuum-frontend`).
- `CLAUDE.md` (this file).

**Missing:**
- PRD and any product or clinical docs (`docs/`).
- Django project: `manage.py`, `config/` (split settings), `apps/`.
- `pyproject.toml` with dependencies and ruff/black/mypy/pytest configuration.
- `.gitignore`, `.env.example`, README.
- Test setup: `conftest.py`, factories and `config/settings/test.py`.
- Tailwind build, static assets, and `templates/base.html`.
- CI pipeline and a pre-commit configuration.

## 7. Common commands

Placeholders: fill these in once the Django project exists.

```powershell
# Setup
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
# TODO: pip install -e ".[dev]"   (or the chosen dependency tool)
# TODO: copy .env.example to .env and set DATABASE_URL, SECRET_KEY, ...

# Run
# TODO: python manage.py runserver
# TODO: Tailwind watch command

# Migrate
# TODO: python manage.py makemigrations
# TODO: python manage.py migrate
# TODO: python manage.py makemigrations --check --dry-run   (CI check)

# Test
# TODO: pytest --reuse-db
# TODO: pytest --cov=apps --cov-report=term-missing

# Quality
# TODO: ruff check . ; black --check . ; mypy .
# TODO: python manage.py check ; bandit -r apps ; pip-audit
```
