# Per-file audit — README.md

## A. Identity
- Path: `README.md`
- SHA-256: `204dd469f382126691730b675d447b6420bb7e714fdb1216b193403b90d61a9a`
- Size: 4112 bytes | Type: text | Classification: documentation
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Top-level product doc: purpose statement, unified `x86decomp` interface (claims 59 groups / 239 routes), install (wheel + extras), first-project walkthrough, local-LLM proposal loop with safety posture (loopback-only endpoints, env-var secrets, byte-identity gates), assembly-output policy, verification instructions (`make verify`, `make hashes`), harness usage, operating principles, doc pointers.

## C. Correctness (claims vs tree)
- 59/239 claim: repeated in 5+ artifacts; mechanical count deferred to Phase 6 (COMMAND_SYSTEM_AUDIT).
- `make verify` instruction currently leads to a hash-verification failure on this exact tree (REPO-001) — the doc is correct but the tree isn't; user-visible contradiction.
- Harness example writes ./x86decomp-test.json, ./.x86decomp-test-tools, ./test-results into the source tree — invocation pattern that produced the contamination (REPO-004). The doc actively encourages polluting the release tree without matching ignore rules.
- References docs/architecture.md, docs/supported-scope.md, docs/build-and-verification.md, docs/local-llm.md — existence verified in inventory (docs/ has 18 files); content cross-check in B02/Phase 9.
- Install section references wheel filename matching dist/ contents. Consistent.

## D. Documentation quality
Clear, specific, honest about boundaries (untrusted LLM output, explicit authorization for execution). Good real-world examples. No quick uninstall/upgrade guidance; minor.

## L. Findings
- Contributes to REPO-004 (invocation pattern) and REPO-001 (verify instruction fails on shipped tree).

## M. Verdict
Doc quality: high. Priority: low (fix examples to use out-of-tree paths or add ignore rules). Final status: Audited — complete.