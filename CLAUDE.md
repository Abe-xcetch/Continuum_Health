# CLAUDE.md

Guidance for Claude Code when working in this repository.

## 1. Project

**Continuum Health** is a system for managing patients with sickle cell disease (SCD).
The first deployment is a pilot in Kenya.

**PRD and docs:**
- `docs/prd.md` is the **source of truth**. Cite it as "PRD §x.y" using its section numbers.
  It was converted word-for-word from `docs/CONTINUUM_HEALTH_PRD_CLEANED.docx` (the original,
  kept for reference). Don't edit `prd.md` by hand outside an agreed PRD revision.
- `docs/prd-review.md`: gaps, contradictions and 29 open decisions found in the v0 PRD.
- **The PRD is under revision (v0 baseline).** Three areas are being resolved before any
  feature work: the SCD core dataset, emergency identification, and the data-model blockers
  (prd-review §c, §d, §e). Don't start feature plans that depend on these areas.
  If a task touches an open decision in prd-review §f, ask; don't assume.
- Section numbers may change in the revision; re-check citations afterwards.

## 2. Stack (decided; don't revisit without asking)

- **Backend:** Python 3.12+, Django (current LTS), PostgreSQL, Django REST Framework for APIs
  (for mobile, integrations and other JSON needs; the main UI is server-rendered).
- **Frontend:** Django templates + HTMX + Alpine.js + Tailwind CSS. HTMX, Alpine and
  Tailwind are bundled locally, with no CDN in production.
- **Async:** Celery + Redis only where a task truly needs it (SMS reminders, reports, imports).
- **Tooling:** uv (packaging), pytest-django, factory_boy, ruff, black, mypy (django-stubs).
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

## 6. Current state (as of 2026-11-16)

**Exists (foundation only):**
- Django 5.2 LTS project, managed with **uv** (`uv.lock`, Python 3.12): split settings in
  `config/settings/`, all secrets read from `.env` (never committed).
- `apps/core`: `ContinuumModel` abstract base (UUID `public_id`, timestamps,
  `created_by`/`updated_by` via `set_actor()`, soft delete with `objects` / `all_objects`).
  There is **no hard-delete method**; see `docs/decisions-pending.md` for the pending purge
  policy. Also request-ID logging, a placeholder home page and `/health/`.
- `apps/accounts`: custom `User` with **email login for staff/clinician accounts only**.
  **Patient login is an open decision** (Continuum ID / phone + OTP, PRD §11.4), likely a
  separate authentication path. Don't add patient fields to `User`.
- Frontend: `templates/base.html`, `components/`, Tailwind 4 standalone CLI, vendored HTMX 2 +
  Alpine (CSP build), strict CSP (no inline scripts or styles; register Alpine components
  in `static/js/app.js`).
- pytest-django on PostgreSQL, pre-commit, GitHub Actions CI. `docs/`: PRD v0 and review.

**Missing (blocked on PRD decisions):** patient, SCD dataset, verification, identifiers,
consent, emergency access, roles, facilities and guardian models.

## 7. Common commands (PowerShell)

```powershell
# Setup (see README for the full first-time steps)
uv sync                                         # install from uv.lock
Copy-Item .env.example .env                     # then set DJANGO_SECRET_KEY and DB password

# Run
uv run python manage.py runserver
.\scripts	ailwind.ps1 -Watch                    # CSS rebuild while editing templates

# Migrate
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py makemigrations --check --dry-run

# Test
uv run pytest                                   # PostgreSQL, migrations, --reuse-db
uv run pytest --create-db --cov --cov-report=term-missing

# Quality
uv run ruff check . ; uv run black --check . ; uv run mypy .
uv run python manage.py check
uv run bandit -q -c pyproject.toml -r apps config
uv export --format requirements-txt --no-hashes --all-groups -q > $env:TEMP
eq.txt
uv run pip-audit -r $env:TEMP
eq.txt
uv run pre-commit run --all-files
```
