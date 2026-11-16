from django.apps import AppConfig


class CoreTestAppConfig(AppConfig):
    """Concrete models for testing apps.core's abstract models. Installed only in test settings."""

    name = "apps.core.tests.testapp"
    label = "core_testapp"
    default_auto_field = "django.db.models.BigAutoField"
