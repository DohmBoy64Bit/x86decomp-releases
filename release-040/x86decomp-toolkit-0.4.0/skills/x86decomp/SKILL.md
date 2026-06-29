---
name: x86decomp-evidence-engineer
description: Evidence-first operation of x86decomp-toolkit 0.4.0 for durable matching and functional decompilation of authorized native Windows x86/x86-64 PE targets.
version: 4.0.0
license: Apache-2.0
compatibility: Python 3.11+, native PE32/i386 and PE32+/AMD64, optional Ghidra and bounded validation adapters
metadata:
  release_contract: 0.4.0
  modes:
    - matching
    - functional
  architectures:
    - x86
    - x86_64
  evidence_policy: three-independent-source-gate
  execution_policy: static-by-default-explicit-consent-for-native-execution
  project_schema: 3
  target_pack_schema: 1
  pipeline_schema: 1
  no_placeholder_policy: true
tags:
  - reverse-engineering
  - decompilation
  - x86
  - x86-64
  - pe
  - ghidra
  - evidence
  - reproducibility
  - orchestration
---

# x86decomp evidence engineer

## Purpose

Use this skill to create, operate, recover, and release an x86decomp project without confusing plausible reconstruction with recovered fact. The goal is a durable project in which:

- every target artifact has a content identity;
- observations and decisions are separated;
- matching and functional goals advance independently;
- every source candidate is reproducibly buildable;
- validator claims are narrow and scope-bound;
- interrupted work can resume safely;
- release acceptance can be reproduced or explained on another machine.

This skill does not authorize analysis of a target. Confirm ownership or permission before importing artifacts.

## Non-negotiable truth rules

1. Never call a decompiler or AI output original source.
2. Never call a plausible name or type original unless exact-build evidence authenticates it.
3. Never convert an unknown compiler, linker, language, flag, object boundary, or class relationship into a convenient default.
4. Never treat a missing static reference as proof of no runtime reference.
5. Never call instruction similarity byte identity.
6. Never call relocation-normalized equality raw equality.
7. Never call finite differential tests universal equivalence.
8. Never call a bounded solver result complete beyond its model and bounds.
9. Never treat three-source review as a guarantee of truth.
10. Never hide unsupported instructions, parser bounds, timeouts, truncation, contradictions, or failed adapters.
11. Never represent an unimplemented subsystem with a TODO, shim, fake success, or empty adapter.
12. Never execute unknown native code on the ordinary host merely because it was imported.

## Required epistemic vocabulary

- **Observed** — directly captured from an artifact, tool output, or trace.
- **Derived** — calculated deterministically from observed inputs.
- **Proposed** — interpretation or candidate not yet verified.
- **Corroborated** — supported by multiple records but below the verification gate.
- **Verified** — passed the exact project claim gate.
- **Rejected** — contradicted or falsified for the named artifact/version.
- **Unknown** — insufficient evidence.

Every analytical response should identify which category applies.

## Separation of concerns

### Immutable evidence

Target binaries, PDBs, MAP files, objects, libraries, compiler outputs, traces, and reports are immutable content-addressed artifacts. Never edit them in place. Create a new artifact and retain the old identity.

### Static analysis

Ghidra, Capstone, PE/PDB/COFF parsers, metadata scanners, and database annotations produce analysis records. Analysis can be wrong or become stale after new evidence.

### Candidate source

C, C++, assembly, headers, compiler profiles, linker manifests, and generated harnesses are working implementations. They are not evidence of original source.

### Verification

Compiler, ABI, byte, instruction, dynamic, symbolic, integration, relink, image, and release reports each establish one named property in one scope.

### Project control

The target pack, project-state database, orchestrator, content store, work queue, evidence store, and project memory own durable workflow state.

### Agents and UI

AI, MCP, and the read-only web service may inspect or propose. Canonical mutation remains explicit, evidence-backed, hash-approved, and auditable.

## Supported baseline

Operate on authorized native PE32/i386 or PE32+/AMD64 targets. Conventional unpacked user-mode C/C++ is the production-pilot baseline. Treat managed CLR, kernel mode, packing, virtualization, encryption, self-modification, anti-analysis, malware-like behavior, or unknown host-execution requirements as unsupported or special scope until an isolated environment and explicit policy are supplied.

## Mandatory repository startup

Before changing toolkit code:

1. read `CHANGELOG.md`, `FEATURE_PARITY.md`, `PROJECT_MEMORY.md`, and `AGENTS.md`;
2. run the existing regression suite with unrelated pytest plugin autoload disabled;
3. inventory modules, functions, commands, schemas, Ghidra scripts, workflow states, and adapters;
4. identify compatibility obligations from the previous release;
5. state the narrow implementation objective;
6. add implementation, schema, tests, docs, feature-catalog entry, and map updates together;
7. run complete root and integrated test-suite verification;
8. clean build/cache/test artifacts before packaging.

## Mandatory target-project startup

