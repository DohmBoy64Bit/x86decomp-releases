# Agent and contributor operating rules — 0.4.0

These rules bind human contributors, coding agents, reverse-engineering agents, MCP clients, and automation working on this repository or a generated target project.

## 1. Truth and vocabulary

Never encode a guess as recovered fact.

Required labels:

- `observed`: directly present in a captured artifact, byte sequence, tool output, or trace;
- `derived`: deterministically calculated from observations;
- `proposed`: useful interpretation not yet verified;
- `corroborated`: multiple supports but below the verification gate;
- `verified`: passed the exact project gate for the narrow claim;
- `rejected`: falsified or contradicted for the named artifact/version;
- `unknown`: insufficient evidence.

Decompiler output, AI output, naming suggestions, type guesses, and template choices are proposals. Three-source verification reduces correlated error; it is not a truth guarantee. Static-reference absence is not proof of no runtime access. Finite tests and bounded symbolic results are not universal proofs.

## 2. No-placeholder policy

No supported feature may be represented by:

- a TODO or empty success branch;
- a shim that returns a success-shaped document without performing the work;
- a mock adapter in production code;
- a schema with no producing/consuming implementation;
- documentation that claims a subsystem absent from the command/API surface;
- a fallback that silently weakens a verification property.

Unavailable optional tools must produce an explicit dependency error or `BLOCKED` test result. Unsupported input must produce a bounded failure with the exact reason.

## 3. Two-mode separation

Matching state:

```text
not_started → decompiled → compiles → abi_compatible
            → instruction_similar → byte_matched
            → image_integrated → full_relink_validated
```

Functional state:

```text
not_started → decompiled → compiles → abi_compatible
            → differentially_validated
            → symbolically_bounded
            → integration_validated
```

Either mode can enter `blocked`. Never advance one mode because the other advanced. Regressions require an explicit reason, retained prior report, and audit event.

## 4. Target packs and templates

Target-specific facts belong in a verified target pack, not generic runtime code.

- Keep parser observations separate from operator decisions.
- Preserve `unknown` rather than guessing compiler, linker, language, original files, or flags.
- A source extension in a PDB is evidence, not automatic proof of the complete source language.
- A generated template may create directories, policies, pipelines, helpers, and blockers. It may not generate fake decompiled function bodies or fake compiler profiles.
- Target-specific overrides must cite artifact hashes and rationale.
- Rebuilt-image comparison is allowed only against the exact reference hash named by its image profile.

## 5. Evidence before mutation

Before a rename, prototype/type change, source promotion, PE patch, relink acceptance, Ghidra write, or release-state change:

1. verify project and memory integrity;
2. capture the exact current artifact;
3. create or identify evidence records;
4. state the narrow claim and validator;
5. apply one reversible conceptual change;
6. rebuild/re-export;
7. run named validators;
8. record outputs, hashes, and transition in project memory.

Ghidra MCP writes require a tool allowlist, rationale, evidence IDs, persisted proposal, and exact approval hash. Bulk writes require a reviewed change set and rollback plan.

## 6. Triple fact-check gate

A claim can be `verified` only when all are true:

- at least three support records;
- at least three independent failure domains;
- at least two evidence kinds;
- valid hashes for file-backed evidence;
- no unresolved contradiction;
- claim wording no broader than the evidence.

Multiple outputs derived from one Ghidra database are generally one independent group. Multiple AI summaries are not independent evidence. A compiler and a disassembler sharing the same malformed input may also be correlated; record that dependency.

## 7. Address, range, and artifact contracts

- Stable function ID: `pe-rva:XXXXXXXX`.
- Directory ID: `pe-rva_XXXXXXXX`.
- Ranges are unsigned, sorted, half-open, and all discontiguous ranges are preserved.
- Ghidra address strings are display/provenance, not stable identity.
- Immutable evidence changes only by creating a new object/version.
- Archive extraction rejects traversal, absolute paths, duplicate names, symlinks, hard links, devices, excessive members, oversized files, and expansion bombs.
- COFF classic and bigobj symbol widths remain distinct after format detection.
- Linker public-symbol order is not byte-accurate contribution evidence.
- PDB/MAP/OBJ names can be promoted as build-authenticated only when tied to the exact image/build.

## 8. Durable orchestration

Every pipeline stage must declare:

- stable stage ID and kind;
- dependencies;
- input paths/hashes;
- expected outputs;
- command as an argument array or exact evidence-gate contract;
- environment policy;
- worker isolation and limits;
- retry/cancellation behavior.

Successful outputs must be materialized outside ephemeral work directories, hashed, stored immutably, and revalidated before reuse. Missing or altered output invalidates prior success. Runner heartbeats are durable. Stale-job recovery is explicit and logged; it never assumes partial output is complete.

## 9. Project migrations and recovery

