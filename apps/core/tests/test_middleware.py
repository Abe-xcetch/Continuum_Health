"""Request ID middleware and the logging filter that adds request/user IDs to log lines."""

import logging

import pytest
from django.http import HttpResponse
from django.test import RequestFactory

from apps.core.logging import RequestIDFilter
from apps.core.middleware import RequestIDMiddleware, current_request_id


def _ok(_request):
    return HttpResponse("ok")


def test_generates_request_id_and_returns_it_in_header():
    request = RequestFactory().get("/")

    response = RequestIDMiddleware(_ok)(request)

    assert len(request.request_id) == 32
    assert response["X-Request-ID"] == request.request_id


def test_accepts_a_well_formed_incoming_request_id():
    request = RequestFactory().get("/", HTTP_X_REQUEST_ID="abc-123")

    response = RequestIDMiddleware(_ok)(request)

    assert response["X-Request-ID"] == "abc-123"


@pytest.mark.parametrize("bad", ["has space", "x" * 65, "<script>", ""])
def test_replaces_malformed_incoming_request_id(bad):
    request = RequestFactory().get("/", HTTP_X_REQUEST_ID=bad)

    response = RequestIDMiddleware(_ok)(request)

    assert response["X-Request-ID"] != bad
    assert len(response["X-Request-ID"]) == 32


def test_request_id_context_is_cleared_after_response():
    RequestIDMiddleware(_ok)(RequestFactory().get("/"))

    assert current_request_id() is None


def test_log_filter_adds_placeholders_outside_a_request():
    record = logging.LogRecord("x", logging.INFO, __file__, 1, "msg", None, None)

    assert RequestIDFilter().filter(record) is True
    assert record.request_id == "-"
    assert record.user_id == "-"


def test_log_filter_uses_current_request_id_inside_a_request():
    seen = {}

    def view(request):
        record = logging.LogRecord("x", logging.INFO, __file__, 1, "msg", None, None)
        RequestIDFilter().filter(record)
        seen["request_id"] = record.request_id
        return HttpResponse("ok")

    request = RequestFactory().get("/")
    RequestIDMiddleware(view)(request)

    assert seen["request_id"] == request.request_id
