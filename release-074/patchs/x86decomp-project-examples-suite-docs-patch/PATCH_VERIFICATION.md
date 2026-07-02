# Project Examples Suite patch verification

- Patch: `x86decomp-project-examples-suite-v2`
- Target: x86decomp `0.7.4`
- Status: **PASS**
- Detailed examples: **11**
- Installed HTML pages: **13**

## Verification results

- Source identity and anchors: **PASS** — 50 files, 95 exact anchors, detected release 0.7.4.
- CLI command surface: **PASS** — 163 command lines across 80 commands.
- Content and caveat audit: **PASS** — 11 detailed pages, inline graphs, bounded-claim sections, no failures.
- Runtime implementation probes: **PASS**.
- Targeted source tests: **PASS** — 17 passed, 3 skipped, 0 failed, 0 errors.
- Installer/idempotency: **PASS** — both application runs passed; 13 unique search entries and 95 installed source-audit rows.

## Important source-backed corrections

- v0.7.4 has two DecompilationMode values: matching and functional. preferred_mode=both composes both lanes; hybrid is not a third mode enum.
- hybrid-generate takes project and output positional arguments; its generated Makefile builds the assembly fallback path, not an automatic accepted-source switch.
- patch-image overwrites exactly the candidate file length. It checks PE bounds and optional hashes but does not independently discover or enforce the intended function boundary.
- The v0.7.4 release gate reads a legacy modes object, while public workflow commands serialize selected_modes, matching_status, and functional_status. --require-workflows can require workflow existence but does not enforce those public schema-v2 status minima.
- Validators write reports but do not automatically promote workflow status; workflow-update is a separate operator action.
- The strict evidence gate checks record count, independent groups, evidence kinds, contradictions, and file hashes; it does not semantically interpret referenced report contents.
- Concrete, symbolic, integration, normalization, convergence, and release results remain bounded by their explicit contracts and do not establish universal equivalence or original-source recovery.

## Truth boundary

This verification covers the documentation patch, exact v0.7.4 source anchors, parser compatibility, selected implementation tests/probes, and static-site installation. It is not a rerun of the complete 0.7.4 release suite and does not make target-specific assumptions or outcomes true.