- Schema migrations are monotonic, versioned, transactional, and tested from every supported legacy schema.
- Non-dry-run migration requires a deterministic backup or an explicit recorded backup path.
- Restore extracts through a staging directory and verifies project integrity before final placement.
- Repair may reconstruct indexes and empty infrastructure only; it may not rewrite evidence or target bytes.
- Garbage collection defaults to dry-run and deletes only content not referenced by project state.
- Concurrent writers use transactions/leases; never bypass the state database with ad hoc edits.

## 10. External execution and worker security

- Static parsing/import never executes the target.
- Local bounded workers are not a security boundary.
- Container workers use a pinned image, read-only root, disabled network, dropped capabilities, `no-new-privileges`, explicit mounts, and resource limits.
- Unknown native programs run only in a disposable VM or approved external sandbox.
- Every process has a timeout, bounded output, separate stdout/stderr logs, return code, and tool/version hash where relevant.
- Never use shell interpolation for user-controlled commands.
- Proprietary historical toolchains are operator-owned and registered by path/hash; never redistribute them.

## 11. Validator semantics

- `compiles`: the declared compiler emitted the expected artifact.
- `abi_compatible`: every declared ABI observation/check passed; not semantic proof.
- `instruction_similar`: a versioned normalized instruction/CFG comparison passed.
- `byte_matched`: raw bytes in the exact stated scope are identical.
- `relocation_normalized_match`: equality after documented relocation masks; not byte identity.
- `differentially_validated`: all declared concrete harnesses passed.
- `symbolically_bounded`: selected model/backend found equality within recorded bounds and without disqualifying truncation.
- `integration_validated`: named scenarios passed in the recorded environment.
- `full_relink_validated`: the declared linker/output/image gate passed; not proof that original linker decisions were recovered.
- `profile_normalized_match`: images match after only named profile ranges; never call it raw identity.

## 12. Compiler, linker, and corpus rules

- Hash compiler, linker, libraries, profiles, source, environment policy, and outputs.
- Compiler cache keys include every semantically relevant input.
- Resolve COMDAT groups before inferring object layout.
- Preserve relocation and auxiliary records; unknown forms remain raw evidence.
- Preserve ASSOCIATIVE parents and report conflicts rather than choosing a convenient winner.
- Linker reconstruction decisions cite MAP contribution, object, section, alignment, symbol, and/or neighboring evidence.
- Generated source corpus cases are reproducible source inputs only. They become compiler ground truth only after successful recorded builds.
- Similar object bytes are code-generation evidence, not a compiler identity oracle.

## 13. C++ and symbolic-depth rules

- RTTI/vtable scans require section, pointer, count, and executable-slot validation.
- Adjustor thunks are candidates until call relationships and class evidence corroborate them.
- x64 unwind metadata is not automatically a source-level exception construct.
- x86 FuncInfo scans remain candidates until handler-specific fields validate.
- Linked TLS, `.tls$*`, `.CRT$XL*`, and `.CRT$X*` contributions remain distinct evidence classes.
- Symbolic reports record instruction subset, path/step/time bounds, memory model, alias assumptions, observations, unsupported operations, counterexamples, and truncation reason.
- Truncated exploration cannot satisfy a completed bounded-equivalence gate.

## 14. AI work

AI may draft candidates, names, types, tests, compiler experiments, and explanations. AI may not:

- count as evidence;
- accept its own work;
- mutate canonical state directly;
- hide contradictions or failures;
- invent tool/API behavior;
- silently skip validators;
- claim generated source is original.

The work queue accepts a proposal only after every required validator report passes.

## 15. Release and documentation contract

A release is complete only when:

- implementation, schemas, examples, CLI, docs, skill, feature catalog, and project memory agree;
- all previous supported commands and schemas remain compatible or have tested migrations;
- root and integrated test-suite tests pass with zero pytest skips;
- every defined Python function/method executes at least one body line under coverage;
- all four Mermaid/ASCII architecture maps are synchronized;
- package wheel/sdist and test-suite wheel/sdist build and clean-install;
- source ZIP manifest verifies after extraction;
- optional live adapters are either tested or explicitly `BLOCKED`—never represented as pass;
- caches, virtual environments, downloaded adapters, machine paths, build outputs, and test results are absent from source artifacts;
- `VERIFICATION.md` distinguishes executed tests from unavailable integrations;
- unsupported/general-unsolved behavior is explicit.

## 16. Mandatory startup sequence

For target work:

1. read `project.json`, target pack, acceptance policy, and current memory;
2. run project and memory integrity checks;
3. inspect function workflow states and blockers;
4. verify relevant artifact hashes;
5. identify the exact mode and next validator;
6. create or claim a work item;
7. make the smallest evidence-grounded change;
8. validate and record.

For repository changes:

1. run the existing regression suite before editing;
2. inventory current command/schema/function surface;
3. add implementation and contracts together;
4. add positive, malformed-input, integrity-failure, migration, and regression tests;
5. regenerate the feature catalog and manifests;
6. run packaging and clean-install checks;
7. update changelog, parity matrix, skill, maps, memory, and verification record.
