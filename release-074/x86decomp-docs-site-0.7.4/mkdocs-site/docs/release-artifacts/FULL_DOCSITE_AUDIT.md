# Full documentation-site audit — x86decomp 0.7.4

**Status:** PASS

## Baselines

- Documentation archive: `x86decomp-docs-site-0.7.4(1).zip` — `ccf250ecb431795bb5cc4a0f37560bc362db3dcb91bff222e4c42c869bfb9145`
- Release archive: `x86decomp-toolkit-0.7.4-release-bundle(3).zip` — `7fae1658b0eccb980d54a3c80a5f91a6cf09f8eb4e2eb4ebcae3bd477f6d36e8`
- Only these two newly supplied archives were used as the audit baseline.

## Coverage

- **checks:** 28
- **passed checks:** 28
- **failed checks:** 0
- **html pages:** 354
- **command sections:** 285
- **parsed examples:** 622
- **modules:** 137
- **functions and methods:** 983
- **tests:** 215
- **schemas:** 93
- **adapters:** 31
- **source manifest files:** 411
- **project example source anchors:** 95
- **search entries:** 2183

## Checks

- **PASS** — current release archive identity
- **PASS** — current docs archive readable
- **PASS** — release status and version
- **PASS** — release SHA256SUMS (entries=2703)
- **PASS** — root source manifest (entries=411)
- **PASS** — test-suite source manifest (entries=60)
- **PASS** — source/parser inventory contract
- **PASS** — source inventory matches sealed release evidence
- **PASS** — live HTML page count
- **PASS** — no embedded backup trees
- **PASS** — local links, fragments, scripts, and styles
- **PASS** — no external runtime assets
- **PASS** — consistent global navigation (pages=354)
- **PASS** — no placeholder or unfinished-content markers
- **PASS** — command reference exactness (sections=285)
- **PASS** — all documented executable examples parse (examples=622)
- **PASS** — module and function reference exactness (modules=137, functions_and_methods=983)
- **PASS** — test reference exactness (tests=215)
- **PASS** — schema reference and meta-schema validation (schemas=93)
- **PASS** — adapter catalog exactness (adapters=31)
- **PASS** — complete manifest-backed source coverage (files=411)
- **PASS** — Ghidra script coverage (scripts=3)
- **PASS** — project examples exact-source ledger (pages=11, anchors=95)
- **PASS** — search index completeness (entries=2183)
- **PASS** — coverage manifest exactness
- **PASS** — JavaScript syntax (files=2)
- **PASS** — rendered release evidence matches sealed report
- **PASS** — changelog source provenance

## Sealed release evidence

- Exact gate: 215/215 passed, with 0 failures, 0 errors, and 0 skips.
- Comprehensive harness: 189 PASS, 0 FAIL, 0 ERROR, 7 BLOCKED.
- Coverage: 79.03% statements and 51.70% branches.
- These are authenticated values from `release-verification.json`, not a newly claimed full-suite run by this documentation audit.

## Truth boundary

The audit proves structural completeness and exact correspondence for enumerated parser, AST, schema, adapter, manifest, source-ledger, link, search, and placeholder contracts. It does not prove target-specific outcomes or all-input semantic equivalence, and it does not reinterpret sealed release test evidence as a newly executed complete test run.
