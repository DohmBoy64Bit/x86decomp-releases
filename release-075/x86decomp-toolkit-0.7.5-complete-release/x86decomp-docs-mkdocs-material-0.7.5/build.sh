#!/usr/bin/env sh
set -eu
python -m mkdocs build --strict --clean
python scripts/canonicalize_site.py site
python scripts/verify_end_user_site.py
python scripts/verify_built_site.py
