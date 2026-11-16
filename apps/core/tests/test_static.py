"""Static-file layout guards (production collectstatic must succeed)."""

from pathlib import Path

from django.conf import settings


def test_tailwind_source_is_not_inside_staticfiles_dirs():
    # Regression: the Tailwind input (`@import "tailwindcss"`) under static/ made
    # ManifestStaticFilesStorage fail in collectstatic, because the import is not a file.
    offenders = [
        path
        for static_dir in settings.STATICFILES_DIRS
        for path in Path(static_dir).rglob("*.css")
        if '@import "tailwindcss"' in path.read_text(encoding="utf-8")
    ]

    assert offenders == []
