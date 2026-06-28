# x86decomp comprehensive test suite 0.3.0

A standalone, regression-oriented verification harness for **x86decomp-toolkit 0.3.0**.

The suite inventories the toolkit before testing it. It fails when a command, Python module, schema, Ghidra script, workflow state, or declared external adapter is added or removed without updating the pinned feature catalog. Missing external tools are never silently skipped: their live tests are recorded as `BLOCKED`, and strict mode returns a non-zero exit code.

## What it verifies

The default complete run performs all of the following:

1. Detects every declared adapter before asking any questions.
2. Prompts for a custom path **only** for an adapter that was not detected.
3. Optionally installs missing adapters after explicit install/network consent.
4. Inventories every toolkit Python module, public function/method, CLI command, JSON Schema, and Ghidra script.
5. Compares that inventory with a version-pinned feature catalog.
6. Verifies source-file hashes from `MANIFEST.sha256`.
7. Validates all JSON Schemas.
8. Parses every Ghidra Java script.
9. Validates the agent skill frontmatter.
10. Byte-compiles the toolkit and the test harness.
11. Parse-tests `--help` for every discovered CLI subcommand.
12. Runs the toolkit's native tests plus supplemental public-API tests under branch coverage.
13. Rejects any pytest/JUnit skipped test.
14. Audits coverage so every discovered function/method executes at least one direct body line.
15. Enforces configurable line and branch coverage floors.
16. Builds the toolkit wheel and source distribution.
17. Installs the built wheel in a clean virtual environment and probes the installed CLI.
18. Runs a real live probe for every resolved adapter.
19. Emits JSON, Markdown, HTML, JUnit, coverage, text, and JSONL event logs.

Executing a function once is not a proof of correctness for every input. The suite combines surface execution, targeted regression cases, contracts, structural checks, coverage, and live integrations. Future releases must expand targeted tests when behavior grows.

## Install

From the source tree:

```bash
python -m pip install -e .[dev]
```

Or install the wheel:

```bash
python -m pip install x86decomp_test_suite-0.3.0-py3-none-any.whl
```

## Configure

```bash
x86decomp-test init-config \
  --toolkit-root /path/to/x86decomp-toolkit \
  --output-root ./test-results \
  --config ./x86decomp-test.json
```

The default configuration is interactive and strict. Network access, installation, and host execution are disabled unless explicitly enabled.

Example configuration:

```json
{
  "schema_version": 1,
  "toolkit_root": "/path/to/x86decomp-toolkit",
  "output_root": "./test-results",
  "adapter_paths": {},
  "install_root": "./.x86decomp-test-tools",
  "python_executable": "/path/to/python",
  "strict": true,
  "interactive": true,
  "allow_network": false,
  "allow_install": false,
  "allow_host_execution": false,
  "timeout_seconds": 900,
  "line_coverage_floor": 70.0,
  "branch_coverage_floor": 50.0,
  "require_public_api_execution": true,
  "custom_environment": {}
}
```

## Adapter resolution

Inspect without prompting:

```bash
x86decomp-test adapters --config x86decomp-test.json
```

Resolve missing adapters interactively:

```bash
x86decomp-test adapters --config x86decomp-test.json --resolve
```

The resolver follows this exact order:

1. Configured path.
2. Adapter environment variables.
3. `PATH`.
4. Known platform-specific locations.
5. Only when still missing: ask whether the user has a custom path.
6. Only when still missing: offer automatic installation where a safe contract exists.
7. If unresolved: record the adapter and every dependent test as `BLOCKED`.

An already detected adapter does not trigger a prompt.

Automatic installation requires `allow_install: true`. Network downloads additionally require `allow_network: true`. Proprietary historical MSVC toolchains are never redistributed; the resolver accepts a user-owned custom path.

## Run everything

```bash
x86decomp-test run --config x86decomp-test.json --verbose
```

Exit codes:

| Code | Meaning |
|---:|---|
| `0` | No failures/errors; in non-strict mode, blocked external integrations may remain |
| `1` | At least one failed or errored test |
| `2` | Strict mode and at least one test is blocked by an unresolved adapter |
| `130` | Interrupted by the user |

Strict mode is the release-gating mode. It ensures that unavailable integrations cannot be mistaken for passing coverage.

## Reports

Each run creates an immutable run directory containing:

```text
run-<timestamp>-<id>/
  run.log
  events.jsonl
  adapters.json
  inventory.json
  catalog-audit.json
  results.json
  REPORT.md
  report.html
  junit.xml
  coverage.json
  coverage.xml
  coverage-html/
  public-api-coverage.json
  tests/<test-id>/stdout.log
  tests/<test-id>/stderr.log
  adapter-work/
  distributions/
```

`events.jsonl` records adapter detection, installation commands, downloads, test starts, test finishes, and run completion. Each process test gets separate stdout and stderr files.

## External adapters

The catalog currently covers Python, pytest, coverage.py, jsonschema, javalang, PyYAML, build, Capstone, Unicorn, Z3, angr, FastAPI, Uvicorn, LIEF, Java, Ghidra, DynamoRIO, objdiff, Clang/Clang++, LLD, LLVM archive/object tools, GCC/G++, CMake, Ninja, and a user-owned MSVC toolchain.

See [`docs/ADAPTERS.md`](docs/ADAPTERS.md) for detection and installation details.

## Run harness self-tests

```bash
python -m pytest -q
```

The self-tests verify prompting rules, adapter detection, safe archive extraction, installer command construction, configuration round trips, inventory drift detection, coverage auditing, JUnit skip detection, reports, logs, process isolation, and CLI behavior.

## Future release maintenance

The suite is version-pinned by design. For every toolkit release, update the feature catalog, supplemental tests, adapter catalog, schemas, documentation, and release verification record. See [`MAINTENANCE.md`](MAINTENANCE.md).
