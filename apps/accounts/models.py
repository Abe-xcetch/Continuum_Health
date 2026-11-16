"""Custom user model.

SCOPE: this model is for **staff and clinician accounts**, which log in with email + password.

OPEN DECISION: patient login is NOT designed yet. PRD §11.4 describes patients
authenticating with their Continuum Patient ID or username, with OTP, and many pilot
patients may not have an email address. Patient login will most likely be a separate
authentication path (its own backend and flow), not this email login. Do not add
patient fields here until that decision is made (see docs/prd-review.md §f).

Roles, facilities and permissions are also pending PRD decisions and are out of scope.
"""

from __future__ import annotations

from typing import Any, ClassVar

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.functions import Lower

from apps.core.models import PublicIdModel, TimeStampedModel


class UserManager(BaseUserManager["User"]):
    use_in_migrations = True

    @classmethod
    def normalize_email(cls, email: str | None) -> str:
        # Lowercase the whole address so lookups and the unique constraint agree.
        return (email or "").strip().lower()

    def get_by_natural_key(self, username: str | None) -> User:
        return self.get(email=self.normalize_email(username))

    def create_user(self, email: str, password: str | None = None, **extra: Any) -> User:
        email = self.normalize_email(email)
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=email, **extra)
        user.set_password(password)  # None -> unusable password
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str | None = None, **extra: Any) -> User:
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        for flag in ("is_staff", "is_superuser"):
            if extra[flag] is not True:
                raise ValueError(f"Superuser must have {flag}=True.")
        return self.create_user(email, password, **extra)


class User(PublicIdModel, TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """Staff/clinician account. Deactivate with ``is_active``; users are never deleted."""

    # unique=True is required by Django for USERNAME_FIELD; the Lower() constraint below
    # additionally makes the database reject case variants (Nurse@x vs nurse@x).
    email = models.EmailField("email address", max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, help_text="Can log in to the Django admin site.")

    objects: ClassVar[UserManager] = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[list[str]] = []

    class Meta:
        constraints = [
            models.UniqueConstraint(Lower("email"), name="accounts_user_email_ci_unique"),
        ]

    def __str__(self) -> str:
        return self.email

    def clean(self) -> None:
        super().clean()
        self.email = UserManager.normalize_email(self.email)
