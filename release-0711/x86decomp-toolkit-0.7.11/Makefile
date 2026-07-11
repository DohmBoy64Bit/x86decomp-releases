.PHONY: verify test test-suite compile contracts docs docstrings docstrings-update command-reference command-reference-update self-test-sync lint typecheck corpus-sync verify-hashes hashes package install editable clean

verify: compile contracts docs docstrings command-reference self-test-sync lint typecheck corpus-sync verify-hashes test

compile:
	python3 -m compileall -q src tests scripts test-suite/src test-suite/tests

contracts:
	PYTHONPATH=src python3 scripts/validate-contracts.py

docs:
	python3 -m mkdocs build --strict --site-dir build/site

docstrings:
	python3 scripts/audit-docstrings.py --check

docstrings-update:
	python3 scripts/audit-docstrings.py --write

command-reference:
	PYTHONPATH=src python3 scripts/generate_command_reference.py --check

command-reference-update:
	PYTHONPATH=src python3 scripts/generate_command_reference.py

self-test-sync:
	python3 scripts/verify_self_test_sync.py

lint:
	python3 -m ruff check src tests scripts test-suite/src test-suite/tests

typecheck:
	python3 -m pyright

corpus-sync:
	python3 scripts/verify-corpus-sync.py

verify-hashes:
	python3 scripts/source_hashes.py verify

hashes:
	python3 scripts/source_hashes.py generate

test:
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=src:test-suite/src python3 scripts/run-pytest-partitions.py

test-suite:
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=test-suite/src python3 -m pytest -q test-suite/tests

package:
	python3 -m build
	python3 -m build test-suite --outdir test-suite/dist

install:
	python3 -m pip install .

editable:
	python3 -m pip install -e '.[disassembly,dynamic,symbolic,service,dev]'
	python3 -m pip install -e 'test-suite[dev]'

clean:
	rm -rf build dist test-suite/build test-suite/dist *.egg-info src/*.egg-info test-suite/src/*.egg-info
	rm -rf .coverage htmlcov .pytest_cache .ruff_cache .mypy_cache .tox test-suite/.pytest_cache test-results .x86decomp-test-tools tools x86decomp-test.json test-suite/test-results test-suite/.x86decomp-test-tools
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
