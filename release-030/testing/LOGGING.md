# Logging contract

## Human log

`run.log` contains UTC timestamps, log levels, phase transitions, and run summaries.

## Event stream

`events.jsonl` is append-only during a run. Events include:

- logging configuration;
- run start and completion;
- adapter detection and missing-adapter declarations;
- custom-path prompt decisions and validation attempts;
- install decisions, commands, downloads, hashes, and failures;
- every process test start and finish.

Each line is independent JSON and can be streamed into CI or observability systems.

## Per-test process logs

Every process test receives a dedicated directory with `stdout.log` and `stderr.log`. Reports reference the exact paths. Output is never merged, truncated, or discarded by the harness.

## Structured reports

- `adapters.json`: resolved path, source, version, and diagnostics for every adapter.
- `inventory.json`: discovered modules, commands, functions, schemas, and scripts.
- `catalog-audit.json`: exact stale/uncataloged differences.
- `all-function-coverage.json`: canonical all-function execution audit.
- `public-api-coverage.json`: retained compatibility alias with identical content.
- `results.json`: canonical run report.
- `REPORT.md`: review-friendly report.
- `report.html`: standalone visual report.
- `junit.xml` and `harness-junit.xml`: testcase reports.
- `coverage.json`, `coverage.xml`, and `coverage-html/`: source coverage.

Paths may expose workstation directory names. Review reports before publishing them publicly.