1. verify target authorization and supported scope;
2. run `x86decomp project-check` and `x86decomp memory-verify`;
3. verify the target pack and relevant artifacts;
4. read `TARGET.md`, template blockers, acceptance policy, and active pipelines;
5. inspect function matching and functional states independently;
6. select the next narrow claim and required validator;
7. create or claim a work item;
8. make one reversible conceptual change;
9. validate, record evidence, update workflow, and append project memory.

## Target-pack workflow

Create target packs from only the artifacts actually supplied:

```bash
x86decomp target-pack-infer target.exe target-pack/ \
  --pdb target.pdb \
  --map target.map \
  --object obj/main.obj \
  --library lib/runtime.lib \
  --rebuilt-image rebuilt.exe \
  --decisions decisions.json
```

Rules:

- the primary image must be a regular native PE;
- supporting artifacts remain hash-bound;
- observations are stored separately from decisions;
- source extensions in a PDB are evidence candidates, not complete language proof;
- unknown compiler/linker facts remain `unknown`;
- `allow_host_execution` is an explicit decision, never inferred;
- verify before project generation.

```bash
x86decomp target-pack-verify target-pack/
```

## Grounded template workflow

Derive before materializing:

```bash
x86decomp template-derive target-pack/
x86decomp project-from-target target-pack/ project/
x86decomp template-materialize project/
```

A valid template can generate:

- matching/functional/hybrid source lanes;
- exact assembly fallback directories;
- validation policy;
- durable default pipeline;
- report/test/config directories;
- project helper;
- blocker and next-step records.

A template must not generate fake decompiled functions, fake original file boundaries, fake toolchain profiles, or unsupported linker decisions.

## Durable pipeline workflow

Run:

```bash
x86decomp pipeline-run project/ project/orchestration/pipelines/default.json
x86decomp pipeline-status project/ PIPELINE_ID
```

Every command stage must declare inputs, outputs, dependencies, environment, isolation, and limits. Every evidence-gate stage must name exact claims. A missing adapter or unmet claim becomes `blocked`.

Cancellation:

```bash
x86decomp pipeline-cancel project/ PIPELINE_ID --stage-id STAGE
```

Stale runner recovery:

```bash
x86decomp pipeline-recover project/ --pipeline-id PIPELINE_ID --stale-seconds 600
```

Never manually set a running job to success. A successful stage is reusable only while materialized output hashes remain valid.

## Matching-mode workflow

Matching states:

```text
not_started
  → decompiled
  → compiles
  → abi_compatible
  → instruction_similar
  → byte_matched
  → image_integrated
  → full_relink_validated
```

Minimum evidence by state:

- `decompiled`: verified function artifact and labeled source candidate;
- `compiles`: compiler report with tool/profile/source/output hashes;
- `abi_compatible`: explicit convention, stack, register, return, and preservation checks in declared scope;
- `instruction_similar`: versioned decoder/normalizer and CFG report;
- `byte_matched`: raw target/candidate bytes exact in named ranges;
- `image_integrated`: hash-gated patch or relink output passes declared integration check;
- `full_relink_validated`: target-specific linker and image gate passes.

Never promote `relocation_normalized_match` to `byte_matched`.

## Functional-mode workflow

Functional states:

```text
not_started
  → decompiled
  → compiles
  → abi_compatible
  → differentially_validated
  → symbolically_bounded
  → integration_validated
```

Requirements:

- differential harnesses declare registers, stack, memory, stubs, observations, limits, and initial state;
- symbolic reports declare instruction support, path/step/time limits, memory and alias model, outputs, truncation, and counterexamples;
- integration scenarios require explicit execution consent or an external wrapper;
- passing scenarios prove only the selected observations in the recorded environment.

## Function artifacts

Use stable IDs `pe-rva:XXXXXXXX` and directories `pe-rva_XXXXXXXX`. Preserve every discontiguous half-open body range. A complete artifact can include:

```text
function.json
ranges/*.bin
instructions.jsonl
listing.asm
references.jsonl
decompiler.c
decompiler-tree.jsonl
raw-pcode.jsonl
high-pcode.jsonl
high-pcode.txt
context.h
workflow.json
```

Validate artifacts before use. Reject traversal and symlinks.

## Ghidra workflow

Ghidra is the primary analysis engine, not the project database. Read C, token tree, raw/high P-code, symbols, references, and exact bytes. Cross-check instruction decode with Capstone.

For MCP writes:

1. list/read tools;
2. create evidence records;
3. propose one mutation with rationale and allowlist;
4. review persisted arguments and approval hash;
5. commit the exact hash;
6. re-export and validate;
7. record the change.

Do not permit silent bulk renames or type changes.

## Compiler and toolchain workflow

Register user-owned toolchains by family/version and exact executable roles. Verify hashes before every reproducible build.

Compiler reports must include:

- compiler executable hash/version;
- complete argument array;
- environment policy;
- source/profile hash;
- output hash;
- return code/stdout/stderr;
- cache key and worker identity where applicable.

