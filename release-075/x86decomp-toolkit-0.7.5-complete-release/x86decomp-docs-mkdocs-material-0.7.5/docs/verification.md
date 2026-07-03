---
title: Verification
description: Exact x86decomp 0.7.5 release and documentation verification results.
---

# Verification

The release-test surface, comprehensive harness, package checks, and documentation audit are separate contracts. This page reports each without broadening its claim.

## Distinct release tests

| Surface | Result |
| --- | ---: |
| Toolkit tests | **180/180 passed** |
| Standalone test-suite tests | **22/22 passed** |
| Bundled public-contract tests | **21/21 passed** |
| Total distinct tests | **223/223 passed** |
| Dedicated local-LLM tests | **8/8 passed** |

These runs had zero failures, errors, or skips.

## Comprehensive adapter-aware harness

| Status | Count |
| --- | ---: |
| PASS | **191** |
| BLOCKED | **11** |
| FAIL | **0** |
| ERROR | **0** |

- Function/method bodies executed: **879/879**.
- Statement coverage: **78.89%** against a 70% floor.
- Branch coverage: **51.73%** against a 50% floor.
- Installed adapters exercised or detected: **25**.
- Explicitly blocked adapters: **11**.
- Harness exit code: **0**.

Blocked adapters in this environment:

`container-runtime, dynamorio, ghidra, llama-server, llvm-readobj, lm-studio, localai, msvc, objdiff, ollama, vllm`

A blocked adapter is not a pass or a skip. It means the external runtime or proprietary tool was unavailable under the non-installing, network-disabled verification policy.

## Source, schema, package, and documentation gates

- Root source manifest: **427/427** files verified.
- Standalone test-suite manifest: **60/60** files verified.
- JSON Schemas: **97/97** passed meta-schema validation.
- Toolkit and test-suite wheels and source distributions built successfully.
- Fresh wheel installation passed `pip check` and installed-entry-point smoke tests.
- Strict Material for MkDocs build passed.
- Documentation source pages: **366**.
- Material search coverage: **366/366** pages.
- Built-site local references checked: **20779**, with zero failures.

## Local-model truth boundary

The local-model subsystem was tested with bounded mock HTTP servers and a real Clang-to-COFF exact-byte loop. The release does **not** claim that a particular live LM Studio, Ollama, llama.cpp, vLLM, or LocalAI model will match arbitrary functions. In this verification environment, the live local inference runtimes listed above were unavailable and are therefore `BLOCKED`.

A local model can only propose C. Acceptance requires deterministic compilation, COFF symbol extraction, complete relocation resolution, equal length, and exact byte identity with the declared contiguous target range.

## Machine-readable records

- [`HARNESS_SUMMARY.json`](release-artifacts/HARNESS_SUMMARY.json)
- [`FULL_DOCSITE_AUDIT.json`](release-artifacts/FULL_DOCSITE_AUDIT.json)
- [`DOCSITE_SYNC_AUDIT.json`](release-artifacts/DOCSITE_SYNC_AUDIT.json)
- [`PROJECT_EXAMPLES_SOURCE_AUDIT.json`](release-artifacts/PROJECT_EXAMPLES_SOURCE_AUDIT.json)
