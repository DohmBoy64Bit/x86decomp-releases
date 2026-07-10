# Findings Register — x86decomp-toolkit 0.7.11

Severity: Critical / High / Medium / Low / Informational.
Confidence: Verified / Strongly supported / Probable / Possible / Unverified / Blocked from verification.
Status values: Open / Corroborated / Merged / Downgraded / Closed-verified.

---

## REPO-001 — Shipped integrity manifest does not match shipped files
- Category: Repository hygiene / release integrity
- Severity: High
- Confidence: Verified (that hashes mismatch); cause attribution: Probable (post-manifest modification)
- Status: Open — cause corroboration pending (B02: SECOND_AUDIT_FIX_REPORT_0.7.11.md review)
- Affected files: MANIFEST.sha256 vs 68 files (full list: project-audit/manifest_failures.txt) — 34 under src/x86decomp, 17 under tests/, 15 under test-suite/, test-suite/docs/TEST_PLAN.md, x86decomp-test.json
- Affected symbols/commands: release verification workflow (`make verify-hashes`, scripts/source_hashes.py)
- Exact evidence: RUN_LOG R-004 — `sha256sum -c MANIFEST.sha256` → 381 OK / 68 FAILED at audit start, before any audit activity (audit writes only under project-audit/).
- Corroborating evidence: file mtimes — bulk of tree 2026-07-06 18:44; src/ 18:48, test-suite/ 18:56, scripts/ 18:57, tests/ 19:54, x86decomp-test.json 23:32. Repo root contains SECOND_AUDIT_FIX_REPORT_0.7.11.md (post-release fix report, mtime 18:44) suggesting a fix pass occurred; whether it accounts for all 68 mismatches is unverified pending B02.
- Consistency check: RELEASE_VERIFICATION.md/json claim a verified release — contradicted by current tree state. To be re-examined in B02.
- User impact: anyone running the documented integrity check (`make verify-hashes` semantics may differ — uses scripts/source_hashes.py, to be verified) or `sha256sum -c MANIFEST.sha256` will conclude the release is corrupt or tampered with; provenance guarantees of an "evidence-governed" toolkit are undermined for exactly the files most likely to be inspected (core src + tests).
- Technical impact: MANIFEST.sha256, ALL_FILE_MANIFEST_0.7.11.json, RELEASE_VERIFICATION.* cannot be trusted as ground truth for this tree; the audit will treat computed hashes in FILE_INVENTORY.csv as the authoritative baseline instead.
- Why it matters: the project's own value proposition is evidence governance and reproducible release work; a stale first-party manifest is a direct contradiction of that claim.
- Recommended remediation: regenerate MANIFEST.sha256 (and dependent verification JSON/MD) after any post-release fix pass, or ship fixes as 0.7.12; document manifest regeneration in the release procedure.
- Verification needed: read scripts/source_hashes.py to determine which manifest it checks; read SECOND_AUDIT_FIX_REPORT_0.7.11.md and DOCSTRING_AUDIT reports to see whether the 68 files match the declared fix scope; check whether x86decomp-test.json (mtime 23:32, later than everything else) is expected to be machine-updated.
- Duplicates/related: none yet.

## REPO-001 (update 2026-07-10)
- Status: Corroborated. Cause: post-release fix pass responding to CODE_AUDIT_REPORT.md (mtime 19:27) edited 68 files without regenerating manifests. Evidence: RELEASE_VERIFICATION.json records 449/449 PASS at packaging; reports.py already contains the audit's C1 fix (direct read, escaped_summary hoisted at lines 84–90); tests/ mtime 19:54 postdates the audit report. Confidence: mismatch Verified; cause Strongly supported.

## REPO-002 — Machine-local harness config committed at release root
- Category: Repository hygiene / information exposure. Severity: Medium. Confidence: Verified. Status: Open.
- Files: x86decomp-test.json (root). Evidence: direct read — absolute C:\Users\SeanS\... paths, python_executable, install_root, and custom_environment.PATH embedding the user's complete Windows PATH (~40 entries). allow_network:true, allow_install:true.
- Impact: environment/user-topology leakage on redistribution; config is machine-specific and useless to other users. Remediation: delete from tree; add root path to .gitignore (see REPO-004).

