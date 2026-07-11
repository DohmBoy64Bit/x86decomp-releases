# Build and verification

Install development dependencies, then run the comprehensive verification gate:

```bash
make verify
```

The committed reports, command reference, self-test synchronization, lint/type gates, and
source manifests are checked by `make verify` without rewriting tracked files.

## After source changes

After an intentional source change, regenerate deterministic artifacts and immediately
verify them:

```bash
make docstrings-update
make command-reference-update
make hashes
make verify-hashes
```

## Individual gates

| Command | What it checks |
|---|---|
| `make compile` | Compiles the toolkit via setuptools |
| `make contracts` | Validates all JSON schemas and example documents |
| `make docstrings` | Checks docstring coverage across the public API |
| `make command-reference` | Regenerates the command reference from argparse |
| `make self-test-sync` | Verifies the test suite surface matches the toolkit surface |
| `make lint` | Runs pylint and flake8 |
| `make typecheck` | Runs mypy in strict mode |
| `make verify-hashes` | Checks all content hashes against the manifest |
| `make test` | Runs the toolkit-level test suite |
| `make test-suite` | Runs the standalone verifier (`x86decomp-test`) |
| `make package` | Builds the wheel and source distribution |

## Test harness

The comprehensive harness is configured and run with:

```bash
x86decomp-test init-config \
  --toolkit-root . \
  --output-root ./test-results \
  --install-root ./.x86decomp-test-tools \
  --config ./x86decomp-test.json

x86decomp-test run --config ./x86decomp-test.json --verbose
```

The harness creates the output directory on the first run and writes a unique run
directory containing JSON, Markdown, HTML, JUnit, coverage, process, and adapter evidence.

## Inventory

The exact current inventory includes toolkit behavior, supplemental public-surface coverage,
and standalone verifier contracts. `make test-suite` remains available for running only the
standalone verifier.
