"""Login and logout pages for staff/clinician accounts."""

import pytest
from django.urls import reverse

from apps.accounts.tests.factories import TEST_PASSWORD, UserFactory

pytestmark = pytest.mark.django_db

LOGIN_URL = reverse("accounts:login")
LOGOUT_URL = reverse("accounts:logout")
HOME_URL = reverse("core:home")


def test_login_page_renders_labelled_email_and_password_fields(client):
    response = client.get(LOGIN_URL)
    html = response.content.decode()

    assert response.status_code == 200
    assert 'type="email"' in html
    assert 'autocomplete="email"' in html
    assert 'for="id_username"' in html
    assert 'for="id_password"' in html


def test_valid_login_redirects_to_home(client):
    UserFactory(email="nurse@example.test")

    response = client.post(
        LOGIN_URL, {"username": "nurse@example.test", "password": TEST_PASSWORD}
    )

    assert response.status_code == 302
    assert response["Location"] == HOME_URL
    assert "_auth_user_id" in client.session


def test_invalid_login_shows_error_and_does_not_log_in(client):
    UserFactory(email="nurse@example.test")

    response = client.post(LOGIN_URL, {"username": "nurse@example.test", "password": "wrong"})

    assert response.status_code == 200
    assert 'role="alert"' in response.content.decode()
    assert "_auth_user_id" not in client.session


def test_login_ignores_external_next_redirect(client):
    UserFactory(email="nurse@example.test")

    response = client.post(
        f"{LOGIN_URL}?next=https://evil.example/",
        {"username": "nurse@example.test", "password": TEST_PASSWORD},
    )

    assert response["Location"] == HOME_URL


def test_logout_requires_post(client):
    client.force_login(UserFactory())

    assert client.get(LOGOUT_URL).status_code == 405
    assert "_auth_user_id" in client.session


def test_logout_by_post_ends_session_and_redirects_to_login(client):
    client.force_login(UserFactory())

    response = client.post(LOGOUT_URL)

    assert response.status_code == 302
    assert response["Location"] == LOGIN_URL
    assert "_auth_user_id" not in client.session
