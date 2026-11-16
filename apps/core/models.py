"""Abstract base models for every Continuum domain model.

Use ``ContinuumModel`` for new domain models. It combines:

- ``PublicIdModel``: a random UUID (``public_id``) for URLs and APIs. The integer primary
  key is internal and must never be exposed.
- ``TimeStampedModel``: ``created_at`` / ``updated_at``.
- ``AuditedModel``: ``created_by`` / ``updated_by``. Services set these explicitly with
  ``set_actor(user)``; there is deliberately no thread-local "current user" magic.
- ``SoftDeleteModel``: rows are never hard-deleted. ``delete()`` on an instance or a
  queryset only marks the row deleted; ``objects`` hides deleted rows and
  ``all_objects`` shows everything.

Known limits of soft delete (by design, documented here so nobody is surprised):

- Following a relation (``obj.some_fk``) uses Django's unfiltered base manager, so it can
  reach a soft-deleted row. Code that walks relations must check ``is_deleted``.
- A ``CASCADE`` from another model would bypass soft delete with a real SQL DELETE.
  Domain foreign keys must therefore use ``on_delete=models.PROTECT``.
- There is no hard-delete method. A controlled, audited purge for data-retention or
  erasure requests is pending a policy decision (see docs/decisions-pending.md).
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, ClassVar, Self, TypeVar

from django.conf import settings
from django.db import models
from django.utils import timezone

if TYPE_CHECKING:
    from apps.accounts.models import User


class PublicIdModel(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuditedModel(models.Model):
    # Nullable so system actions (migrations, scheduled jobs) can create rows.
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name="+",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name="+",
    )

    class Meta:
        abstract = True

    def set_actor(self, actor: User | None) -> None:
        """Record who is making this change. Call before ``save()`` in a service."""
        if self._state.adding:
            self.created_by = actor
        self.updated_by = actor


_M = TypeVar("_M", bound=models.Model)


class SoftDeleteQuerySet(models.QuerySet[_M]):
    def alive(self) -> Self:
        return self.filter(deleted_at__isnull=True)

    def deleted(self) -> Self:
        return self.filter(deleted_at__isnull=False)

    def delete(self, *, actor: User | None = None) -> tuple[int, dict[str, int]]:
        """Soft-delete every matching row that is not already deleted. Never hard-deletes."""
        count = self.alive().update(deleted_at=timezone.now(), deleted_by=actor)
        return count, ({self.model._meta.label: count} if count else {})

    delete.alters_data = True  # type: ignore[attr-defined]
    delete.queryset_only = True  # type: ignore[attr-defined]


class SoftDeleteManager(models.Manager.from_queryset(SoftDeleteQuerySet)):  # type: ignore[misc]
    """Default manager: hides soft-deleted rows."""

    def get_queryset(self) -> SoftDeleteQuerySet[Any]:
        return super().get_queryset().alive()  # type: ignore[no-any-return]


class AllObjectsManager(models.Manager.from_queryset(SoftDeleteQuerySet)):  # type: ignore[misc]
    """Includes soft-deleted rows. Use deliberately (audit views, restore)."""


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False, db_index=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        editable=False,
        related_name="+",
    )

    objects: ClassVar[SoftDeleteManager] = SoftDeleteManager()
    all_objects: ClassVar[AllObjectsManager] = AllObjectsManager()

    class Meta:
        abstract = True

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None

    def delete(
        self,
        using: Any = None,
        keep_parents: bool = False,
        *,
        actor: User | None = None,
    ) -> tuple[int, dict[str, int]]:
        """Soft-delete this row. A second delete keeps the original deletion record."""
        if self.is_deleted:
            return 0, {}
        self.deleted_at = timezone.now()
        self.deleted_by = actor
        self.save(using=using, update_fields=["deleted_at", "deleted_by"])
        return 1, {self._meta.label: 1}

    delete.alters_data = True  # type: ignore[attr-defined]

    def restore(self) -> None:
        self.deleted_at = None
        self.deleted_by = None
        self.save(update_fields=["deleted_at", "deleted_by"])

    restore.alters_data = True  # type: ignore[attr-defined]


class ContinuumModel(PublicIdModel, TimeStampedModel, AuditedModel, SoftDeleteModel):
    """Base class for Continuum domain models."""

    class Meta:
        abstract = True