Use `local_bounded` only for trusted tools. Use a digest-pinned container or external VM for stronger isolation.

## Linker reconstruction workflow

1. parse PE, MAP, COFF/bigobj, archives, auxiliary records, relocations, and COMDAT groups;
2. distinguish public-symbol order from contribution extents;
3. resolve COMDAT selection and associative closure;
4. preserve weak externals and unknown relocation evidence;
5. produce an evidence-limited placement plan;
6. generate a relink manifest;
7. run linker under a bounded worker;
8. compare sections and complete image under an explicit profile;
9. record unexplained bytes and next highest-impact mismatch.

Never fill layout gaps with invented object ownership.

## C++ recovery workflow

Treat RTTI, vtables, class hierarchies, PMD records, deleting destructors, adjustor thunks, unwind/EH metadata, TLS, and CRT initializers as separate evidence classes. Promote a class relationship only when pointer/section/count validation and independent usage evidence agree. Preserve candidate status where handler/compiler-specific semantics remain incomplete.

## Corpus workflow

Built-in reviewed cases and generated cases are source inputs. Generate deterministic cases:

```bash
x86decomp corpus-generate generated/ --cases-per-family 64 --seed 0x1234
x86decomp corpus-generated-verify generated/corpus-generation.json
```

Then create an explicit compiler manifest and run the compiler corpus builder. A generated source hash proves reproducibility of source generation, not compiler execution or semantic equivalence.

## Triple fact-check protocol

For each claim:

1. define exact subject, predicate, object, artifact version, and scope;
2. attach at least three support records;
3. verify at least three independent failure domains;
4. require at least two evidence kinds;
5. verify all file hashes;
6. attach contradictory evidence;
7. run `claim-verify`;
8. promote only if state is `verified` and wording remains narrow;
9. record memory event with evidence IDs.

Examples of potentially independent groups:

- raw bytes/PE parser;
- exact-build PDB or MAP identity;
- compiler output comparison;
- dynamic trace;
- independent decoder;
- bounded symbolic result.

Two Ghidra renderings are not automatically independent.

## Project state and recovery

Before migration:

```bash
x86decomp project-check project/
x86decomp project-migrate project/ --dry-run
x86decomp project-backup project/ backup.tar.gz
```

Then apply migration and recheck. Restore only to an empty destination. Repair and GC default to dry-run; inspect actions before `--apply`. Never repair evidence by rewriting it.

## Security workflow

Run:

```bash
x86decomp security-audit . --report reports/security/source.json
x86decomp dependency-audit --report reports/security/dependencies.json
x86decomp sbom-generate reports/security/sbom.json
x86decomp release-manifest-verify .
```

Security reports distinguish scanner availability from findings. A missing vulnerability database or adapter is not a clean scan.

## Reproducibility and release gate

Create and verify:

```bash
x86decomp reproduce-create project/ project/reports/reproducibility/manifest.json
x86decomp reproduce-verify project/ project/reports/reproducibility/manifest.json
```

Evaluate release only after reviewing target acceptance:

```bash
x86decomp release-gate project/ \
  --reproduction-manifest project/reports/reproducibility/manifest.json \
  --security-report project/reports/security/source.json \
  --convergence-report project/reports/convergence/latest.json \
  --require-workflows --require-verified-claims --require-succeeded-pipelines \
  --report project/reports/release-gate.json
```

A pass means the declared gate passed. Include the gate’s truth statement in release communication.

## Required analytical response structure

When reporting work, include:

1. **Scope** — exact target, mode, function/range, and authorization context.
2. **Observed facts** — artifact-backed facts with hashes/locations.
3. **Derived facts** — deterministic calculations and tools.
4. **Proposals** — unverified names/types/source/layout choices.
5. **Contradictions and unknowns** — explicit blockers.
6. **Validation performed** — command, environment, bounds, report path, property established.
7. **State transition** — matching and functional separately.
8. **Next highest-value action** — one evidence-grounded step.

## Repository release definition of done

A versioned release is complete only when:

- previous supported commands/features are retained or migrated with tests;
- all root and integrated test-suite tests pass with zero skips;
- every defined Python function/method body executes under coverage;
- every command is parse-tested;
- all schemas validate and representative outputs are tested;
- Ghidra Java scripts parse and live-run when Ghidra is resolved;
- wheels and source distributions build and clean-install;
- source ZIP verifies after extraction;
- test adapters are detected before prompts and missing ones are explicitly blocked;
- Mermaid and ASCII maps for toolkit and test suite are synchronized;
- README, changelogs, parity matrix, security, memory, skill, manifests, and verification record are current;
- source artifacts contain no cache, venv, downloaded adapter, machine path, build, coverage, or test-result residue;
- unavailable live integrations are disclosed.

## Final safety reminder

Static analysis is the default. A target pack, project template, imported artifact, decompiler output, or passing static validator never grants permission to execute unknown native code. Use a disposable isolated environment and explicit consent for any native execution.
