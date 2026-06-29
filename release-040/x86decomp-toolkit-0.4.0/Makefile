.PHONY: verify test test-suite compile contracts package install editable clean

verify: compile contracts test test-suite

compile:
	python3 -m compileall -q src tests scripts test-suite/src test-suite/tests

contracts:
	PYTHONPATH=src python3 scripts/validate-contracts.py

test:
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=src:test-suite/src python3 -m pytest -q

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
	rm -rf .coverage htmlcov .pytest_cache test-suite/.pytest_cache test-suite/test-results test-suite/.x86decomp-test-tools
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
