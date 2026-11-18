"""Admin for users: no hard delete; users are deactivated instead."""

import pytest
from django.contrib import admin
from django.test import RequestFactory
from django.urls import reverse

from apps.accounts.admin import UserAdmin
from apps.accounts.models import User
from apps.accounts.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def superuser():
    return UserFactory(is_staff=True, is_superuser=True)


def test_user_admin_is_registered():
    assert isinstance(admin.site._registry[User], UserAdmin)


def test_user_admin_never_allows_delete(superuser):
    request = RequestFactory().get("/")
    request.user = superuser

    assert admin.site._registry[User].has_delete_permission(request) is False
    assert admin.site._registry[User].has_delete_permission(request, UserFactory()) is False


def test_user_changelist_has_no_delete_action(client, superuser):
    client.force_login(superuser)

    response = client.get(reverse("admin:accounts_user_changelist"))

    assert response.status_code == 200
    assert "delete_selected" not in response.content.decode()


def test_user_delete_page_is_forbidden(client, superuser):
    client.force_login(superuser)
    target = UserFactory()

    response = client.get(reverse("admin:accounts_user_delete", args=[target.pk]))

    assert response.status_code == 403
    assert User.objects.filter(pk=target.pk).exists()


def test_user_admin_add_and_change_pages_render(client, superuser):
    client.force_login(superuser)

    assert client.get(reverse("admin:accounts_user_add")).status_code == 200
    change = reverse("admin:accounts_user_change", args=[superuser.pk])
    assert client.get(change).status_code == 200
