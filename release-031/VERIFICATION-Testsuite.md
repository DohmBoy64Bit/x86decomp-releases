# Verification record — x86decomp comprehensive test suite 0.3.1

## Test target

This record covers the clean suite source integrated at `test-suite/` in
x86decomp-toolkit 0.3.1. Generated results, adapter downloads, virtual environments,
coverage products, and machine-specific configuration are not part of the source
release.

## Harness tests

The external test directory and the package-carried self-test copy were both run:

```text
tests/:                                      17 passed
src/x86decomp_testkit/self_tests/:           17 passed
0 failed
0 skipped
```

These tests cover configuration round trips, strict exit behavior, adapter detection,
no-prompt behavior for installed adapters, custom-path prompting for missing adapters,
custom Python resolution, non-interactive unresolved behavior, safe archive extraction,
installer construction, inventory drift, function coverage correlation, JUnit parsing,
process logging, reports, and CLI behavior.

## Toolkit supplemental regression

The package-carried toolkit supplemental tests completed with:

```text
src/x86decomp_testkit/toolkit_tests/:        19 passed
0 failed
0 skipped
```

The complete repository regression run, including native toolkit tests and all nested
suite tests, completed with:

```text
109 passed
0 failed
0 skipped
```

## Pinned surface audit

Dynamic discovery exactly matched the 0.3.1 feature catalog:

```text
45 Python modules
394 defined functions and methods
72 CLI commands
38 JSON Schemas
3 Ghidra Java scripts
catalog audit: passed
```

Any uncataloged or stale item remains a release failure.

## Adapter interpretation

A live adapter test is executed only when its installation is resolved. Detection is
performed before prompting. A custom-path question is shown only for a missing adapter.
Unresolved integrations are emitted as `BLOCKED`; they are not omitted or converted to
passes. Strict mode returns exit code `2` while any required adapter remains blocked.

The earlier Windows integration run described in `CHANGELOG.md` verified the 0.3.1
Ghidra and hybrid-build fixes in that environment. This source-normalization pass did
not manufacture equivalent live results for tools absent from the current host.

## Packaging

The suite builds independently as:

```text
x86decomp_test_suite-0.3.1-py3-none-any.whl
x86decomp_test_suite-0.3.1.tar.gz
```

Its source distribution and wheel retain the feature catalog, schemas, self-tests,
documentation, and CLI entry point. Transient run products are excluded.

## Important interpretation

Executing every defined function body at least once is a no-omission surface contract,
not proof for every input or branch. New behavior still requires targeted assertions,
updated catalog entries, live adapter probes where applicable, and maintained coverage
thresholds.
