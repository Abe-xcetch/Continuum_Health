"""Test settings: PostgreSQL with real migrations (run with pytest --reuse-db)."""

from .base import *  # noqa: F403
from .base import INSTALLED_APPS

DEBUG = False
ALLOWED_HOSTS = ["testserver", "localhost"]

# Fast hashing for tests only.
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Celery is not installed yet; this is ready for when it is.
CELERY_TASK_ALWAYS_EAGER = True

# Concrete models used only to test the abstract base models in apps.core.
INSTALLED_APPS = [*INSTALLED_APPS, "apps.core.tests.testapp"]

# Serve static files from app/static dirs without collectstatic (WhiteNoise dev mode).
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
