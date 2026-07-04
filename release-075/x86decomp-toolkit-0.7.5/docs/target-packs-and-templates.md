# Target packs and grounded project templates

## Purpose

A target pack is the immutable, target-specific boundary between generic toolkit code and facts about one authorized binary. It prevents target assumptions from leaking into the runtime and prevents a template generator from inventing source, compiler, linker, or layout information.

## Contents

A generated pack contains:

```text
target-pack/
  target.toml             observed identity plus explicit decisions
  observations.json       bounded parser output
  image-profile.json      reference-hash-bound image layout
  acceptance.json         matching/functional minima
  template-plan.json      adapter needs and unresolved facts
  artifacts/              copied evidence when copy mode is used
```

`target.toml` records artifact hashes and explicit decisions. `observations.json` records parser output. They are intentionally separate.

## Inputs

`target-pack-infer` accepts a primary native PE and optional matching PDB, linker MAP, COFF objects, static/import libraries, and rebuilt image. Every artifact must be a regular file. The default copies artifacts into the pack. `--reference-artifacts` records external paths instead; this is less portable and should be used only when policy forbids copies.

## Decisions

The accepted decision fields are:

- `preferred_mode`: `matching`, `functional`, or `both`;
- `compiler_family` and `compiler_version`;
- `linker_family`;
- `source_language`;
- `allow_host_execution`;
- `target_description`.

Unknown values remain `unknown`. A PDB source filename ending in `.cpp` is recorded as source-language evidence, not automatically promoted to an authoritative project-language decision.

## Template derivation

The template engine uses only verified pack contents and explicit decisions. It calculates:

- enabled modes;
- exact assembly fallback need;
- whether object comparison, linker reconstruction, or whole-image comparison has enough supplied artifacts to start;
- whether compiler/linker identities are confirmed;
- whether dynamic host execution is authorized;
- evidence-backed source-language candidates;
- unresolved blockers.

The engine does not emit candidate function bodies or fake compiler profiles.

## Generated project

`project-from-target` initializes the project, copies the pack, creates the durable default pipeline, copies Ghidra scripts where available, and materializes:

```text
src/matching/
src/functional/
src/asm/
include/
compiler-profiles/
linker-layout/
tests/differential/harnesses/
tests/integration/scenarios/
reports/matching/
reports/functional/
reports/convergence/
reports/reproducibility/
config/project-template.json
config/validation-policy.json
config/next-steps.json
scripts/project.py
TARGET.md
```

## Evidence-safe workflow

1. Verify the pack.
2. Generate the project.
3. Read `config/project-template.json` blockers.
4. Resolve blockers only with evidence or an explicit user decision.
5. Add compiler profiles only after identifying and hashing the toolchain.
6. Generate source candidates from function artifacts, not assumptions about original files.
7. Run validators before advancing matching or functional state.
8. Record decisions and state transitions in project memory.

## Commands

```bash
x86decomp target-pack-infer target.exe target-pack/ --decisions decisions.json
x86decomp target-pack-verify target-pack/
x86decomp template-derive target-pack/
x86decomp project-from-target target-pack/ project/
x86decomp template-materialize project/
```

## Limitations

The template engine cannot determine original source organization, compiler flags, link order, class hierarchy, or function semantics merely because a PE was supplied. Optional PDB/MAP/OBJ/LIB evidence can narrow those unknowns, but every promotion remains provenance-bound.
