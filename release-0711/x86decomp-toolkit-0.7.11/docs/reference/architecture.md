# Architecture

The toolkit has one CLI plane and four capability packages layered over shared project,
evidence, workflow, and adapter services.

## Command plane

`x86decomp.cli` registers **166 root commands** and dispatches through the canonical
capability router. `x86decomp.canonical` exposes **59 groups** and **239 routes**.

## Capability packages

| Package | Responsibility |
|---|---|
| `x86decomp.governance` | Hypotheses, campaigns, reviews, proofs, workers, consensus, audit evidence |
| `x86decomp.reconstruction` | Modules, translation units, headers, builds, ABI contracts, provenance, libraries, generated tests, capsules, semantic changesets |
| `x86decomp.native` | PE boundaries, function slots, matching, patch planning, hybrid composition, staging context, closed loops, runtime checks, Windows tools |
| `x86decomp.assembly` | Byte, annotated, and mnemonic materialization plus relocation resolution and round-trip evidence |

## Root modules

Root modules provide binary parsing, compilation, diffing, orchestration, symbolic and
dynamic validation, project state, security, and reproducibility.

## Local LLM

`x86decomp.local_llm` provides bounded local-model profiles, deterministic prompt
construction, untrusted C proposal parsing, and a closed compiler/COFF/relocation/byte-identity
loop. It cannot promote workflow state or accept its own output.

!!! warning "LLM output is never authoritative"
    Local-model output remains an untrusted proposal until the deterministic compiler,
    relocation, and exact-byte gates pass.

## Test kit

`x86decomp_testkit` recursively inventories and verifies the complete current surface,
including optional local-inference runtime adapters.

## v0.7.11 acceleration layer

The v0.7.11 reconstruction layer adds command families for:

* LLM job creation, batch matching, and candidate promotion
* Source-map annotations and module assignment
* Type/header propagation plans
* C++ vtable/class scaffolding
* Diff explanation and triage
* Playability smoke-plan scaffolds and asset inventory
* Mod branch manifests and regression comparison manifests

These commands sit above the existing validators: they organize work and materialize
reviewable manifests, but they do not replace compiler, relocation, byte-match, ABI,
symbolic, dynamic, integration, or release gates.

## Plan-only command contract

The action-named reconstruction routes `candidate search`, `type propagate`, and
`triage next` are intentionally conservative planning commands. They emit JSON plans
with explicit claims such as `ordered_candidate_search_plan_only`,
`plan_only_no_silent_overwrite`, or `planning_only`; they do not promote candidates,
edit source files, or mutate workflow state.

!!! note
    Downstream scripts must treat plan-only outputs as reviewable proposals until a
    separate evidence gate accepts them.
