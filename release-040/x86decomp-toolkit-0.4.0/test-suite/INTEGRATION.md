# Test-suite integration — 0.4.0

The comprehensive harness is bundled at the stable source path while remaining a
separately installable package:

```text
x86decomp-toolkit/
  pyproject.toml
  src/
  tests/
  test-suite/
    pyproject.toml
    src/
    tests/
    docs/
```

Do not merge the package definitions. Test-only dependencies, adapter installers, and
network/host-execution consent must not become toolkit runtime dependencies.

## Run from the bundled tree

```bash
cd test-suite
python -m pip install -e '.[dev]'
x86decomp-test init-config \
  --toolkit-root .. \
  --output-root ./test-results \
  --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

Generated config, results, downloads, adapter installations, build products, coverage,
and virtual environments are ignored and must not be committed or packaged.

## CI release mode

```json
{
  "strict": true,
  "interactive": false,
  "allow_network": false,
  "allow_install": false
}
```

CI images supply adapter paths or environment variables. Exit code `2` means one or
more declared live integrations remain untested. Release pytest subprocesses disable
third-party plugin autoload to prevent host-plugin interference.

## Standalone use

`test-suite/` may be copied beside the toolkit and renamed. Set `--toolkit-root`
explicitly. The exact feature catalog remains version-pinned to the toolkit release.
