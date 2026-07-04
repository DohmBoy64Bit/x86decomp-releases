# x86decomp comprehensive test suite 0.7.5

This separately packaged harness verifies the complete current x86decomp-toolkit surface without silent skips.

## Interface

```bash
x86decomp-test --help
x86decomp-test init-config --toolkit-root . --output-root ./test-results --install-root ./.x86decomp-test-tools --config ./x86decomp-test.json
x86decomp-test run --config ./x86decomp-test.json --verbose
```

The run command creates the configured output directory and a unique run subdirectory. Reports include adapter status, process logs, JUnit, coverage, inventory drift, package checks, and unified PASS, FAIL, ERROR, or BLOCKED results.

## Current pinned surface

- 113 Python modules
- 879 function and method bodies
- 141 root commands
- 34 canonical groups
- 181 canonical routes
- 97 schemas
- 3 Ghidra scripts
- 36 adapter contracts
- one toolkit executable and one test-suite executable

The catalog is recursive. Capability subpackages and nested schema directories are included.

## Result policy

- PASS: the exact check succeeded.
- FAIL: the asserted product behavior did not satisfy its contract.
- ERROR: the verifier could not complete because of an internal or environmental error.
- BLOCKED: an explicitly declared external dependency was unavailable.

A skipped test is a release failure.
