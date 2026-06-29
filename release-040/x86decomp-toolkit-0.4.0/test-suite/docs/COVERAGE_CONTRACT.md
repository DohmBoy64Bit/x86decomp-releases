# Coverage and completeness contract

The suite uses independent dimensions rather than treating one percentage as proof of
correctness.

## Exact source-surface inventory

Dynamic inventory discovers:

- every `x86decomp.*` Python module;
- every defined module-level function, including private helpers;
- every defined class method, including private helpers;
- every CLI subcommand;
- every JSON Schema;
- every Ghidra Java script;
- matching and functional workflow states;
- every declared adapter contract.

The discovered set must exactly match `feature_catalog.json`. New or removed surfaces
fail until the catalog and tests are reviewed together.

## Function-body execution

Coverage JSON is correlated with AST body lines. Every defined function and method must
execute at least one direct body line. Missing symbols are reported by fully qualified
ID. This detects complete test omission; it does not claim exhaustive branch or input
coverage.

## CLI coverage

Every discovered command receives an independent process-level `--help` parser test.
Semantic behavior is covered by native regressions, supplemental API contracts, and
live-adapter tests.

## No-skip and blocked-adapter policy

JUnit must report zero pytest skips. External unavailability is modeled outside pytest
as an explicit `BLOCKED` result. Strict mode rejects blocked release gates.

## Thresholds

Default floors:

- statement coverage: 70%;
- branch coverage: 50%;
- defined function/method body execution: 100%;
- pytest skips: 0.

Floors may be raised. Lowering them requires an explicit reviewed compatibility record;
it must not be used to conceal regressions.

## Structural and operational contracts

Coverage is supplemented by source hashes, schema validation, Java syntax, skill
frontmatter, architecture-map synchronization, compatibility contracts, migrations,
backup/restore, pipeline resumability, concurrency/cancellation, clean package
installation, and real adapter probes.
