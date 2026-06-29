# Logging contract — 0.4.0

## Human and machine streams

`run.log` records UTC time, level, phase, adapter, test ID, and summaries.
`events.jsonl` is the append-only machine stream for configuration, detection, prompts,
install consent, downloads/hashes, process starts/completions, results, and exit policy.

## Per-test process logs

Every subprocess receives a dedicated directory with `stdout.log` and `stderr.log`.
Commands are stored as argument arrays. Timeout, return code, working directory,
environment policy, executable identity, and output paths remain distinguishable.

## Canonical reports

- `adapters.json`: path, source, version, and diagnostics for each adapter.
- `inventory.json`: discovered modules, functions/methods, commands, schemas, and scripts.
- `catalog-audit.json`: uncataloged and stale surfaces.
- `all-function-coverage.json`: AST-to-coverage execution audit.
- `public-api-coverage.json`: compatibility alias of the same body-execution report.
- `results.json`: canonical run result model.
- `REPORT.md` and `report.html`: human projections.
- `junit.xml` and `harness-junit.xml`: pytest testcase records.
- `coverage.json`, `coverage.xml`, and `coverage-html/`: code coverage.
- `tests/<test-id>/`: isolated command and output logs.

A `BLOCKED` adapter test includes the unresolved adapter ID and diagnostics. It is never
omitted from results. Reports can expose workstation paths and environment details;
review/redact before public release.
