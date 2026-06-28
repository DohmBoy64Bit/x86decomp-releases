---
name: x86decomp-evidence-engineer
description: Evidence-first workflow for native Windows PE32/x86 decompilation projects using Ghidra, compiler experiments, function artifacts, and explicit verification states.
version: 1.0.0
license: Apache-2.0
compatibility: Python 3.11+, Ghidra 12.1 baseline, native PE32 i386 targets
tags:
  - reverse-engineering
  - decompilation
  - x86
  - pe32
  - ghidra
  - evidence
---

# x86decomp evidence engineer

## Purpose

Use this skill to create, inspect, and advance an x86decomp-toolkit project while
preserving a strict boundary between observations, inferences, source candidates, and
verified properties.

The objective is not to claim automatic recovery of original source. The objective is
to produce a reproducible project in which every important assertion has provenance,
every source candidate is testable, and every status means one narrowly defined thing.

## Supported operating scope

Operate within all of these constraints unless the project contract has been formally
extended:

- Native Windows PE32.
- IMAGE_FILE_MACHINE_I386.
- Conventional user-mode C or C++.
- Unpacked and statically analyzable code.
- Function-oriented incremental work.
- Authorized binaries only.

Stop and report `unsupported_scope` when the input is PE32+, managed CLR, a non-i386
machine, packed/virtualized, kernel-mode, intentionally self-modifying, or requires
executing unknown code on the host.

## Non-negotiable truth rules

1. Never say “original source” unless an exact source artifact from the same build is
   independently authenticated.
2. Never say “original name” because a proposed name is semantically plausible.
3. Never promote a Ghidra type, decompiler signature, or AI suggestion directly to
   fact.
4. Never treat absence from a static reference database as proof that runtime access
   cannot occur.
5. Never call byte similarity semantic equivalence.
6. Never call finite differential tests a universal proof.
7. Never claim three-source verification guarantees truth. It is a governance gate
   designed to reduce correlated errors.
8. Never hide a failure, timeout, unsupported format, parser bound error, compiler
   diagnostic, or contradictory evidence.
9. Never create a fake implementation, empty adapter, TODO branch, placeholder return,
   or success response for an unimplemented subsystem.
10. Never execute the target binary outside an explicitly documented isolated dynamic
    analysis environment.

## Required vocabulary

Use these terms precisely:

- **Observed:** directly present in a captured artifact, byte sequence, tool output, or
  runtime trace.
- **Derived:** deterministically calculated from observed data.
- **Proposed:** a working interpretation that may be useful but is not verified.
- **Corroborated:** supported by at least two records but below the verification gate.
- **Verified:** passed the project verification gate for the exact claim stated.
- **Rejected:** contradicted or falsified for the tested artifact/version.
- **Unknown:** insufficient evidence.

Avoid vague terms such as “basically matched,” “probably exact,” “fully recovered,” or
“confirmed” without naming the exact verification property.

## Separation of concerns

Keep these layers distinct.

### Immutable evidence layer

Contains target bytes, hashes, imported symbols, debug records, captured compiler
outputs, traces, and external documents. Do not edit evidence in place. Create a new
record when an artifact changes.

### Analysis layer

Contains Ghidra functions, P-code, references, decompiler output, Capstone decoding,
and analyst annotations. Analysis may be wrong or change after reanalysis.

### Candidate source layer

Contains C, C++, assembly, headers, compiler profiles, and build scripts. Candidate
source is an attempted implementation, not evidence of original source.

### Verification layer

Contains compiler reports, byte comparisons, ABI checks, differential tests, bounded
symbolic checks, and integration results. Each verifier reports only its defined
property.

### Project-memory layer

Contains durable decisions, hypotheses, blockers, tool changes, and status transitions
in an append-only hash chain. Memory references evidence; it does not replace evidence.

### Agent layer

May propose names, types, source, experiments, and tests. Agent output is always a
proposal until an independent verifier or evidence gate promotes the specific claim.

## Mandatory startup sequence

For any new task:

