# Coverage and completeness contract

The suite uses several independent dimensions rather than treating a single test count as complete coverage.

## Surface inventory

The harness dynamically discovers:

- every `x86decomp.*` Python module;
- every public module-level function;
- every public class and public method;
- every CLI subcommand;
- every JSON Schema;
- every Ghidra Java script;
- both matching and functional workflow states.

The discovered set must exactly match `feature_catalog.json`. New or removed surfaces fail the inventory test until the catalog and tests are intentionally updated.

## Function-body execution

Coverage JSON is correlated with the AST inventory. Every public function and method must execute at least one direct body line. Class declarations must execute during import. A missing function is listed by module-qualified symbol ID.

This rule detects untested public APIs. It does not claim exhaustive input-space or branch correctness.

## CLI coverage

Every discovered CLI command receives an independent process-level `--help` parse test. Semantic behavior is exercised through the toolkit's native regression tests and the supplemental API contract tests.

## No-skip rule

The JUnit report must contain zero skipped tests. Conditional pytest skips are treated as a test-suite failure. External dependencies are represented outside pytest as explicit `BLOCKED` live tests.

## Thresholds

Defaults:

- statement coverage: at least 70%;
- branch coverage: at least 50%;
- function-body execution: 100%.

Thresholds are configurable, but a release should not lower them to accommodate regressions. Increase them as coverage depth grows.

## Structural contracts

The suite also checks source hashes, schemas, Java syntax, skill frontmatter, Python compilation, package construction, and clean installation. These protect artifacts that ordinary unit coverage cannot measure.
