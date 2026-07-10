# Per-file audit — MANIFEST.in

## A. Identity
- Path: `MANIFEST.in`
- SHA-256: `69db866c1421555409f490a901506cf31957aa7944eb920565f0602653783f22`
- Size: 835 bytes | Type: text | Classification: configuration
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
sdist content control: includes MANIFEST.sha256 + root docs, recursive-includes .github/docs/corpus/examples/ghidra_scripts/schemas/scripts/skills/tests, `graft test-suite`, prunes caches/build/dist/test-results/test-tools.

## C. Correctness
- Prunes cover `test-suite/.x86decomp-test-tools` but NOT root-level `.x86decomp-test-tools/` — same blind spot as .gitignore. If an sdist were built from this contaminated tree, `graft test-suite` is safe but root test-tools is only excluded because no include rule matches it (sdist includes are additive; a root dir not named in any include is omitted). Effective but fragile — depends on nobody adding a broad include. Informational, related to REPO-003.
- `recursive-include examples *.json *.c *.py *.bin` — .bin binary fixtures intentionally packaged.
- Does not include x86decomp-test.json (good — that file should not ship; yet it exists in the tree, REPO-002).

## L. Findings
- Contributes context to REPO-002/REPO-003 (no new ID).

## M. Verdict
Quality: good. Priority: low. Final status: Audited — complete.