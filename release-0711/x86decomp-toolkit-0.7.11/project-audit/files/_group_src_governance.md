# Grouped audit — governance/ subsystem (15 files) (B06g-gov)

Depth: structural digest (AST + full risk sweep R-014) with targeted reads of SQL construction (all parameterized, verified B06) and zip handling (plugins/proofs read fully at risk sites). Evidence-governance is a core product plane (FEATURE_PARITY). Hashes in FILE_INVENTORY.csv. All parameterized SQL; f-string SQL only builds static WHERE fragments + placeholder counts (verified hypotheses.py:153-165). No injection anywhere in this subsystem.

- __init__.py (6): package marker. Audited — complete.
- store.py (418): GovernanceStore — connection/transaction/audit/schema (executescript with static _SCHEMA_SQL). Central store; parameterized. Audited — complete.
- campaigns.py (367): CampaignEngine — lifecycle, budget accounting, branching, next-action selection. Parameterized SQL; budget-exhaustion → status='blocked' (no silent skip). Audited — complete.
- candidates.py (279): CandidateStore — content-addressed candidate/files/lineage; unlink scoped to store; parameterized incl. executemany. Audited — complete.
- changesets.py (90): ChangeSet — zip WRITE (writestr) + infolist READ only; no disk extraction → no traversal. Audited — complete.
- consensus.py (115): ConsensusEngine — multi-observation consensus; f-string WHERE (static). Audited — complete.
- counterexamples.py (131): CounterexampleStore + ddmin_bytes (delta-debug minimizer, bounded). unlink scoped. Audited — complete.
- family.py (119): BinaryFamilyStore — family grouping. Parameterized. Audited — complete.
- hypotheses.py (398): HypothesisLedger — creation/deps/evidence/confidence scoring/state machine; STATES validated before use in WHERE. Audited — complete.
- knowledge_graph.py (100): KnowledgeGraph — subject/relation/object triples (matches db-constraint CLI). `..` = docstring. Audited — complete.
- plugins.py (124): PluginRegistry — FULL READ. Plugins are out-of-process executables: validate_manifest (non-symlink regular file), install (records sha256), doctor (re-verifies hash), invoke (subprocess argv, timeout, output cap). `__import__("hashlib")` = inline stdlib import (MAINT nit). Hash-pinned external adapters; sound. Audited — complete.
- proofs.py (196): ProofLedger/ProofBundle — proof obligations + bundle zip. Zip inspect validates member paths (is_absolute/../backslash/colon rejected, proofs.py:143); writes only. Degenerate docstrings (DOC-001). Audited — complete.
- reviews.py (116): ReviewQueue — review items with priority; f-string WHERE (static) + LIMIT ? param. Audited — complete.
- workers.py (84): WorkerRegistry — worker profiles; f-string WHERE (static). Audited — complete.
- cli.py (240): governance CLI — build_parser/dispatch/main via run_cli (CR-0710-001 json import fix present). Subject to CLI-001 (run_cli error tuple) at subsystem-main entry. Audited — complete.

Findings: DOC-001 (boilerplate/degenerate docstrings across subsystem), CLI-001 (subsystem main error routing), MAINT (inline __import__ in plugins). No correctness/security defects; SQL uniformly safe.
