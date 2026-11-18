"""Local development settings."""

from .base import *  # noqa: F403
from .base import env

DEBUG = True
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Serve static files from app/static dirs without collectstatic (WhiteNoise dev mode).
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