## REPO-003 — Release tree contaminated with working-state byproducts
- Category: Repository hygiene. Severity: Medium. Confidence: Verified. Status: Open.
- Files: dist/ (wheel+sdist), .pytest_cache/ (5 files), .x86decomp-test-tools/ (5,227 files, 1.4 GB vendored Ghidra+objdiff installed by the harness), x86decomp-test.json.
- Evidence: inventory + mtimes; x86decomp-test.json install_root points at root .x86decomp-test-tools confirming harness produced it.
- Impact: a 7.8 MB source release carries 1.4 GB of tool installs and stale caches; blurs what is product vs local state. Remediation: clean before distribution; fix ignore rules.

## REPO-004 — Ignore rules do not match documented invocation paths
- Category: Repository hygiene. Severity: Medium. Confidence: Verified. Status: Open.
- Files: .gitignore, README.md, .github/workflows/ci.yml.
- Evidence: .gitignore ignores test-suite/x86decomp-test.json, test-suite/.x86decomp-test-tools/, test-suite/test-results/ — but README and CI invoke the harness from repo root with --config ./x86decomp-test.json, --install-root ./.x86decomp-test-tools, --output-root ./test-results, none of which are ignored at root.
- Impact: every user following the README pollutes their checkout/release tree exactly as observed (REPO-002/003). Remediation: add root-level patterns or change documented paths to out-of-tree locations.

