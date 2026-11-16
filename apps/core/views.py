import logging

from django.contrib.auth.decorators import login_required
from django.db import DatabaseError, connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)


@login_required
@require_GET
def home(request: HttpRequest) -> HttpResponse:
    """Authenticated placeholder home page. Serves the partial for HTMX requests."""
    template = "core/partials/_home_content.html" if request.htmx else "core/home.html"  # type: ignore[attr-defined]
    return render(request, template)


@never_cache
@require_GET
def health(request: HttpRequest) -> JsonResponse:
    """Liveness + database check for load balancers. Public; reveals nothing internal."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except DatabaseError:
        logger.exception("Health check: database unavailable")
        return JsonResponse({"status": "unavailable"}, status=503)
    return JsonResponse({"status": "ok"})