1. Read `project.json`.
2. Run `x86decomp verify-project <project>`.
3. Run `x86decomp memory-verify <project>`.
4. Read the generated `memory/PROJECT_MEMORY.md`.
5. Identify the exact stable IDs affected.
6. Inspect current function artifacts and integrity reports.
7. State the requested outcome as a measurable property.
8. Select the smallest workflow that can test that property.

Do not mutate Ghidra or candidate source before project integrity is valid.

## Stable identity rules

- Function IDs use `pe-rva:XXXXXXXX`.
- Directory form uses `pe-rva_XXXXXXXX`.
- RVA is unsigned and image-relative.
- Body ranges are sorted, non-overlapping, and half-open.
- A Ghidra address string is provenance/display, not the cross-build key.
- A function body may contain multiple discontiguous ranges.
- Never fabricate one enclosing byte interval as the function body.

## Triple fact-check protocol

A claim may reach `verified` only when all checks pass.

### Check A — evidence count

At least three evidence records support the same narrowly worded claim.

### Check B — independence

At least three independent groups are represented. Independence means different
failure domains, not different files. Examples:

- raw binary decoding;
- a Ghidra analysis database;
- independent Capstone/Zydis decoding;
- compiler output;
- a matching PDB tied by GUID/age;
- a runtime trace from an isolated run;
- authoritative format documentation.

Two scripts reading the same Ghidra program are normally one group. Two LLM summaries
of the same decompiler text are one group. Two compiler runs using identical source,
flags, and compiler build are one group unless the claim specifically concerns run
reproducibility.

### Check C — evidence diversity

At least two evidence kinds must be present. Three static-analysis reports are not
enough even when produced by separate tools.

### Check D — integrity

All file-backed evidence hashes must still match.

### Check E — contradiction handling

No unresolved contradiction evidence may remain attached. Contradiction does not get
ignored because supporting evidence is more numerous. Resolve the scope, version,
input, or interpretation first.

### Check F — exact claim wording

Verify only the narrow property tested. Examples:

- Good: `pe-rva:00012340 has callee stack cleanup of 8 bytes`.
- Bad: `pe-rva:00012340 is definitely __stdcall and fully understood`.
- Good: `candidate bytes equal target range 0 for compiler profile X`.
- Bad: `function is completely matched` when other ranges or relocations were not checked.

## Claim workflow

1. Capture evidence with `x86decomp evidence-add`.
2. Create the claim with `x86decomp claim-create`.
3. Attach evidence with `x86decomp claim-attach`.
4. Attach contradictions with `x86decomp claim-contradict`.
5. Run `x86decomp claim-verify`.
6. Read the failure list.
7. Promote downstream state only when the exact required claim is `verified`.
8. Record the transition in project memory with evidence IDs.

## Function workflow

Use this state machine:

```text
unexplored
  -> exported
  -> candidate
  -> compiles
  -> abi_checked
  -> instruction_similar
  -> byte_matched
```

Additional orthogonal states:

```text
differentially_tested
bounded_symbolic_check
integration_tested
```

### `unexplored`

No reliable per-function artifact exists.

### `exported`

Function manifest, exact body range bytes, instruction records, references, and
analysis outputs exist and pass artifact integrity.

### `candidate`

A source implementation exists. Record its source and generator. AI-generated source
must be labeled proposed.

### `compiles`

A named compiler profile produced the expected output artifact. Preserve the compiler
report. This state says nothing about behavior or matching.

### `abi_checked`

Calling convention, parameter locations, return behavior, stack delta, and relevant
register preservation have explicit checks. Each component may remain unknown.

### `instruction_similar`

A versioned normalizer compared decoded instructions and references. Preserve the
normalization policy and report. Do not use raw sequence similarity as this state.

### `byte_matched`

All target ranges in scope are byte-identical under the recorded extraction policy.
If relocations are excluded or normalized, name that explicitly; do not use plain
`byte_matched` for a weaker property.

## Ghidra read workflow

Prefer the bundled read-only scripts or read-only ghidra-mcp operations.

For a function:

1. Read `function.json`.
2. Read exact range bytes.
3. Read `instructions.jsonl`.
4. Read `references.jsonl`.
5. Read `decompiler.c` as a candidate representation.
6. Read `high-pcode.txt` for data-flow questions.
7. Query callers and target references where required.
8. Cross-check suspicious decoding with an independent decoder.

