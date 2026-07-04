#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python -m mkdocs build --strict
python scripts/verify_end_user_site.py
python scripts/verify_markdown_hashes.py
