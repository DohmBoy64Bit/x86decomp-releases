# Cross-File Analysis — x86decomp-toolkit 0.7.11

## Architecture & module boundaries
Layered and coherent (see ARCHITECTURE_NOTES + REVERSE_ENGINEERING_PRACTICES): parsers → analysis → evidence/governance → reconstruction/native/assembly → reporting, over shared util/contracts/models/errors. Dependency direction is mostly downward (subsystems depend on core parsers + contracts, not vice versa). No import cycles observed in the reviewed set. Four capability subsystems each own a cli.py + store.py + domain modules, unified by canonical.py.

## Duplication matrix
| # | Symbols involved | Similar behavior | Key differences | Consolidation safe? | Direction |
|---|---|---|---|---|---|
| DUP-002 | util.py vs contracts.py | utc_now, sha256_bytes/file, canonical JSON, atomic_write_bytes, ensure_relative_path, read/load_json, write_json | atomic_write chmods 0644 (contracts) vs 0600 (util); ensure_relative_path resolve-based (util, root+candidate) vs string-based (contracts, single arg); ContractError base differs | Medium risk — semantics differ; needs deliberate reconciliation | Pick one primitive module; alias the other |
| ARC-001 | errors.ContractError vs contracts.ContractError | both "contract violation" | errors' is X86DecompError(Exception); contracts' is ValueError; different catchability | Medium — 47 importers of contracts', util raises errors' | Collapse to one ContractError |
| DUP-003 | binary_reader.BinaryReader vs pdb._require/_u16/_u32 vs msvc_metadata `view` | bounded LE reads | all correct; 3 implementations | Low risk | Route pdb/msvc through BinaryReader |
| DUP-004 | pe.py _parse_imports64/_tls64/_delay64 vs pe32.py equivalents | directory parsing | width 32 vs 64; pe32 uses local literal, pe uses named const | Low risk | Parameterize width or accept split |
| CLI dup | 6 cli.py main()/dispatch wrappers | parse→dispatch→emit→catch | run_cli now shared by 4 subsystems + canonical; root cli.py NOT migrated (CLI-002) | Low risk | Migrate root cli.py onto run_cli |
| DUP-005 | corpus/ vs src/x86decomp/corpus/ | 24 ground-truth sources | duplicated for package-data | Informational | Conventional; leave or graft |
| DUP-001 | root docs adapter-note paragraph | verbatim in 4 docs | none | Low | Single source + include |

## Inconsistent abstractions / naming
- Two error hierarchies + two ContractError (ARC-001) is the main inconsistency. Otherwise naming is consistent (verb-noun commands, _parse_* helpers, *Store/*Ledger/*Engine classes).
- Error output grammar differs root (plain) vs subsystem (JSON) — CLI-002.

## Conflicting data models — none found
models.py enums + per-capability schemas are namespaced and additive; no conflicting definitions of the same concept observed. VerificationStatus is defined+exported+test-pinned but unused by any runtime path (MAINT-002).

## Dead / orphaned / unreachable
- VerificationStatus enum: no runtime producer/consumer (MAINT-002, Low, grep-verified).
- No unreachable commands: all 106 flat + 239 canonical routes dispatch (live catalog matches parser, R-012/R-019).
- No TODO/FIXME/NotImplementedError stubs in src/ (prior audit + my grep confirm).
- Root cli.py final `raise AssertionError("unhandled command")` is defensive-unreachable while parser/chain stay in sync.

## Documentation contradictions / config inconsistencies
- REPO-001: MANIFEST.sha256 (+ ALL_FILE_MANIFEST, test-suite manifest) contradict the actual tree (68+15 files). RELEASE_VERIFICATION claims 449/449 (true at packaging, false now).
- REPO-004: .gitignore/MANIFEST.in target test-suite/-relative ignore paths while README/CI write those byproducts to repo ROOT.
- REPO-005: dist/ wheels predate the source fix pass.
- MAINT-001: CODE_AUDIT_REPORT.md ships describing already-fixed defects with no disposition.
- DOC-002: MkDocs required by AGENTS/PROJECT_MEMORY/SKILL but no mkdocs.yml exists.
- source-basis.md says the package doesn't vendor Ghidra — technically true (the 1.4GB Ghidra is local harness state under .x86decomp-test-tools, not the package), but its presence in the release tree (REPO-003) muddies that claim.

## Error-handling / logging consistency
- Error handling disciplined tree-wide (rollback-and-re-raise in transactions; narrow excepts; broad Exception only for genuinely-unpredictable parses returning safe defaults). The inconsistency is the CLI catch-tuple drift (CLI-001/002) + two ContractError (ARC-001).

## Testing gaps (cross-file)
- No single monolithic pytest completion demonstrated (TEST-001). Negative/fuzz coverage lighter than happy-path (parsers are robust regardless). Optional-dep paths (angr/unicorn/z3/lief/fastapi) only exercised when installed.

## Security boundaries (cross-file) — consistent and strong
- Untrusted-binary parsing (bounded), subprocess (argv/no-shell/timeout), network (loopback+same-origin+env-secrets), archive extraction (safe), worker isolation (RLIMIT+container), SQL (parameterized). One real defect: SEC-003 path traversal via function_id.

## New-user & contributor experience
- New user: strong docs + exactly-synced command reference, but 78 help-less flat commands (CLI-003) and a release that fails its own `make verify` (REPO-001) hurt first-run confidence.
- Contributor: AGENTS.md + evidence vocabulary + gates are clear; the un-regenerated manifests + stale audit report + missing MkDocs send mixed signals about release discipline.

## Packaging / portability
- src-layout, zero required deps, optional extras well-bounded; CI matrix ubuntu+windows × py3.11-3.13. Portable. Contamination (REPO-003) and stale dist (REPO-005) are the packaging problems.
