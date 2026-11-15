---
name: continuum-frontend
description: Use when building Continuum's user interface: Django templates with HTMX, Alpine.js and Tailwind CSS, including forms, partials, layouts and accessibility.
---

# Continuum: frontend conventions

Chosen stack: **Django templates + HTMX + Alpine.js + Tailwind CSS**, server-rendered. Reasons: one language and codebase, fast pages on slow connections and low-end devices, Django auth/CSRF/permissions apply directly, no separate SPA build to maintain. Revisit (e.g. React PWA) only if offline data entry becomes a hard requirement.

## Structure
- `templates/base.html` → layout blocks; `templates/components/` for reusable pieces (buttons, form fields, tables, modals, alerts).
- Per app: `templates/<app>/<page>.html` and `templates/<app>/partials/_<fragment>.html`.
- Use django-template-partials or `{% include %}` with explicit context; django-widget-tweaks or crispy-forms (Tailwind pack) for form rendering.
- Tailwind built via the standalone CLI or django-tailwind; no CDN in production. Bundle HTMX and Alpine locally (no runtime CDN dependency).

## HTMX rules
- The same view serves full page or partial: check `request.htmx` (django-htmx) and render the partial template.
- Every HTMX request carries the CSRF token: set `hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'` on `<body>`.
- Use `hx-get` for reads, `hx-post` for writes; never change data on GET.
- Forms: on validation error return the form partial with errors (status 422); on success return the updated fragment or `HX-Redirect`.
- Show progress with `hx-indicator`; disable submit buttons during requests (`hx-disabled-elt`) to prevent double submission.
- Search-as-you-type: `hx-trigger="keyup changed delay:300ms"`.
- Permission checks live in the view, never only in the template.

## Alpine.js
- Only for local UI state (toggles, tabs, modals, dependent fields). No business logic or data fetching in Alpine; that goes through HTMX to Django.

## Templates and security
- Rely on auto-escaping; never `|safe` on user-supplied content.
- No secrets or internal IDs in HTML; use UUIDs in URLs.
- Don't put patient identifiers in URLs or query strings beyond the opaque UUID.

## Usability and accessibility
- Mobile-first layouts; must work on a small Android phone and a desktop at a nursing station.
- Every input has a `<label>`; errors shown next to the field and announced (`aria-live`).
- Keyboard reachable controls; visible focus states; colour contrast AA; never colour alone to convey status.
- Keep pages light: paginate tables, lazy-load heavy panels with `hx-trigger="revealed"`.

## Testing
- View tests assert both full-page and HTMX (`HTTP_HX_REQUEST=true`) responses.
- Playwright E2E for critical journeys only (login, register patient, record visit).
