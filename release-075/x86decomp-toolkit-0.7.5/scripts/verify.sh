#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
python3 -m compileall -q src tests scripts test-suite/src test-suite/tests
PYTHONPATH=src python3 scripts/validate-contracts.py
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=src:test-suite/src python3 -m pytest -q
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=test-suite/src python3 -m pytest -q test-suite/tests
