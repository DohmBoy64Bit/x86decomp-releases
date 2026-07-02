---
title: Verification
description: Exact release and documentation verification results
original_path: verification.html
---

Section: Release and documentation evidence

# Verification

The release evidence and the documentation audit are separate contracts. This page reports both without merging their claims.

## Sealed release evidence

| Value | Meaning |
| --- | --- |
| 215/215 | exact tests passed |
| 843/843 | toolkit bodies executed |
| 189 | harness passes |
| 7 | explicitly blocked adapters |

- Exact gate: 0 failures, 0 errors, 0 skipped across 79 partitions.
- Comprehensive harness: 189 PASS, 0 FAIL, 0 ERROR, 7 BLOCKED.
- Statement coverage: 79.03% against a 70% floor.
- Branch coverage: 51.70% against a 50% floor.
- Root manifest: 411/411 valid.
- Test-suite manifest: 60/60 valid.

### Blocked external integrations in the sealed environment

`container-runtime`, `dynamorio`, `ghidra`, `llvm-readobj`, `msvc`, `objdiff`, `pip-audit`.

## Documentation audit

The post-patch audit is published as [`FULL_DOCSITE_AUDIT.md`](release-artifacts/FULL_DOCSITE_AUDIT.md) and [`FULL_DOCSITE_AUDIT.json`](release-artifacts/FULL_DOCSITE_AUDIT.json). Complete source-file coverage is available on [Source coverage](source-coverage.md).

## Common verification commands

```
make verify-hashes
make verify
make test-suite
x86decomp-test run --config ./x86decomp-test.json --verbose
```
