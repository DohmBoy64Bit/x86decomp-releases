# Build and verification — 0.7.9

Install development dependencies, then run:

```bash
make verify
```

The committed source manifests are verified by `make verify`. After an intentional source change, regenerate and immediately verify them with:

```bash
make hashes
make verify-hashes
```

The exact current inventory includes toolkit behavior, supplemental public-surface coverage, and standalone verifier contracts. `make test-suite` remains available for running only the standalone verifier.

Individual gates:

```bash
make compile
make contracts
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
