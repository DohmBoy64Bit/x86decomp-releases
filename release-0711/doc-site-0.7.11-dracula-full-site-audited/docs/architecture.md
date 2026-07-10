---
title: Architecture
description: Architecture overview for x86decomp 0.7.11.
---

# Architecture — 0.7.11

The toolkit has one current command plane and four capability packages layered over shared project, evidence, workflow, and adapter services.

1. `x86decomp.cli` registers core commands and the canonical capability router.
2. `x86decomp.canonical` exposes 59 groups and 239 routes.
3. `x86decomp.governance` manages hypotheses, campaigns, reviews, proofs, workers, consensus, and audit evidence.
4. `x86decomp.reconstruction` manages modules, translation units, headers, builds, ABI contracts, provenance, libraries, generated tests, capsules, and semantic changesets.
5. `x86decomp.native` manages PE boundaries, function slots, matching, patch planning, hybrid composition, staging context, closed loops, runtime checks, and Windows tools.
6. `x86decomp.assembly` manages byte, annotated, and mnemonic materialization plus relocation resolution and round-trip evidence.
7. `x86decomp.local_llm` provides bounded local-model profiles, deterministic prompt construction, untrusted C proposal parsing, and a closed compiler/COFF/relocation/byte-identity loop. It cannot promote workflow state or accept its own output.
8. Root modules provide binary parsing, compilation, diffing, orchestration, symbolic and dynamic validation, project state, security, and reproducibility.
9. `x86decomp_testkit` recursively inventories and verifies the complete current surface, including optional local-inference runtime adapters.

The active repository contains no source-tree release migration plane.

## v0.7.11 acceleration layer

The v0.7.11 reconstruction layer adds command families for LLM job creation, batch matching, candidate promotion, source-map annotations, module assignment, type/header propagation plans, C++ vtable/class scaffolding, diff explanation, triage, playability smoke-plan scaffolds, asset inventory, mod branch manifests, and regression comparison manifests. These commands sit above the existing validators: they organize work and materialize reviewable manifests, but they do not replace compiler, relocation, byte-match, ABI, symbolic, dynamic, integration, or release gates.

## Plan-only command contract clarification

The action-named reconstruction routes `candidate search`, `type propagate`, and `triage next` are intentionally conservative planning commands. They emit JSON plans with explicit claims such as `ordered_candidate_search_plan_only`, `plan_only_no_silent_overwrite`, or `planning_only`; they do not promote candidates, edit source files, or mutate workflow state. Downstream scripts must treat those outputs as reviewable proposals until a separate evidence gate accepts them.
