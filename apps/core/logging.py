"""Logging filter adding request and user IDs. Never log patient identifiers."""

import logging

from apps.core.middleware import current_request_id, current_user_id


class RequestIDFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = current_request_id() or "-"
        record.user_id = current_user_id() or "-"
        return True
