# Reverse-Engineering Practice Audit — x86decomp-toolkit 0.7.11

Judged against the project's stated scope: authorized static-by-default analysis, reconstruction, and byte-exact validation of native Windows x86/x86-64 PE/COFF artifacts, with an evidence-governance discipline.

## Separation of acquisition / parsing / analysis / interpretation / reporting — STRONG
Clear layering (ARCHITECTURE_NOTES + verified in code): pure parsers (pe/pe32/coff/coff_archive/pdb/msvc_metadata) → analysis (disassembly/symbolic/dynamic/angr/image_match) → evidence/governance (evidence.py three-source gate, claims, memory) → reconstruction/native/assembly → reporting (JSON reports via atomic writers, schemas). Interpretation is explicitly separated from raw facts by the evidence vocabulary (observed/derived/proposed/corroborated/accepted/verified) enforced through ClaimState + EvidenceKind.

## Evidence provenance & input hashing — STRONG
- Inputs hashed on parse (PE64Image.file_sha256, section sha256, content_store content-addressing, tool snapshots by hash, toolchains by executable hash, plugins hash-pinned). Ghidra export records executable sha256.
- Content store is immutable/content-addressed; project memory is append-only hash-chained.

## Reproducibility & determinism — STRONG (with one release-integrity caveat)
- canonical_json (sorted keys, tight separators) + deterministic IDs (stable_id) + fixed zip timestamps (capsules 1980) + seed-deterministic synthetic corpus + reproduction manifests (reproduce-create/verify) + deterministic source manifests (source_hashes.py).
- CAVEAT: the shipped release itself violates its reproducibility contract — MANIFEST.sha256 fails (REPO-001) and dist/ artifacts predate the source fixes (REPO-005). The MACHINERY for reproducibility is excellent; the 0.7.11 release was not re-sealed after its post-audit fix pass.

## Safe handling of malformed/adversarial input — EXEMPLARY
- All binary parsers bounds-check every read (BinaryReader.require, overflow-safe), enforce explicit safety caps (import thunks 1e6, TLS callbacks 65536, resource depth 8 + cycle detection + 100k entry budget, export/section/archive-member/PDB-stream caps), and raise FormatError rather than truncating silently. Verified by full read (B05) + runtime (R-010). No eval/exec/pickle anywhere (grep-verified).
- Archive/tar extraction (test_bundle zip, project_state tar) are model-safe: traversal + symlink + zip-bomb + member-count + size-cap defenses, extractall(filter="data").
- The ONE traversal defect is SEC-003 (function_id not sanitized before path build in workflow.py) — read/write oracle, Medium. Not a parser issue.

## Bounds / resource limits / timeouts — STRONG
- Parser caps (above). Worker RLIMIT (CPU/AS/NPROC/FSIZE) + container isolation (--network=none --read-only --cap-drop=ALL). Subprocess timeouts everywhere (ghidra/compiler/dynamorio/objdiff/plugins). Symbolic/dynamic bounded by max_steps/max_paths/max_instructions. Integration output byte-bounded.

## Sandboxing & execution consent — STRONG
- Static-by-default; native/live execution gated behind explicit flags (allow_host_execution, runtime opt-in) and bounded isolation. worker.py honestly labels local mode "not a security boundary" and offers container mode for real isolation. Matches SECURITY.md/AGENTS.md consent policy.

## Traceability findings→evidence & confidence levels — STRONG
- Evidence IDs + independent-group tracking; claims carry state + evidence/contradiction IDs; three-independent-source gate for verification; governance ledger (hypotheses/proofs/counterexamples/consensus) preserves contradictions (counterexamples.ddmin minimizes them). Confidence is a first-class concept (the exact discipline this audit also follows).

## Format-version / architecture / endianness awareness — STRONG
- Explicit i386 vs AMD64 dispatch (parse_pe), PE32 vs PE32+ separation, COFF classic + BIGOBJ, MSF 7.0 PDB, little-endian throughout with documented scope. Honest about what is NOT modeled (linked-PE relocations ≠ full COFF reloc set — source-basis.md).

## Analyst usability & workflow alignment — GOOD
- Matches common RE workflows: Ghidra headless export → analysis DB → candidate source → compile → objdiff/byte-diff → symbolic/dynamic validation → release gate. decomp.me packet export, objdiff integration, MCP gateway for Ghidra. Matching vs functional as distinct state machines. The CLI discoverability gaps (CLI-003) are the main friction for new analysts.

## Extensibility — GOOD
- Plugin registry (hash-pinned out-of-process adapters), adapter catalog, additive namespaced schemas, toolchain registry. New formats/architectures would require new parser modules (the 32/64 split shows the pattern; DUP-004 notes it's copy-not-parameterized).

## Legal/ethical framing — PRESENT
- "Authorized" analysis framing throughout; SECURITY.md + supported-scope.md + source-basis.md set boundaries; test bundles require an authorization statement; no source-text-recovery overclaim.

## Verdict
The reverse-engineering practice is, on the merits, EXCELLENT and unusually disciplined for a project of this size — the parser safety, evidence governance, reproducibility machinery, and execution-consent model are all strong and largely match the documentation. The gap between practice and the shipped artifact is REPO-001/REPO-005: the release was not re-sealed after fixes, so the very reproducibility/provenance guarantees the tool is built to provide do not hold for its own 0.7.11 distribution.