## REPO-005 — Shipped dist/ artifacts diverge from shipped sources
- Category: Release integrity. Severity: High. Confidence: Strongly supported. Status: Open.
- Files: dist/x86decomp_toolkit-0.7.11-py3-none-any.whl, dist/x86decomp_toolkit-0.7.11.tar.gz vs the 68 post-release-edited source files.
- Evidence: dist mtimes (18:44) predate the fix pass (≥18:48); wheel/sdist therefore package pre-fix code including defects later fixed in-tree (e.g. reports.py py3.11 SyntaxError, per CODE_AUDIT_REPORT C1 — meaning the shipped wheel's test-suite reporting path cannot import on Python 3.11 if the wheel bundles it; sdist definitely carries the broken file). Verification needed (Phase 10/12): unzip wheel+sdist, diff reports.py and the 68 files against tree.
- Impact: pip-installing the shipped wheel yields different code than auditing the shipped source suggests. Remediation: rebuild artifacts or remove them from the tree.

## TEST-001 — Full-suite pytest completion is not demonstrated by shipped evidence
- Category: Testing. Severity: Medium. Confidence: Strongly supported (first-party admission). Status: Open.
- Evidence: RELEASE_VERIFICATION.md 'Not claimed' + SECOND_AUDIT_FIX_VERIFICATION_0.7.11.json segmented_pytest_note: monolithic/sequential runs timed out in the dev sandbox; only file-by-file runs passed. CI (ci.yml) does run monolithic pytest, but no CI logs ship with the tree (not a git repo) — Blocked from verification.
- Impact: inter-test interference or cumulative resource issues would be invisible to segmented runs; the project's own zero-skip release gate (VERIFICATION.md) is weakened. Phase 10 will attempt a partitioned run here.

## DOC-001 — Docstring coverage is presence-only; heavy boilerplate content (candidate)
- Category: Documentation. Severity: Medium. Confidence: Probable (pending my mechanical scan in B04–B06; prior report claims 577 boilerplate/48 degenerate; post-release edits may have changed counts). Status: Open — verification scheduled.
- Evidence so far: CHANGELOG claims 'professional docstrings'; DOCSTRING_AUDIT measures presence only; cli.py direct read shows template docstrings ('Support build parser processing for internal toolkit callers.') on 7 of 9 defs.

## DOC-002 — MkDocs site required by governance docs but absent
- Category: Documentation / process. Severity: Low. Confidence: Verified (absence in inventory: no mkdocs.yml, no site/). Status: Open.
- Evidence: AGENTS.md rule 12, PROJECT_MEMORY.md, SKILL.md rule 12 all require a synchronized MkDocs Material site; inventory contains no MkDocs config or build.

## DUP-001 — Multi-sentence blocks duplicated verbatim across ≥4 root docs
- Category: Duplication (documentation). Severity: Low. Confidence: Verified. Status: Open.
- Evidence: the '0.7.11 adapter-capability note' paragraph appears word-for-word in README.md, PROJECT_MEMORY.md, VERIFICATION.md, FEATURE_PARITY.md; interface-contract bullets repeated across AGENTS/PROJECT_MEMORY/FEATURE_PARITY/SKILL.

## UX-001 — SECURITY.md lacks a reporting channel
- Category: Usability / process. Severity: Low. Confidence: Verified. Status: Open.
- Evidence: Reporting section specifies report contents but no address, form, or tracker.

## MAINT-001 — Stale prior audit report shipped without disposition
- Category: Maintainability / release hygiene. Severity: Low. Confidence: Verified. Status: Open.
- Evidence: CODE_AUDIT_REPORT.md describes defects (e.g. C1) that are already fixed in-tree by the un-manifested edit pass; no addendum records what was fixed. Readers cannot tell which findings still apply.

## CLI-001 — Canonical/subsystem CLIs crash with tracebacks on the toolkit's own domain errors
- Category: CLI / correctness. Severity: High. Confidence: Verified (static); runtime demo scheduled Phase 10. Status: Open.
- Affected: src/x86decomp/cli_utils.py (CLI_ERROR_TYPES), all canonical routes dispatching into modules that raise x86decomp.errors exceptions (native/* via parse_pe: matching.py:98, pe_reconstruction.py:76/82/84/96/138, slots.py:131, runtime.py:35, hybrid_composer.py:7/26/51; local_llm ExternalToolError via reconstruction llm routes).
- Direct evidence: CLI_ERROR_TYPES=(contracts.ContractError,KeyError,OSError,TypeError,ValueError); errors.FormatError⊄ any of these; pe.py raises FormatError at :192,:207,:210,:239,:247 on malformed input; grep confirms no FormatError/X86DecompError handling in native/.
- Corroboration: assembly/relocations.py:291 catches FormatError locally (proves the family reaches subsystem flows); root cli.py catches X86DecompError, so the same malformed PE errors cleanly via `inspect-pe` but tracebacks via canonical native routes.
- Consistency: contradicts cli_utils's own stated purpose ("instead of leaking an interpreter traceback") and SECURITY.md's malformed-input posture.
- Impact: the tool's primary untrusted input (malformed binaries) produces tracebacks/exit-1 on a large command surface; scripts keying on exit 2 misclassify failures.
- Remediation: include X86DecompError in CLI_ERROR_TYPES (or normalize exceptions at subsystem boundaries).

## CLI-002 — Root CLI error contract diverges from subsystem CLIs
- Category: CLI. Severity: Medium. Confidence: Verified. Status: Open.
- Evidence: cli.py main() catches (X86DecompError,ValueError,KeyError,TypeError,JSONDecodeError) — no OSError → missing input file = traceback exit 1; error format is plain `error: msg` vs subsystems' JSON {"error","message"}. Root cli.py absent from the 68-file post-fix edit set (manifest_failures.txt) — the run_cli consolidation skipped it.
- Impact: inconsistent scripting contract across one advertised "unified" interface.

## ARC-001 — Two ContractError classes with different hierarchies
- Category: Architecture. Severity: Medium. Confidence: Verified. Status: Open.
- Evidence: errors.ContractError(X86DecompError) vs contracts.ContractError(ValueError); util.py raises the former, contracts.py the latter; cli_utils catches only the latter (the former only via ValueError-nonmembership → NOT caught). 47 modules import contracts', util's flows through 67 importers.
- Impact: `except ContractError` behavior depends on which module was imported; direct contributor to CLI-001.

## DUP-002 — Parallel foundational helper layers (util.py vs contracts.py)
- Category: Duplication / architecture. Severity: Medium. Confidence: Verified. Status: Open.
- Evidence: duplicated utc_now, sha256_bytes, sha256_file, canonical JSON, JSON read, atomic write (divergent: contracts chmods 0644, util leaves mkstemp 0600 → inconsistent artifact permissions), write_json (formatting drift), ensure_relative_path (same name, different signatures AND validation strategies: resolve-based vs string-based).
- Impact: behavior depends on import choice; consolidation is Medium complexity, medium risk (semantics must be reconciled deliberately).

## MAINT-002 — VerificationStatus exported and test-pinned but unused
- Category: Maintainability. Severity: Low. Confidence: Verified (grep: only consumer is test_public_api_contract.py). Status: Open.

## PERF-001 — Canonical registration rebuilds all subsystem parsers repeatedly at startup
- Category: Performance. Severity: Low. Confidence: Probable (needs timing at Phase 10). Status: Open.
- Evidence: canonical.py register_canonical_commands → canonical_groups()/canonical_routes()/_leaf_parsers() each rebuild the four parsers; called per group iteration.

## CLI-001 (revision 2026-07-10, post-runtime)
- Severity revised High→Medium; scope corrected. Runtime demo (R-010/R-011): via the ROOT `x86decomp` executable, FormatError IS caught (clean exit 2) because root main catches X86DecompError. The uncaught-domain-error path is real but limited to run_cli-based subsystem/canonical module mains (`python -m x86decomp.canonical` etc.). Confidence: Verified (runtime, 3.10+shims; exception routing version-independent). Recommendation unchanged: add X86DecompError family to CLI_ERROR_TYPES.

## CLI-002 (revision 2026-07-10, post-runtime — scope UPGRADED)
- Runtime-verified (R-010): root entry lacks OSError in its catch tuple, so a wrong/missing input path on ANY of the 166 root commands and 239 canonical routes yields a FileNotFoundError interpreter traceback with exit 1 instead of the structured error + exit 2. This is the primary documented user path. Severity: Medium-High (kept Medium category, priority near-term#1 with CLI-001; single-line fix aligning root main with CLI_ERROR_TYPES + X86DecompError).

## DOC-001 (revision 2026-07-10 — now Verified)
- Mechanical scan (R-006): 555/1,614 defs carry template boilerplate docstrings; 36 degenerate repeated-verb non-sentences (memory.py:44,77,102; worker.py:35; work_queue.py:49; assembly/relocations.py:269; assembly/store.py:52,74; +28 more). Confidence: Verified. Severity: Medium (documentation quality metric contradicts 'professional docstrings' release claim; presence-only audit masks it).

## CLI-003 — 78 of 106 flat root commands lack help text
- Category: CLI/UX. Severity: Medium. Confidence: Verified (R-012 parser introspection). Status: Open.
- Evidence: `x86decomp --help` shows bare names for 78 flat commands (abi-check, angr-validate, artifact-import, claim-*, coff-*, db-*, compile, ...). Canonical groups DO have help. Impact: discoverability of the primary interface; new-user experience. Remediation: add help= to every add_parser call (docs/COMMAND_REFERENCE exists and could seed them).

## Surface-claims verification (positive result, no finding)
- 59 groups / 239 routes / 166 root commands: all three shipped claims mechanically Verified at runtime (R-012).

## DUP-003 — Bounded-reader primitives reimplemented in pdb.py and msvc_metadata.py
- Category: Duplication. Severity: Low. Confidence: Verified. Status: Open.
- Evidence: BinaryReader (binary_reader.py) is the CR-0710-007 consolidation for PE/COFF, but pdb.py defines its own _require/_u16/_u32 and msvc_metadata uses a separate `view` reader. Three bounds-checked-reader implementations; all correct, but the consolidation was partial.
- Impact: maintenance; a bounds-logic improvement must be applied in 3 places. Low risk (all currently correct).

## DUP-004 — 32/64-bit PE parser logic duplicated rather than width-parameterized
- Category: Duplication. Severity: Low. Confidence: Verified. Status: Open.
- Evidence: pe.py _parse_imports64/_tls64/_delay_imports64 mirror pe32.py _parse_imports/_tls/_delay_imports at 64-bit width. Deliberate split; some drift risk (pe32 uses local max_thunks literal, pe.py uses MAX_IMPORT_THUNKS constant).
- Impact: low; behavior-preserving consolidation possible but not required.

## Parser layer — positive assurance (no finding)
- pe.py/pe32.py/coff.py/coff_archive.py/pdb.py/msvc_metadata.py/binary_reader.py: grep-verified NO eval/exec/pickle/marshal/os.system/__import__/yaml.load. All reads bounds-checked; explicit safety caps (import thunks 1e6, TLS callbacks 65536, resource depth 8 + cycle detection + 100k entry budget, archive members 1e6/symbols 1e7, export counts 1e6, PDB streams/blocks/modules capped). Malformed-input handling verified robust (Verified static + runtime R-010). This is the strongest-engineered subsystem in the repository and directly fulfills SECURITY.md's bounds/untrusted-input controls.

## SEC-002 — db-query raw SELECT: not read-only connection, DoS-capable (by design)
- Category: Security. Severity: Informational. Confidence: Verified. Status: Open.
- Evidence: analysis_db.query() guards SELECT-only (startswith); SQLite single-statement execution blocks stacked DDL; but connection not opened mode=ro and a heavy SELECT can exhaust CPU/memory. Scriptability feature; acceptable for local DB. Note only.

## SEC-003 — service function_id path containment (to verify)
- Category: Security. Severity: Possible (pending). Confidence: Unverified. Status: Open — verify in B07.
- Evidence: /api/functions/{function_id:path}/workflow → load_function_workflow(root, normalized). Need to confirm workflow loader constrains normalized under root (ensure_relative_path). If not, read-only path traversal to arbitrary workflow.json.

## SEC-004 — service --host allows unauthenticated non-loopback bind
- Category: Security. Severity: Low. Confidence: Verified. Status: Open.
- Evidence: run_service default host=127.0.0.1 (good) but `x86decomp serve --host 0.0.0.0` exposes the read-only project API with no auth. Remediation: warn on non-loopback bind or require an explicit --allow-remote flag. Read-only limits impact.

## Subsystem security — positive assurance (no finding)
- SQL across governance/reconstruction/native/assembly/analysis_db/work_queue: parameterized (?-placeholders + param tuples); f-string SQL only interpolates static clause fragments and placeholder counts (verified hypotheses.py:153-165, provenance.py:153). No injection.
- Subprocess (ghidra/compiler/compiler_worker/dynamorio/ground_truth/integration/plugins/materialize): argument arrays, no shell=True anywhere (grep-verified), timeouts enforced, absence→ExternalToolError (BLOCKED policy).
- Network (transport same-origin redirect + env-var secrets; mcp URL scheme check; service loopback+read-only+CSP+DOM-safe). Archive extraction (test_bundle) is a model-safe implementation.
- grep across entire src: no eval/exec/pickle/marshal/os.system/yaml.load(untrusted). SECURITY.md controls are substantively implemented in code.

## SEC-003 (resolved to a real finding) — Path traversal via unsanitized function_id in workflow loader
- Category: Security. Severity: Medium. Confidence: Verified (static). Status: Open.
- Direct evidence: workflow.py _state_path (line 133) = `project_root.resolve() / "functions" / function_id.replace(":","_") / "workflow.json"` with NO rejection of '/' or '..'. load_function_workflow (170) opens it directly. contracts.ensure_relative_path exists but is NOT used here.
- Corroboration: service.py /api/functions/{function_id:path}/workflow (route allows slashes) calls load_function_workflow(root, normalized) with the raw URL segment; CLI workflow-show also passes function_id straight through.
- Consistency: contradicts SECURITY.md 'Validate paths...reject...output paths outside declared roots' and the codebase's own ensure_relative_path helper used elsewhere.
- Exploitability: read-only oracle — target must be a file literally named workflow.json containing JSON whose function_id starts 'pe-rva:' (FunctionWorkflow.from_dict enforces). Constrained, but a genuine containment break; materially worse if service is bound non-loopback (SEC-004). Also affects save path (_state_path used by save_function_workflow) → potential write traversal when function_id is attacker-influenced (writes workflow.json under a traversed dir).
- Remediation: validate function_id with validate_id()/a `pe-rva:<hex>` regex before path construction, or route through ensure_relative_path.

## REPO-001 (final confirmation R-016)
- The project's own `scripts/source_hashes.py verify` returns valid=False on the shipped tree: 68 hash mismatches (root) + 15 test-suite failures; overall invalid. `make verify`→verify-hashes fails. Product-relevant unlisted files: CODE_AUDIT_REPORT.md only (other unlisted = this audit's project-audit/). REPO-001 severity High CONFIRMED by first-party tooling. Note: the 68 files match the post-audit fix-pass scope (src core + tests + test-suite), consistent with 'edited after packaging, manifest not regenerated'.

## PROCESS-NOTE (audit self-disclosure, not a product finding) — 76 bytecode files added by the audit
- The audit's Phase-10 execution of the project's own scripts wrote 76 .cpython-310.pyc files into src/ (+4 scripts/). No existing file content was modified. The sandbox FUSE mount denies deletion, so they could not be cleaned in-session. They are gitignored, regenerable, ignored by the manifest verifier, and removable by the user via `make clean`. Fully disclosed in RUN_LOG R-020 and COVERAGE_REPORT. This is an auditor side-effect, NOT a defect in the audited project.

## Phase-10 execution summary (positive assurance)
- pyflakes CLEAN (R-021), full-tree compileall PASS on 3.10 (R-021, confirms reports.py C1 fixed), validate-contracts PASS (R-018), all 97 schemas valid (R-017), source_hashes verify FAIL=REPO-001 (R-016), ~80+ tests pass with every failure attributed to sandbox py3.10 / missing optional toolchains — ZERO product-attributable test failures found (R-013/R-022). Surface counts 59/239/166 verified live (R-012). CLI-001/002 runtime-verified (R-010/R-011).

## REPO-005 (Phase-11 fact-check → Verified)
- Upgraded Strongly-supported → VERIFIED. Direct evidence (R-023): unpacking dist/x86decomp_toolkit-0.7.11.tar.gz shows test-suite reports.py STILL contains the raw backslash-in-f-string (py3.11 SyntaxError; escaped_summary fix ABSENT), while the shipped SOURCE tree has the fix. Meanwhile sdist governance/cli.py DOES have the CR-0710-001 json import — confirming the exact timeline: SECOND_AUDIT fixes → package @18:44 (dist built) → CODE_AUDIT_REPORT @19:27 → 68-file fix pass incl. reports.py → manifest+dist NOT regenerated. pip-installing the shipped sdist yields code that fails to import on Python 3.11 (the lowest supported version), whereas auditing the shipped source would not reveal it. Severity High CONFIRMED.

## Phase-11 fact-check confirmations (all Critical/High re-verified against tree)
- REPO-001: source_hashes verify still valid=False, 68 mismatches (R-023). Verified.
- REPO-005: sdist carries pre-fix reports.py (R-023). Verified.
- CLI-002: cli.py:444 except tuple confirmed lacks OSError. Verified.
- CLI-001: cli_utils.py:20 CLI_ERROR_TYPES confirmed lacks X86DecompError family. Verified.
- SEC-003: workflow.py:133-136 _state_path confirmed no '/'/'..' sanitization. Verified.
- All line/symbol references in the register spot-checked accurate.
