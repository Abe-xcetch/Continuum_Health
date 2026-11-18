"""Home page, health endpoint and base-template guarantees."""

from unittest import mock

import pytest
from django.db import OperationalError
from django.urls import reverse

from apps.accounts.tests.factories import UserFactory

pytestmark = pytest.mark.django_db

HOME_URL = reverse("core:home")
HEALTH_URL = reverse("core:health")
LOGIN_URL = reverse("accounts:login")


# --- Home -------------------------------------------------------------------


def test_home_redirects_anonymous_user_to_login(client):
    response = client.get(HOME_URL)

    assert response.status_code == 302
    assert response["Location"] == f"{LOGIN_URL}?next={HOME_URL}"


def test_home_renders_full_page_for_authenticated_user(client):
    client.force_login(UserFactory(email="clinician@example.test"))

    response = client.get(HOME_URL)
    html = response.content.decode()

    assert response.status_code == 200
    assert "<html" in html
    assert "clinician@example.test" in html
    assert 'action="/accounts/logout/"' in html


def test_home_renders_partial_only_for_htmx_request(client):
    client.force_login(UserFactory())

    response = client.get(HOME_URL, HTTP_HX_REQUEST="true")
    html = response.content.decode()

    assert response.status_code == 200
    assert "<html" not in html
    assert 'id="home-content"' in html


# --- Base template ------------------------------------------------------------


def test_body_sends_csrf_token_header_for_htmx(client):
    response = client.get(LOGIN_URL)
    html = response.content.decode()
    token = response.context["csrf_token"]

    assert f'hx-headers=\'{{"X-CSRFToken": "{token}"}}\'' in html


def test_base_template_loads_local_assets_only(client):
    html = client.get(LOGIN_URL).content.decode()

    assert "/static/vendor/htmx" in html
    assert "/static/vendor/alpine" in html
    assert "/static/css/app.css" in html
    assert "cdn" not in html.lower()
    assert "<script>" not in html  # no inline scripts (strict CSP)


def test_base_template_has_skip_link_and_main_landmark(client):
    html = client.get(LOGIN_URL).content.decode()

    assert 'href="#main"' in html
    assert '<main id="main"' in html


def test_strict_content_security_policy_header(client):
    csp = client.get(LOGIN_URL)["Content-Security-Policy"]

    assert "script-src 'self'" in csp
    assert "unsafe-inline" not in csp
    assert "unsafe-eval" not in csp
    assert "frame-ancestors 'none'" in csp


def test_security_headers(client):
    response = client.get(LOGIN_URL)

    assert response["X-Frame-Options"] == "DENY"
    assert response["X-Content-Type-Options"] == "nosniff"
    assert response["Referrer-Policy"] == "same-origin"


# --- Health -------------------------------------------------------------------


def test_health_is_public_and_reports_ok(client):
    response = client.get(HEALTH_URL)

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_reports_503_when_database_unavailable(client):
    with mock.patch("apps.core.views.connection") as conn:
        conn.cursor.side_effect = OperationalError("down")
        response = client.get(HEALTH_URL)

    assert response.status_code == 503
    assert response.json() == {"status": "unavailable"}


def test_health_rejects_non_get(client):
    assert client.post(HEALTH_URL).status_code == 405


def test_health_response_is_not_cached(client):
    assert "no-store" in client.get(HEALTH_URL)["Cache-Control"]
