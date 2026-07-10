# Audit Plan — x86decomp-toolkit 0.7.11

Status: ACTIVE. Reread this file, FILE_INVENTORY.csv, AUDIT_LEDGER.csv, FINDINGS_REGISTER.md, ARCHITECTURE_NOTES.md, and RUN_LOG.md at the start of every session/batch.

## Scope
- 100% accounting of the working tree at `x86decomp-toolkit-0.7.11/` (694 first-party files + 3 vendored component rows; see FILE_INVENTORY.csv).
- Owner decisions (2026-07-10): vendored `.x86decomp-test-tools/` gets component-level review; per-file reports for all code/config/docs/tests; grouped batch reports for fixtures/generated/data files; project purpose derived from repo docs.
- Excluded: nothing. `.git/` does not exist (not a git repo).

## Repository-specific risks to watch
1. Release integrity: MANIFEST.sha256 already fails for 68/449 files (REPO-001). Distinguish "post-manifest fixes" from tampering using SECOND_AUDIT_FIX_REPORT_0.7.11.md as corroboration.
2. Untrusted-input parsing: PE/COFF parsers (pe.py, pe32.py, coff_archive.py) process adversarial binaries — bounds checking, integer overflow, resource limits.
3. Subprocess/tool orchestration: Ghidra, objdiff, local LLM transport, MCP server — command injection, path handling, network exposure (service.py, fastapi).
4. Self-referential audit artifacts: repo ships its own audit/verification reports; verify their claims independently, do not inherit them.
5. Python version skew: package requires 3.11; sandbox has 3.10 — attribute runtime failures correctly.
6. Claims vs reality: README claims 59 groups / 239 routes — count mechanically in Phase 6.

## Review order (dependency-ordered batches)
- B01 Root metadata & manifests: pyproject.toml, setup.cfg, MANIFEST.in, Makefile, .gitignore, .github/, LICENSE, MANIFEST.sha256, RELEASE_VERIFICATION.*, ALL_FILE_MANIFEST_0.7.11.json
- B02 Root docs: README.md, CHANGELOG.md, AGENTS.md, PROJECT_MEMORY.md, SECURITY.md, VERIFICATION.md, FEATURE_PARITY.md, prior audit reports, skills/x86decomp/SKILL.md
- B03 Entry points & CLI core: src/x86decomp/cli.py, cli_utils.py, __init__.py, __main__.py (if present), commands registry
- B04 Core models & shared utils: models.py, util.py, contracts.py, canonical.py, content_store.py, project_state.py
- B05 Parsing/analysis: pe.py, pe32.py, coff_archive.py, msvc_metadata.py, image_match.py, disassembly/symbolic/dynamic/angr backends
- B06 Subsystems: governance/, reconstruction/, assembly/, native/, local_llm/, mcp.py, service.py, orchestrator.py, tools.py, dynamic.py, symbolic.py
- B07 Output/reporting components
- B08 Config & schemas: schemas/ (97 JSON schemas — full read, grouped reporting where repetitive)
- B09 Tests: tests/ (102), test-suite/ (115)
- B10 Build/automation: scripts/ (12), ghidra_scripts/ (3), .github/workflows
- B11 Examples: examples/ (26)
- B12 Fixtures/data/generated: corpus/ (24), dist/, .pytest_cache/, root JSON artifacts — grouped reports
- B13 Vendored components: 3 component rows
- B14 Phases 6–9 system-level audits; B15 Phase 10 safe execution; B16 Phases 11–12 fact-check + coverage reconciliation + final report

## Methodology
- Read every first-party text file completely (Read tool / cat). Per-file report per template sections A–M under project-audit/files/, filename = path with `/`→`__`, plus `.md`.
- Grouped reports: project-audit/files/_group_<name>.md with one entry per member file (identity + purpose + belongs-in-repo + concerns); each member still gets its own inventory/ledger row.
- Findings get IDs (COR/SEC/DOC/CLI/ARC/PERF/TEST/DUP/MAINT/UX/RE/REPO-###) in FINDINGS_REGISTER.md immediately upon discovery.
- Triple verification for important findings: direct evidence + corroboration (call sites/tests/docs) + consistency check. Label confidence: Verified / Strongly supported / Probable / Possible / Unverified / Blocked from verification.
- Ledger updated after every file; batch reconciliation against inventory at each batch end.

## Commands: safe vs prohibited
Safe (allowed): read-only file ops; sha256sum; python3 -m compileall to temp dirs (writes .pyc — use PYTHONDONTWRITEBYTECODE=1 or pycache_prefix outside repo); pytest with cache disabled or redirected outside repo (-p no:cacheprovider); `x86decomp --help`-style commands with cwd/outputs outside repo; pyflakes (no fix mode); scripts/source_hashes.py verify (read-only per Makefile semantics — confirm before running); scripts/validate-contracts.py (confirm read-only first).
Prohibited: any formatter/fixer (ruff --fix etc.); pip install into project; python -m build inside repo (writes dist/); make clean/package/install/editable; deleting/renaming anything; executing objdiff.exe or Ghidra binaries; commands contacting the network; running the fastapi service against a network port; executing corpus binaries.
Caution rule: before any script execution, read its source to confirm it cannot write into the project tree; if it can, run with cwd and outputs redirected, or skip and record Blocked.

## Completion criteria
Per the audit contract: every inventory row has a final status; per-file or grouped report for every applicable file; command matrix complete; findings triple-verified or labeled; coverage reconciliation with hash recomputation clean or explained; confirmation that no pre-existing project file was modified (verify by re-running full hash pass and comparing to FILE_INVENTORY.csv).
