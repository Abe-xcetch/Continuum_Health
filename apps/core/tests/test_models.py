"""Behaviour of the abstract base models in apps.core, tested through the Note test model."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest import mock

import pytest
from django.db.models import ProtectedError

from apps.accounts.tests.factories import UserFactory
from apps.core.models import SoftDeleteQuerySet
from apps.core.tests.factories import NoteFactory
from apps.core.tests.testapp.models import Note

pytestmark = pytest.mark.django_db

FIXED_NOW = datetime(2026, 1, 1, 9, 0, tzinfo=UTC)


# --- Public ID ----------------------------------------------------------------


def test_public_id_is_generated_as_uuid4_on_create():
    note = NoteFactory()

    assert isinstance(note.public_id, uuid.UUID)
    assert note.public_id.version == 4


def test_public_id_is_unique_per_row():
    first, second = NoteFactory(), NoteFactory()

    assert first.public_id != second.public_id


def test_public_id_is_not_editable_and_survives_save():
    note = NoteFactory()
    original = note.public_id

    note.title = "Changed"
    note.save()
    note.refresh_from_db()

    assert Note._meta.get_field("public_id").editable is False
    assert note.public_id == original


# --- Timestamps ---------------------------------------------------------------


def test_created_and_updated_at_are_set_on_create():
    with mock.patch("django.utils.timezone.now", return_value=FIXED_NOW):
        note = NoteFactory()

    assert note.created_at == FIXED_NOW
    assert note.updated_at == FIXED_NOW


def test_updated_at_changes_on_save_but_created_at_does_not():
    with mock.patch("django.utils.timezone.now", return_value=FIXED_NOW):
        note = NoteFactory()
    later = FIXED_NOW + timedelta(hours=1)

    with mock.patch("django.utils.timezone.now", return_value=later):
        note.title = "Updated"
        note.save()
    note.refresh_from_db()

    assert note.created_at == FIXED_NOW
    assert note.updated_at == later


# --- created_by / updated_by --------------------------------------------------


def test_actor_fields_are_optional_for_system_actions():
    note = NoteFactory()

    assert note.created_by is None
    assert note.updated_by is None


def test_set_actor_on_new_instance_sets_created_by_and_updated_by():
    user = UserFactory()
    note = Note(title="New")

    note.set_actor(user)
    note.save()
    note.refresh_from_db()

    assert note.created_by == user
    assert note.updated_by == user


def test_set_actor_on_existing_instance_only_changes_updated_by():
    creator, editor = UserFactory(), UserFactory()
    note = Note(title="New")
    note.set_actor(creator)
    note.save()

    note.set_actor(editor)
    note.save()
    note.refresh_from_db()

    assert note.created_by == creator
    assert note.updated_by == editor


def test_user_referenced_by_created_by_cannot_be_deleted():
    user = UserFactory()
    note = Note(title="Owned")
    note.set_actor(user)
    note.save()

    with pytest.raises(ProtectedError):
        user.delete()


# --- Soft delete --------------------------------------------------------------


def test_instance_delete_soft_deletes_and_hides_row_from_default_manager():
    actor = UserFactory()
    note = NoteFactory()

    with mock.patch("django.utils.timezone.now", return_value=FIXED_NOW):
        note.delete(actor=actor)

    assert not Note.objects.filter(pk=note.pk).exists()
    stored = Note.all_objects.get(pk=note.pk)
    assert stored.deleted_at == FIXED_NOW
    assert stored.deleted_by == actor
    assert stored.is_deleted is True


def test_instance_delete_returns_django_style_count():
    note = NoteFactory()

    assert note.delete() == (1, {"core_testapp.Note": 1})


def test_soft_deleted_row_is_not_returned_by_get():
    note = NoteFactory()
    note.delete()

    with pytest.raises(Note.DoesNotExist):
        Note.objects.get(pk=note.pk)


def test_deleting_an_already_deleted_row_keeps_the_original_deletion_record():
    first_actor, second_actor = UserFactory(), UserFactory()
    note = NoteFactory()
    with mock.patch("django.utils.timezone.now", return_value=FIXED_NOW):
        note.delete(actor=first_actor)

    result = Note.all_objects.get(pk=note.pk).delete(actor=second_actor)

    stored = Note.all_objects.get(pk=note.pk)
    assert result == (0, {})
    assert stored.deleted_at == FIXED_NOW
    assert stored.deleted_by == first_actor


def test_queryset_delete_soft_deletes_every_matching_row():
    actor = UserFactory()
    NoteFactory.create_batch(3)

    count, per_model = Note.objects.all().delete(actor=actor)

    assert count == 3
    assert per_model == {"core_testapp.Note": 3}
    assert Note.objects.count() == 0
    assert Note.all_objects.count() == 3
    assert set(Note.all_objects.values_list("deleted_by", flat=True)) == {actor.pk}


def test_all_objects_queryset_delete_is_also_soft_and_skips_deleted_rows():
    already = NoteFactory()
    with mock.patch("django.utils.timezone.now", return_value=FIXED_NOW):
        already.delete()
    NoteFactory()

    count, _ = Note.all_objects.all().delete()

    assert count == 1
    assert Note.all_objects.count() == 2
    assert Note.all_objects.get(pk=already.pk).deleted_at == FIXED_NOW


def test_restore_makes_row_visible_again():
    note = NoteFactory()
    note.delete(actor=UserFactory())

    restored = Note.all_objects.get(pk=note.pk)
    restored.restore()

    assert Note.objects.filter(pk=note.pk).exists()
    restored.refresh_from_db()
    assert restored.deleted_at is None
    assert restored.deleted_by is None
    assert restored.is_deleted is False


def test_alive_and_deleted_queryset_filters():
    alive = NoteFactory()
    gone = NoteFactory()
    gone.delete()

    assert list(Note.all_objects.alive()) == [alive]
    assert list(Note.all_objects.deleted()) == [gone]


def test_no_hard_delete_method_exists():
    # Clinical records are never hard-deleted (CLAUDE.md). A controlled, audited purge
    # for retention/erasure requests is pending a policy decision (see docs).
    assert not hasattr(Note, "hard_delete")
    assert not hasattr(SoftDeleteQuerySet, "hard_delete")


def test_default_manager_count_is_a_single_query(django_assert_num_queries):
    NoteFactory.create_batch(3)
    NoteFactory().delete()

    with django_assert_num_queries(1):
        assert Note.objects.count() == 3