Do not reason solely from decompiler C when raw instructions or references answer the
question more directly.

## Ghidra mutation workflow

Default to no mutation.

Before a rename, prototype change, structure creation, comment, or data definition:

1. Export the affected artifact.
2. Record proposed claims and evidence.
3. Write a reversible change plan.
4. Use one transaction for one conceptual change.
5. Avoid mass changes from generated lists.
6. Re-run only the necessary analysis.
7. Re-export affected artifacts.
8. Compare before/after manifests.
9. Run downstream compiler or verification checks.
10. Record the change and rollback route in memory.

When using ghidra-mcp, do not count its write response as independent evidence that the
new type or name is correct.

## Naming policy

Names have provenance:

- `DEFAULT`: generated by Ghidra or importer.
- `IMPORTED`: from export/import metadata.
- `DEBUG`: from authenticated debug information.
- `ANALYST_DESCRIPTIVE`: useful human name, not claimed original.
- `AI_PROPOSED`: generated suggestion awaiting review.
- `ORIGINAL_VERIFIED`: reserved for authenticated same-build evidence.

Use semantic descriptive names freely when helpful, but record that they are analyst
or AI names. Never erase the stable function ID.

## Type policy

Track type properties independently:

- width;
- signedness;
- pointer versus integer;
- pointee type;
- constness;
- aggregate layout;
- field offsets;
- calling convention;
- parameter storage;
- return storage.

A verified width does not verify signedness. A verified field offset does not verify
the original field name. A vtable-like call does not alone verify a complete C++ class.

## Compiler experiment workflow

1. Select an explicit profile.
2. Confirm the executable path and version.
3. Hash the source.
4. Run through `x86decomp compile`; never construct an unrecorded shell command.
5. Preserve stdout and stderr.
6. Confirm output kind before comparison.
7. Extract the intended function or section using a versioned method.
8. Compare exact bytes and/or normalized instructions as separate reports.
9. Modify one source/compiler variable per experiment when identifying causality.
10. Record successful and failed experiments when they affect future strategy.

A historical proprietary compiler must be user-supplied and legally available. Do not
bundle it.

## Byte comparison rules

The bundled comparator answers only whether two supplied byte strings are equal.

- `equal=true` means identical length and content.
- Similarity is diagnostic.
- Mismatch truncation must be disclosed.
- File extraction boundaries must be recorded.
- Comparing a full COFF object to function bytes is invalid.
- Comparing linked PE bytes to compiler bytes without handling references/relocations
  may produce expected mismatches; do not “normalize” them ad hoc.

## objdiff integration policy

objdiff is designed around relocatable object comparisons. Use it when both sides are
appropriate object files and the project configuration accurately identifies units and
symbols. Do not present objdiff as direct proof against an arbitrary linked PE unless a
separate, documented target-object reconstruction pipeline produced the target object.

Capture:

- objdiff version;
- configuration revision;
- target and candidate hashes;
- selected symbol/unit;
- architecture backend;
- complete report.

## decomp.me policy

Use local per-function packets as the default integration. Before uploading anything:

- confirm operator authorization;
- inspect whether target assembly or context contains proprietary material;
- confirm service/privacy policy appropriate for the project;
- minimize the submitted fragment;
- record the upload decision.

Do not automate public upload in a default workflow.

## Capstone policy

Capstone is an independent decoder, not a decompiler or equivalence prover. Use it for:

- independent instruction boundaries;
- mnemonic/operand extraction;
- direct branch targets;
- display and indexing;
- cross-checking Ghidra.

Record architecture, mode, syntax, version, input bytes, and start address. Incorrect
mode or address produces misleading output.

## Dynamic validation policy

Dynamic validation requires an isolation plan. Before execution record:

- exact target hash;
- VM/container image;
- snapshot identifier;
- network state;
- input corpus;
- environment variables;
- filesystem mounts;
- timeout;
- trace instrumentation;
- expected cleanup/reset.

Dynamic results are observations for the executed paths and inputs only.

## Symbolic validation policy

Use symbolic or concolic execution for bounded functions with explicit state models.
Record:

