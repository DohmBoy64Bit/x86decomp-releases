# Build and verification — 0.7.11

Install development dependencies, then run:

```bash
make verify
```

The committed reports, command reference, self-test synchronization, lint/type gates, and source manifests are checked by `make verify` without rewriting tracked files. After an intentional source change, regenerate deterministic artifacts and immediately verify them with:

```bash
make docstrings-update
make command-reference-update
make hashes
make verify-hashes
```

The exact current inventory includes toolkit behavior, supplemental public-surface coverage, and standalone verifier contracts. `make test-suite` remains available for running only the standalone verifier.

Individual gates:

```bash
make compile
make contracts
make docstrings
make command-reference
make self-test-sync
make lint
make typecheck
make verify-hashes
make test
make test-suite
make package
```

The comprehensive harness is configured and run with:

```bash
x86decomp-test init-config --toolkit-root . --output-root ./test-results --install-root ./.x86decomp-test-tools --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

The harness creates the output directory on the first run and writes a unique run directory containing JSON, Markdown, HTML, JUnit, coverage, process, and adapter evidence.
