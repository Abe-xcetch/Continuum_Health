"""Request ID middleware: every request gets an ID that appears in logs and responses."""

import re
import uuid
from collections.abc import Callable
from contextvars import ContextVar
from typing import Any

from django.http import HttpRequest, HttpResponse

REQUEST_ID_HEADER = "X-Request-ID"
_VALID_REQUEST_ID = re.compile(r"^[A-Za-z0-9-]{1,64}$")

_request_id: ContextVar[str | None] = ContextVar("request_id", default=None)
_user_id: ContextVar[str | None] = ContextVar("user_id", default=None)


def current_request_id() -> str | None:
    return _request_id.get()


def current_user_id() -> str | None:
    return _user_id.get()


class RequestIDMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        incoming = request.headers.get(REQUEST_ID_HEADER, "")
        request_id = incoming if _VALID_REQUEST_ID.match(incoming) else uuid.uuid4().hex
        request.request_id = request_id  # type: ignore[attr-defined]
        rid_token = _request_id.set(request_id)
        uid_token = _user_id.set(None)
        try:
            response = self.get_response(request)
        finally:
            _request_id.reset(rid_token)
            _user_id.reset(uid_token)
        response[REQUEST_ID_HEADER] = request_id
        return response

    def process_view(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        # Runs after AuthenticationMiddleware, so request.user is available here.
        user = getattr(request, "user", None)
        if user is not None and user.is_authenticated:
            _user_id.set(str(user.pk))
