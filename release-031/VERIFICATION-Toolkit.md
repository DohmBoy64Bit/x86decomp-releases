# Verification record — x86decomp-toolkit 0.3.1

## Release scope

This record covers the normalized 0.3.1 source tree containing the toolkit and its
separately packaged comprehensive harness under `test-suite/`.

The 0.3.1 update preserves the 0.3.0 feature surface while adding Windows adapter and
hybrid-build fixes, stable test-suite integration, version alignment, release hygiene,
and a maintained Mermaid architecture map.

## Source hygiene

The release tree was checked for and cleared of:

- Python bytecode and `__pycache__` directories;
- `.pytest_cache`, coverage databases, HTML/XML/JSON coverage output, and JUnit output;
- editable-install `.egg-info` metadata;
- `build/`, `dist/`, and smoke-test virtual environments;
- generated `test-results/` trees;
- downloaded adapter binaries and installer output;
- machine-specific test configuration and absolute user paths.

The source tree contains no bundled proprietary compiler or external adapter binary.

## Contract validation

Executed from the repository root:

```bash
python scripts/validate-contracts.py
```

Result:

```text
contract, example, Java syntax, and skill frontmatter validation passed
```

This validates JSON Schemas and examples, parses the Ghidra Java scripts, and checks the
3.1.0 skill frontmatter and 0.3.1 release contract.

## Combined regression suite

Executed with bytecode and pytest-cache generation disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=src \
python -m pytest -q -p no:cacheprovider
```

Result:

```text
109 passed
0 failed
0 skipped
```

The environment included the declared optional Python validation adapters used directly
by the supplemental tests: Capstone, Unicorn, Z3, and angr.

## Comprehensive test-suite validation

The independently packaged harness was also exercised by concern:

```text
test-suite/tests:                                      17 passed
test-suite/src/x86decomp_testkit/self_tests:           17 passed
test-suite/src/x86decomp_testkit/toolkit_tests:        19 passed
```

Its pinned 0.3.1 inventory audit reported:

```text
45 Python modules
394 functions and methods
72 CLI commands
38 JSON Schemas
3 Ghidra Java scripts
catalog audit: passed
```

## Source manifests

The nested `test-suite/MANIFEST.sha256` seals the independent harness source. The root
`MANIFEST.sha256` seals the complete repository, including the nested suite manifest.
Transient and machine-specific paths are excluded by contract.

## Packaging checks

The final release process builds and clean-installs both Python projects:

```text
x86decomp_toolkit-0.3.1-py3-none-any.whl
x86decomp_toolkit-0.3.1.tar.gz
x86decomp_test_suite-0.3.1-py3-none-any.whl
x86decomp_test_suite-0.3.1.tar.gz
```

The toolkit source distribution includes the clean `test-suite/` source tree, while the
toolkit wheel remains runtime-only. The test suite retains its own package metadata and
entry point.

## Environment-dependent integrations

The following adapters have implementation and detection contracts but require their
actual external installations for a live release-gate run:

- Ghidra headless analysis;
- DynamoRIO tracing;
- an operator-selected objdiff CLI build;
- user-owned historical MSVC toolchains;
- platform-specific compiler/linker combinations not installed in the current host.

Unavailable integrations must be reported as `BLOCKED` by the comprehensive harness.
They must never be silently skipped or counted as passing.

## Claims deliberately not made

This release does not claim:

- recovery of source information erased by compilation;
- correctness of every inferred name, type, class, or source boundary;
- complete reconstruction of every historical linker decision;
- generic whole-image identity for arbitrary targets;
- semantic equivalence outside a validator's declared finite scope;
- safe native execution of unknown binaries;
- that a three-source governance gate guarantees truth.

Version 0.3.1 is a regression-tested, production-oriented bounded framework for
authorized, target-specific decompilation work. Unsupported and unverified conditions
remain explicit states rather than success shims.
