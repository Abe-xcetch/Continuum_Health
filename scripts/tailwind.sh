#!/usr/bin/env bash
# Build Continuum's CSS with the Tailwind standalone CLI on Linux (CI, deploy).
# Windows developers use scripts/tailwind.ps1. Keep the version in sync with it.
set -euo pipefail

VERSION="v4.3.3"
SHA256="dc61b3ac6b8c9ca874c0cc4c57b2409791a64c5540404ca5f5367360babc313a"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BIN="$ROOT/bin/tailwindcss-$VERSION"
URL="https://github.com/tailwindlabs/tailwindcss/releases/download/$VERSION/tailwindcss-linux-x64"

if [[ ! -x "$BIN" ]]; then
  mkdir -p "$ROOT/bin"
  curl -sSfL "$URL" -o "$BIN.download"
  echo "$SHA256  $BIN.download" | sha256sum --check --status \
    || { echo "Tailwind CLI checksum mismatch" >&2; rm -f "$BIN.download"; exit 1; }
  mv "$BIN.download" "$BIN"
  chmod +x "$BIN"
fi

"$BIN" -i "$ROOT/static/src/app.css" -o "$ROOT/static/css/app.css" --minify "$@"
