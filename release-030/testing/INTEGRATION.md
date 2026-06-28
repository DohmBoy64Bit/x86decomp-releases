# Adding this suite to the toolkit repository

The suite is intentionally standalone. It can remain beside the toolkit:

```text
workspace/
  x86decomp-toolkit/
  x86decomp-test-suite-0.3.0/
```

Or be copied into the toolkit as:

```text
x86decomp-toolkit/
  testing/
    comprehensive/
      pyproject.toml
      src/
      tests/
      docs/
      schemas/
```

Do not merge its package metadata into the toolkit package. Keeping a separate `pyproject.toml` prevents test-only dependencies and adapter-install behavior from becoming runtime dependencies of `x86decomp-toolkit`.

From the standalone directory:

```bash
python -m pip install -e .[dev]
x86decomp-test init-config \
  --toolkit-root ../x86decomp-toolkit \
  --output-root ./test-results \
  --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

From `testing/comprehensive/` inside the toolkit:

```bash
python -m pip install -e .[dev]
x86decomp-test init-config \
  --toolkit-root ../.. \
  --output-root ./test-results \
  --config ./x86decomp-test.json
```

## CI release gate

Commit a non-interactive config with explicit adapter paths supplied by the CI image:

```json
{
  "strict": true,
  "interactive": false,
  "allow_network": false,
  "allow_install": false
}
```

A release CI environment should preinstall all adapters. Exit code `2` means an integration is unresolved and therefore untested; it is not a successful release gate.
