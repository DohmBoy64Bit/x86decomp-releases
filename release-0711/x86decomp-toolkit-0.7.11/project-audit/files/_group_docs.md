# Grouped audit — docs/ (18 files) (Bdocs)

Depth: all read/skimmed in full; COMMAND_REFERENCE mechanically diffed against the live parser (R-019: EXACT MATCH, 239/239 routes, 0 drift). Hashes in FILE_INVENTORY.csv.

- architecture.md (23) + ARCHITECTURE_MAP.md (82) + ARCHITECTURE_MAP_ASCII.txt (109): accurate 4-capability-package model; 59/239 and plan-only contract documented; matches code. Audited — complete.
- COMMAND_REFERENCE_0.7.11.json (1452) + .md (11): **exact match to live canonical_routes (R-019)** — 59 groups/239 routes/166 root commands, no drift. This is the one release-inventory artifact that IS in sync (regenerated in the fix pass), unlike MANIFEST.sha256. Audited — complete.
- build-and-verification.md (36): documents make verify/hashes flow — accurate but points at the verify-hashes gate that currently fails (REPO-001). Audited — complete.
- contracts.md (102): document/state contracts; consistent with schemas/. Audited — complete.
- evidence-and-claims.md (58): three-independent-source gate — matches evidence.py. Audited — complete.
- ghidra-integration.md (48): matches ghidra.py + ghidra_scripts + verify-ghidra.sh. Audited — complete.
- guardrails.md (57): safety/consent posture — matches SECURITY.md + code (worker isolation, allow_host_execution). Audited — complete.
- local-llm.md (238): loopback-only, env-var secrets, byte-identity gate — matches local_llm/ implementation (profiles loopback check, transport same-origin). Audited — complete.
- operations-and-recovery.md (106): pipeline resumability/backup/restore — matches orchestrator.py + project_state.py. Audited — complete.
- project-memory.md (42): memory protocol — matches memory.py hash chain. Audited — complete.
- source-basis.md (20): explicit upstream boundaries + 'does not vendor Ghidra/Capstone/...'. NOTE tension with REPO-003: the shipped tree DOES contain a vendored Ghidra install under .x86decomp-test-tools/ (installed by the harness, not part of the package proper) — doc refers to the PACKAGE not vendoring, which is technically accurate (the tools tree is local test state, gitignored). Documented for CROSS_FILE. Audited — complete.
- supported-scope.md (5): honest scope limits (no source-text recovery claim). Audited — complete.
- target-packs-and-templates.md (101): matches target_pack.py/project_template.py. Audited — complete.
- test-bundle.md (132): matches test_bundle.py safe-extraction design. Audited — complete.
- roadmap.md (3): brief forward-looking note; no MkDocs (DOC-002). Audited — complete.

Overall docs quality: HIGH, accurate, honest about limits, and — for COMMAND_REFERENCE — mechanically in sync with code. No new findings; DOC-002 (no MkDocs site despite governance requirement) stands. Docs do NOT exhibit the boilerplate problem that the docstrings do.
