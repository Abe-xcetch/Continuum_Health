from django.db import models

from apps.core.models import ContinuumModel


class Note(ContinuumModel):
    """Synthetic test-only model built on the full Continuum base model."""

    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
