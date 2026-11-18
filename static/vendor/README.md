# Vendored frontend libraries

Bundled locally: no runtime CDN dependency (continuum-frontend skill). Each file is
byte-identical to the `dist/` file inside the official npm package, which was checked
against the registry's published integrity hash.

| File | Package | Version | Published | SHA-256 |
|---|---|---|---|---|
| `htmx-2.0.11.min.js` | `htmx.org` (`dist/htmx.min.js`) | 2.0.11 | 2026-09-22 | `d6fdc75f204e6bdefa99b69bf1e6d4ac69b8a364f77929f45c13476b4000f717` |
| `alpine-csp-3.17.5.min.js` | `@alpinejs/csp` (`dist/cdn.min.js`) | 3.17.5 | 2026-10-20 | `48c170c92032e527cbae71b8ce75cf1f96ca06fa869a6120ef0fe438d8e92c36` |

Notes:
- **Alpine CSP build**: the standard Alpine build needs `unsafe-eval`, which our Content
  Security Policy forbids. The CSP build only evaluates simple expressions; anything more
  must be registered with `Alpine.data()` in a static JS file under `static/js/`.
- **HTMX 2.x on purpose**: HTMX 4 exists, but django-htmx and the continuum-frontend
  conventions target 2.x. Upgrading major versions is a separate decision.
- Verify a file: `Get-FileHash static\vendor\<file> -Algorithm SHA256` (PowerShell).

To upgrade: download the new `dist/` file from the npm tarball, verify the tarball's
`integrity` against `https://registry.npmjs.org/<package>/<version>`, rename with the new
version, update this table and the `<script>` tags in `templates/base.html`.