- architecture semantics;
- memory model;
- unconstrained inputs;
- path bounds;
- loop bounds;
- external-call summaries;
- solver timeout;
- satisfiable counterexamples.

A timeout or path explosion is `unknown`, not success.

## Project memory workflow

Append memory after durable events, not every trivial command.

Required durable events:

- project initialization;
- architecture decisions;
- compiler-profile discoveries;
- function state promotions or reversions;
- accepted/rejected ABI or type claims;
- discovered packer/self-modification/exception complexity;
- tool version change affecting output;
- legal/security constraints;
- blocker creation and resolution.

A memory event should include stable IDs, old/new state, evidence IDs, exact result,
and rollback information. Verify the hash chain before appending.

## Context and efficiency optimization

To minimize irrelevant context without sacrificing evidence:

1. Work one function or one tightly connected call cluster at a time.
2. Load the manifest before large text outputs.
3. Prefer structured JSONL filters over full decompiler dumps.
4. Read only referenced ranges and callers needed for the claim.
5. Reuse stable IDs in notes and commands.
6. Summarize prior experiments in memory, linking reports rather than pasting them.
7. Generate compiler matrices programmatically but inspect only changed outcomes.
8. Keep raw evidence immutable and derive compact indexes.
9. Separate display artifacts from machine contracts.
10. Stop an experiment branch when its falsifying evidence is conclusive.

Optimization must never remove provenance, failure output, hashes, or contradiction
records.

## Required response structure for analytical work

When reporting a result, use this order:

1. **Finding:** narrow statement.
2. **Status:** observed, proposed, corroborated, verified, rejected, or unknown.
3. **Evidence:** stable evidence IDs and relevant artifact locations.
4. **Checks performed:** commands/reports and exact measured properties.
5. **Contradictions/limitations:** anything unresolved.
6. **Project changes:** files, Ghidra mutations, source changes, or state transitions.
7. **Next highest-value experiment:** one concrete action only when needed.

Do not bury uncertainty after a confident headline.

## Failure and escalation rules

Stop and report rather than improvise when:

- project integrity fails;
- memory hash chain fails;
- function body ranges overlap unexpectedly;
- binary hash differs from all recorded artifacts;
- Ghidra and independent decoding disagree on instruction boundaries;
- a compiler profile invokes an unexpected executable;
- evidence files changed after verification;
- contradiction evidence exists;
- target execution would be required without isolation;
- legal authorization is unclear;
- the requested claim exceeds implemented verifier capability.

Escalation report must name the failed contract, affected stable IDs, artifacts needed
to resolve it, and whether existing conclusions are invalidated.

## Definition of done

A task is done only when:

- the requested measurable property has been checked;
- all commands and artifacts are preserved;
- relevant integrity checks pass;
- no unsupported fact is promoted;
- contradictions are stated;
- project memory is updated for durable changes;
- tests pass for modified toolkit code;
- documentation and schemas match behavior;
- unsupported follow-on work is clearly separated from implemented capability.

## Command reference

### Initialize and audit

```bash
x86decomp init program.exe projects/program
x86decomp verify-project projects/program
x86decomp memory-verify projects/program
```

### Export Ghidra artifacts

```bash
x86decomp ghidra-export \
  program.exe \
  projects/program/analysis/ghidra \
  program \
  projects/program/analysis/exports \
  --scripts-dir ghidra_scripts \
  --overwrite
```

### Compile candidate

```bash
x86decomp compile profile.json candidate.c candidate.o --report compile.json
```

### Compare bytes

```bash
x86decomp diff-bytes target.bin candidate.bin --report diff.json
```

### Record memory

```bash
x86decomp memory-add projects/program \
  --actor analyst \
  --category function \
  --summary "pe-rva:00012340 candidate compiles under profile msvc-x" \
  --details-json '{"old_state":"candidate","new_state":"compiles","report":"reports/compile.json"}' \
  --evidence ev-compiler-report
```

## Final safety reminder

This skill improves rigor and reproducibility. It does not make decompilation fully
automatic, guarantee factual correctness, or eliminate the need for expert review.
Whenever the tool cannot measure a property, label it unknown and design the next
experiment instead of filling the gap with a plausible story.
