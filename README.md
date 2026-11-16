# Continuum Health

A secure, patient-centred longitudinal health record for people living with sickle cell
disease (SCD). The first deployment is a pilot at one facility in Kenya.

- Product requirements: [`docs/prd.md`](docs/prd.md) (source of truth, v0, under revision)
- PRD review and open decisions: [`docs/prd-review.md`](docs/prd-review.md)
- Pending technical decisions: [`docs/decisions-pending.md`](docs/decisions-pending.md)
- How we work (for people and Claude Code): [`CLAUDE.md`](CLAUDE.md)

**Status:** project foundation only. No patient or clinical features yet; they wait on
PRD decisions. **Use synthetic data only. Never real patient data.**

## Stack

Python 3.12 · Django 5.2 LTS · PostgreSQL · Django REST Framework · Django templates +
HTMX 2 + Alpine.js (CSP build) + Tailwind CSS 4 (standalone CLI, no Node) ·
pytest-django · factory_boy · ruff · black · mypy · bandit · pip-audit · uv.

## Setup on Windows (PowerShell)

Prerequisites: [uv](https://docs.astral.sh/uv/) and PostgreSQL 17 running locally.
uv installs Python 3.12 itself if needed.

```powershell
# 1. Install dependencies (creates .venv with Python 3.12 from uv.lock)
uv sync

# 2. Configure environment
Copy-Item .env.example .env
#    Edit .env: set DJANGO_SECRET_KEY and replace CHANGE_ME in DATABASE_URL with your
#    postgres password. Generate a key with:
uv run python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"

# 3. Create the database (prompts for the postgres password)
createdb -h localhost -U postgres continuum_dev

# 4. Apply migrations and create an admin account
uv run python manage.py migrate
uv run python manage.py createsuperuser

# 5. Build the CSS (downloads the Tailwind CLI once into bin\, checksum-verified)
.\scripts\tailwind.ps1

# 6. Run
uv run python manage.py runserver
```

Open http://localhost:8000/ (redirects to the login page), http://localhost:8000/admin/
and http://localhost:8000/health/.

While editing templates, run `.\scripts\tailwind.ps1 -Watch` in a second terminal.
`static\css\app.css` is generated and never committed; CI builds it.

If PowerShell blocks the script, allow local scripts for your user once:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Tests and quality checks

```powershell
uv run pytest                                  # PostgreSQL, real migrations, --reuse-db
uv run pytest --create-db                      # after adding or changing migrations
uv run pytest --cov --cov-report=term-missing  # coverage (fails under 80%)

uv run ruff check . ; uv run black --check . ; uv run mypy .
uv run python manage.py makemigrations --check --dry-run
uv run bandit -q -c pyproject.toml -r apps config
uv export --format requirements-txt --no-hashes --all-groups -q > $env:TEMP\req.txt
uv run pip-audit -r $env:TEMP\req.txt

uv run pre-commit install                      # once: run hooks on every commit
```

Tests need the `postgres` user to be able to create `test_continuum_dev`.

## Layout

```
config/settings/   base, development, test, production (all secrets from the environment)
apps/core/         abstract base models (UUID public_id, timestamps, created_by/updated_by,
                   soft delete), request-ID logging, home page, /health/
apps/accounts/     custom User: email login for staff/clinician accounts only
templates/         base.html, components/, per-app pages and partials
static/            src/app.css (Tailwind input), js/, vendor/ (pinned HTMX + Alpine)
scripts/           tailwind.ps1 (Windows), tailwind.sh (CI/Linux)
docs/              PRD, PRD review, pending decisions
```

CI (GitHub Actions) runs lint, types, security, migration checks, the Tailwind build and
the tests on PostgreSQL 17 for every push and pull request to `main`.
