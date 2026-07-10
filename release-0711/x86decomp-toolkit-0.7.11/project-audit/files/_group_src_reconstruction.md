# Grouped audit — reconstruction/ subsystem (14 files) (B06g-recon)

Depth: structural digest + full risk sweep (R-014); acceleration.py network sites read; SQL verified parameterized (provenance.py:153 IN-clause uses static placeholder count). Hashes in FILE_INVENTORY.csv.

- __init__.py (7): package marker. Audited — complete.
- store.py (176): ReconstructionStore — schema/connection; parameterized; sqlite_master introspection uses LIKE 'reconstruction_%' (static). Audited — complete.
- cli.py (465): reconstruction CLI — build_parser/dispatch/main; CR-0710-002 (write_json import) + CR-0710-003 (json import in error handler) fixes present; hosts the llm routes. Packed one-liner style (prior M3). Subject to CLI-001. Audited — complete.
- acceleration.py (1985 — largest module): human-readable decompilation acceleration; LLM job/batch construction, candidate promotion. `socket`/`urlopen` appear for local-endpoint probing (loopback LLM), consistent with local_llm posture; not arbitrary fetch. CR-0710-005 dead-assignment (unused db) fix applies here — verified no stray unused var at the noted site. Very large; cohesive around the LLM acceleration workflow. DOC-001 present. Audited — complete.
- abi_contracts.py (59): ABIContracts — ABI record store. Audited — complete.
- builds.py (231): BuildManager — build systems/targets/variants/generated sources. Audited — complete.
- capsules.py (64): Capsules — capsule zip WRITE + manifest/namelist READ only (no disk extraction → no traversal). Deterministic zip (fixed 1980 timestamps → reproducible archives, good). Audited — complete.
- generated_tests.py (121): GeneratedTests — regression-contract tests backed by the store. Audited — complete.
- headers.py (174): HeaderManager — C/C++ header reconstruction + symbol recording. Audited — complete.
- libraries.py (37): LibraryRecognition — library identification. Audited — complete.
- project_layout.py (114): ProjectLayout — reconstruction project layout. Audited — complete.
- provenance.py (181): ProvenanceLedger — maps reconstructed source ranges to binary regions with evidence; source-edit reconciliation invalidates stale proof obligations (semantic edits). IN-clause SQL built with static '?' placeholder count + param tuple (verified). Audited — complete.
- security.py (97): SecurityReview — observational security review over reconstructed behavior. Audited — complete.
- semantic_changesets.py (63): SemanticChangeSets — semantic changeset records. Audited — complete.

Findings: DOC-001, CLI-001, M3 (packed one-liners in cli.py). No correctness/security defects; SQL safe.
