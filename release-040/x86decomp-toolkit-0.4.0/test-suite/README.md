# x86decomp comprehensive test suite 0.4.0

A separately packaged, no-silent-skip verification harness for **x86decomp-toolkit 0.4.0**.

The harness inventories the toolkit before testing it. It fails when a module, defined function/method, CLI command, JSON Schema, Ghidra script, workflow state, or external adapter changes without an updated pinned catalog and regression coverage.

## Core guarantees

- Detect adapters before asking questions.
- Never prompt for a custom path when an adapter is already detected.
- Ask about a custom path only for a missing adapter.
- Offer installation only after explicit consent and only when a supported installer exists.
- Record unresolved adapter-dependent tests as `BLOCKED`, never skipped or passed.
- Fail strict release mode when anything is blocked.
- Execute at least one direct body line of every defined toolkit Python function/method.
- Parse-test every CLI subcommand.
- Reject any pytest/JUnit skip.
- Build and clean-install release packages.
- Produce separate stdout/stderr and structured event logs for every external process.

Executing every function once is a surface-coverage contract, not proof of every branch or input. Targeted tests, malformed-input tests, integrity checks, migration tests, live adapter probes, coverage floors, and package tests provide the deeper evidence.

## 0.4.0 coverage areas

The suite covers all retained 0.3.1 functionality plus:

- verified target packs and grounded project templates;
- project schema-v3 migration, transactional state, backup/restore/repair/GC;
- content-addressed immutable storage;
- durable pipelines, idempotency, retries, cancellation, heartbeats, stale recovery, and output sealing;
- bounded local/container workers and compiler workers;
- linker reconstruction, C++ recovery, harness generation, convergence, and symbolic flag semantics;
- reproducibility, security audits, dependency audits, SBOMs, and target release gates;
- deterministic generated C/C++ corpora;
- read-only control-plane service state;
- synchronized toolkit/test-suite Mermaid and ASCII architecture maps;
- compatibility from 0.3.1 to 0.4.0.

## Install

From source:

```bash
cd test-suite
python -m pip install -e '.[dev]'
```

From the release wheel:

```bash
python -m pip install x86decomp_test_suite-0.4.0-py3-none-any.whl
```

## Create a configuration

```bash
x86decomp-test init-config \
  --toolkit-root /path/to/x86decomp-toolkit \
  --output-root ./test-results \
  --install-root ./.x86decomp-test-tools \
  --config ./x86decomp-test.json
```

The default is interactive and strict. Network, installation, and host execution remain disabled unless explicitly enabled.

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

Resolve only missing adapters:

```bash
x86decomp-test adapters --config x86decomp-test.json --resolve --verbose
```

Resolution order:

1. configured path;
2. environment variable;
3. system `PATH`;
4. known platform locations;
5. custom-path prompt only when still missing;
6. consent-gated installation only when still unresolved;
7. explicit `BLOCKED` record.

Python adapters may be resolved with a custom interpreter/virtual environment. Historical MSVC is always user-owned and custom-path-only.

## Complete run

```bash
x86decomp-test run --config x86decomp-test.json --verbose
```

Exit codes:

| Code | Meaning |
|---:|---|
| `0` | no failures/errors; blocked tests permitted only in non-strict mode |
| `1` | at least one `FAIL` or `ERROR` |
| `2` | strict mode and at least one `BLOCKED` integration |
| `130` | interrupted |

## What a complete run does

1. Detects/resolves adapters.
2. Builds the exact toolkit inventory and checks catalog drift.
3. Verifies source manifest hashes.
4. Validates JSON Schemas.
5. Parses Ghidra Java scripts.
6. Validates skill frontmatter/release contract.
7. Byte-compiles toolkit and harness.
8. Parse-tests every CLI command.
9. Runs harness self-tests.
10. Runs native and supplemental tests under branch coverage with unrelated pytest plugin autoload disabled.
11. Enforces zero skips and all-defined-function body execution.
12. Enforces line and branch coverage floors.
13. Builds wheel and source distribution.
14. Installs the wheel in a clean environment and probes installed CLI/data.
15. Runs real live operations for every resolved external adapter.
16. Writes complete reports and strict exit status.

## Reports

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
  harness-junit.xml
  coverage.json
  coverage.xml
  coverage-html/
  all-function-coverage.json
  public-api-coverage.json
  tests/<test-id>/stdout.log
  tests/<test-id>/stderr.log
  adapter-work/
  dist/
```

`events.jsonl` records detection, prompt decisions, installation decisions, download hashes, test starts/finishes, result classifications, and final exit code.

## Adapter families

The catalog includes Python/test/schema/build packages, Capstone, Unicorn, Z3, angr, FastAPI/Uvicorn, LIEF, Java, Ghidra, DynamoRIO, objdiff, Clang/Clang++, LLD/LLVM tools, GCC/G++, CMake, Ninja, `pip-audit`, Docker/Podman, and user-owned MSVC.

See [docs/ADAPTERS.md](docs/ADAPTERS.md).

## Architecture

- [Mermaid test-suite map](docs/ARCHITECTURE_MAP.md)
- [ASCII test-suite map](docs/ARCHITECTURE_MAP_ASCII.txt)
- [Separation of concerns](docs/ARCHITECTURE.md)
- [Toolkit Mermaid map](../docs/ARCHITECTURE_MAP.md)

## Self-tests

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
```

Self-tests cover adapter detection/prompting, installer safety, archive safety, configuration, inventory drift, all-function coverage audits, JUnit skip rejection, reporting, process isolation, CLI behavior, and architecture-map synchronization.

## Maintenance

This suite is intentionally version-pinned. Every toolkit release must update the catalog, supplemental tests, adapter catalog, schemas, maps, docs, changelog, verification record, package version, and manifests. See [MAINTENANCE.md](MAINTENANCE.md).
