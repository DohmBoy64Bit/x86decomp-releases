# Test-suite architecture — 0.4.0

Visual release artifacts:

- Mermaid: [`ARCHITECTURE_MAP.md`](ARCHITECTURE_MAP.md)
- plain-text ASCII: [`ARCHITECTURE_MAP_ASCII.txt`](ARCHITECTURE_MAP_ASCII.txt)

## Separation of concerns

- `config.py`: configuration and path serialization.
- `models.py`: immutable adapter/test/run records and exit policy.
- `adapters/catalog.py`: declarative adapter contracts.
- `adapters/detection.py`: detection and version probing.
- `adapters/installation.py`: consent and installer orchestration.
- `adapters/download.py`: bounded download and safe extraction.
- `inventory.py`: exact source/CLI/schema/Ghidra/function discovery.
- `coverage_audit.py`: AST-to-coverage body execution.
- `suites.py`: structural, CLI, native, supplemental, coverage, self-test, and package phases.
- `live_adapters.py`: bounded real probes for resolved external tools.
- `process.py`: timeouts, environment isolation, and per-test logs.
- `logging_utils.py`: text and JSONL streams.
- `reports.py`: JSON, Markdown, HTML, and JUnit projections.
- `orchestrator.py`: deterministic phase order; no individual test logic.
- `cli.py`: user interface only.

No phase owns toolkit truth. It emits a `TestResult`; the run summary alone computes the
final exit code. Live unavailability is `BLOCKED`, not a pytest skip.

## Release feedback loop

Inventory drift, compatibility regression, failed production-control tests, stale maps,
package-install failure, or unresolved strict adapters returns the release to
implementation. The four Mermaid/ASCII maps, feature catalog, maintenance contract,
skill, changelog, project memory, and verification records must agree before sealing.
