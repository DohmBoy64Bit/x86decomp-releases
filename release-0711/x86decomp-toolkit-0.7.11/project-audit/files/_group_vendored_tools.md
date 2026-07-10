# Grouped audit — vendored test tools (.x86decomp-test-tools/) (Bvendored, component-level per owner scope)

3 component-level inventory rows (V-prefixed). These are third-party binaries/installs placed by the x86decomp-test harness (install_root in x86decomp-test.json), NOT part of the product package. Owner-approved: component-level review, no per-file rows for the ~5,227 upstream files.

## .x86decomp-test-tools/ghidra/current/ghidra_12.1.2_PUBLIC (extracted install, ~5,200 files)
- Identity: NSA Ghidra 12.1.2 PUBLIC (20260605). Third-party (Apache-2.0 + bundled component licenses in its licenses/ dir).
- Purpose: local static-analysis backend for the harness (ghidra.py analyzeHeadless).
- Belongs in repo? NO — it is local test tooling, correctly gitignored as test-suite/.x86decomp-test-tools/ (though it sits at ROOT here, REPO-004 path mismatch). 1.4 GB dominates the tree (REPO-003).
- Security/licensing/reproducibility: upstream signed release; not reviewable line-by-line (external tool) — full source review NOT APPLICABLE (vendored third-party). Its own bundled licenses cover redistribution; shipping it inside a product release tree is a hygiene/licensing-surface concern (REPO-003) but the files themselves are unmodified upstream (not verified byte-for-byte here; assumed from installer provenance — Probable).
- Reproducibility: acquired via harness download/extract; the ghidra .zip is retained alongside (see below).

## .x86decomp-test-tools/ghidra/ghidra_12.1.2_PUBLIC_20260605.zip (distribution archive)
- Identity/purpose: the source archive for the above install; kept post-extraction.
- Belongs in repo? NO — redundant with the extracted install; ~300MB+ duplication. REPO-003. Deleting it was noted as an easy space win.

## .x86decomp-test-tools/objdiff/current (objdiff.exe + wrapper)
- Identity: objdiff (third-party object-diff tool, github.com/encounter/objdiff). Windows binary.
- Purpose: objdiff_adapter.py integration.
- Belongs in repo? NO — local tool; gitignored path. Binary — not reviewable; full source review NOT APPLICABLE.

## Verdict
All 3 components: Audited — vendored dependency. Findings: REPO-003 (1.4GB of local tooling contaminates a 7.8MB source release), REPO-004 (located at root, outside the gitignored test-suite/ path). No evidence the binaries are malicious (upstream-provenance tools), but their presence in a distributed release tree is a hygiene, size, and licensing-surface problem. Recommend excluding from any distributed artifact.
