# Verification record — x86decomp-toolkit 0.5.0 integrated release

## Verified source baseline

The complete x86decomp-toolkit 0.4.0 source tree was supplied and upgraded in place through the staging-first v0.5 installer. The integrated release preserves the exact 0.4 feature catalog as `feature_catalog.v040.baseline.json` and enforces set inclusion against the current catalog.

Verified retained surface:

```text
0.4.0 baseline modules retained:            60 / 60
0.4.0 function/method symbols retained:    514 / 514
0.4.0 CLI commands retained:               106 / 106
0.4.0 root JSON Schemas retained:           52 / 52
0.4.0 Ghidra scripts retained:               3 / 3
0.4.0 adapter contracts retained:           31 / 31
matching/functional workflow modes:          2 / 2
```

The integrated top-level v0.5 surface is 61 modules, 515 function/method symbols, and 107 legacy CLI commands. The additive command is the active `x86decomp v050 ...` compatibility bridge. The independent `x86decomp-v050` control plane contains 67 leaf commands, 18 namespaced modules, 142 defined functions/methods, and 12 namespaced schemas.

## Repository and contract gates

Executed on 2026-06-29 with Python 3.13.5:

```text
complete monolithic repository collection: 188 passed, 0 failed, 0 skipped
standalone verifier gate:                    26 passed, 0 failed, 0 skipped
recursive contract/schema/skill validation: passed
Python compileall:                           passed
root and nested SHA-256 manifests:           passed
```

The 188-test collection comprises 125 root toolkit tests, 26 standalone verifier tests, 17 packaged harness self-tests, and 20 supplemental toolkit tests. The repository `make verify` path executes the complete collection and then repeats the standalone verifier as an independent gate.

## Comprehensive no-silent-skip harness

Run ID `run-20260629T225453918Z-36a0d510` completed with:

```text
PASS:       156
FAIL:         0
ERROR:        0
BLOCKED:      7
exit code:    0 (non-strict mode)
```

The seven blocked integrations were container runtime, DynamoRIO, Ghidra, llvm-readobj, historical MSVC, objdiff, and pip-audit. They were unavailable on this host and remain explicit `BLOCKED` records; none was skipped, omitted, or converted into a pass. Strict mode would return exit code 2 while those integrations remain unresolved.

Coverage and no-omission results:

```text
515 / 515 cataloged top-level function/method bodies executed
107 / 107 legacy CLI commands parser-tested
145 coverage-run pytest cases, zero skipped
statement coverage: 77.90021156558534%
branch coverage:    52.57318224740321%
```

Both inherited floors—70% statements and 50% branches—passed without reduction.

## Packaging and installed behavior

The comprehensive harness built and clean-installed:

```text
x86decomp_toolkit-0.5.0-py3-none-any.whl
x86decomp_toolkit-0.5.0.tar.gz
```

Installed package checks cover the retained `x86decomp` entry point, the active `x86decomp v050` bridge, the standalone `x86decomp-v050` entry point, the `x86decomp-apply-v050` transactional installer, the separately packaged `x86decomp-test` harness, embedded deterministic upgrade overlay, package data, versions, and command help. The installer now runs compileall, recursive contract validation, the complete monolithic pytest collection, and the standalone verifier against a staged copy before committing.

The final toolkit wheel was installed into an isolated environment and its embedded overlay was applied to a fresh untouched 0.4.0 tree using the declared `full`, `pe`, and `dev` verification dependencies. That installed-wheel transaction passed 188 staged repository tests and 26 staged standalone tests before commit. A bare environment without those verification dependencies is rejected rather than silently skipping the safety gates.

The worker launcher supersedes the thread-unsafe POSIX `preexec_fn` production path with an exec-based resource-limit wrapper while retaining and directly testing the legacy `_preexec` compatibility symbol. The final commit boundary is rollback-tested.

## Truth boundary

These results establish the declared release and regression contracts. They do not claim original-source recovery, arbitrary-program equivalence, complete compiler identification, safe ordinary-host execution of unknown targets, or that adapter consensus establishes truth.
