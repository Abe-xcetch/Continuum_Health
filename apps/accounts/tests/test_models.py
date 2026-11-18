"""Custom User model: email login for staff/clinician accounts."""

import uuid

import pytest
from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError

from apps.accounts.models import User
from apps.accounts.tests.factories import TEST_PASSWORD, UserFactory

pytestmark = pytest.mark.django_db


def test_auth_user_model_is_the_custom_user():
    assert get_user_model() is User


def test_email_is_the_login_field_and_there_is_no_username():
    assert User.USERNAME_FIELD == "email"
    assert User.REQUIRED_FIELDS == []
    assert "username" not in {f.name for f in User._meta.get_fields()}


def test_create_user_normalises_email_to_lowercase_and_hashes_password():
    user = User.objects.create_user(email="  Nurse.One@Example.TEST ", password=TEST_PASSWORD)

    assert user.email == "nurse.one@example.test"
    assert user.password != TEST_PASSWORD
    assert user.check_password(TEST_PASSWORD)
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False


def test_create_user_requires_an_email():
    with pytest.raises(ValueError, match="email"):
        User.objects.create_user(email="", password=TEST_PASSWORD)


def test_create_user_without_password_has_unusable_password():
    user = User.objects.create_user(email="nopass@example.test")

    assert user.has_usable_password() is False


def test_create_superuser_sets_staff_and_superuser_flags():
    admin = User.objects.create_superuser(email="admin@example.test", password=TEST_PASSWORD)

    assert admin.is_staff is True
    assert admin.is_superuser is True


@pytest.mark.parametrize("flag", ["is_staff", "is_superuser"])
def test_create_superuser_rejects_false_flags(flag):
    with pytest.raises(ValueError, match=flag):
        User.objects.create_superuser(
            email="admin@example.test", password=TEST_PASSWORD, **{flag: False}
        )


def test_email_is_unique_ignoring_case():
    UserFactory(email="clinician@example.test")

    with pytest.raises(IntegrityError):
        # Bypass the manager's normalisation to prove the database enforces it.
        User.objects.bulk_create([User(email="CLINICIAN@example.test")])


def test_user_has_uuid4_public_id_and_timestamps():
    user = UserFactory()

    assert isinstance(user.public_id, uuid.UUID)
    assert user.public_id.version == 4
    assert user.created_at is not None
    assert user.updated_at is not None


def test_str_is_email():
    assert str(UserFactory(email="lab@example.test")) == "lab@example.test"


def test_authenticate_with_email_is_case_insensitive():
    user = UserFactory(email="doctor@example.test")

    assert authenticate(username="Doctor@Example.test", password=TEST_PASSWORD) == user


def test_inactive_user_cannot_authenticate():
    UserFactory(email="gone@example.test", is_active=False)

    assert authenticate(username="gone@example.test", password=TEST_PASSWORD) is None


def test_wrong_password_does_not_authenticate():
    UserFactory(email="doctor@example.test")

    assert authenticate(username="doctor@example.test", password="wrong") is None


def test_clean_normalises_email_entered_through_forms():
    user = User(email="  Admin.Two@Example.TEST ")

    user.clean()

    assert user.email == "admin.two@example.test"
