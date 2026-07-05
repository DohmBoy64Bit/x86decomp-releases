---
name: x86decomp-evidence-engineer
description: Evidence-first operation of the unified x86decomp-toolkit 0.7.9 release.
version: 7.5.0
license: Apache-2.0
compatibility: Python 3.11+, x86decomp-toolkit 0.7.9, native PE32/i386 and PE32+/AMD64, optional bounded validation adapters
metadata:
  release_contract: 0.7.9
  unified_release: true
  toolkit_entry_point: x86decomp
  test_suite_entry_point: x86decomp-test
  modes:
    - matching
    - functional
  architectures:
    - x86
    - x86_64
  evidence_policy: three-independent-source-gate
  execution_policy: static-by-default-explicit-consent-for-native-execution
  project_schema: 3
  governance_extension_schema: 4
  reconstruction_extension_schema: 5
  native_extension_schema: 6
  assembly_extension_schema: 7
  canonical_group_count: 59
  canonical_route_count: 239
  source_tree_upgrade_subsystem: false
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

## Interface

Use only the unified executables:

```text
x86decomp commands
x86decomp <capability-group> <action> ...
x86decomp-test <action> ...
```

The toolkit exposes 59 canonical capability groups and 239 routes. Do not create release-numbered modules, executables, command bridges, installers, overlays, reports, catalogs, or tests.

## Non-negotiable rules

1. Never claim original source, names, comments, macros, or translation units without authenticated evidence.
2. Keep observations, deterministic derivations, proposals, analyst decisions, and verified claims distinct.
3. Never treat adapter majority, AI output, byte similarity, or finite testing as universal proof.
4. Never hide contradictions, unknowns, missing adapters, unsupported instructions, timeouts, or blocked integrations.
5. Require explicit authorization and bounded isolation before native execution.
6. Never create placeholders, fake adapters, TODO branches, empty success paths, or fabricated reports.
7. Preserve current functionality unless a complete tested successor supersedes it.
8. Keep byte-form assembly as the conservative default. Annotated and mnemonic forms require explicit selection and exact evidence.
9. Keep code, tests, schemas, examples, catalog, docs, skill, and all four architecture artifacts synchronized.
10. A release must pass exact inventory, zero-skip tests, function-body coverage, command probes, package checks, archive checks, and SHA-256 verification.
11. Treat local-model output as an untrusted proposal. Only deterministic compilation, COFF extraction, complete relocation resolution, and exact target-byte identity may establish an LLM-loop byte match.
12. Keep the MkDocs Material documentation source and built site synchronized with the release parser, schemas, adapters, examples, tests, manifests, and architecture artifacts.

## Evidence vocabulary

- **Observed:** directly present in bytes, files, tool output, or runtime traces.
- **Derived:** calculated deterministically from observations.
- **Proposed:** a useful interpretation not yet accepted.
- **Corroborated:** supported by multiple independent records below the acceptance gate.
- **Accepted:** passed the declared governance gate.
- **Verified:** passed the named verifier for the exact scoped property.
- **Behaviorally tested:** finite declared inputs or scenarios agreed.
- **Symbolically proved:** the declared bounded model was discharged.
- **Byte identical:** exact bytes agree under the declared range and policy.
- **Rejected:** contradicted for the scoped artifact.
- **Blocked:** a declared dependency or authorization was unavailable.
- **Unknown:** evidence or implemented semantics are insufficient.

## Workflow

1. Hash and inventory inputs before interpretation.
2. Define whether the goal is matching, functional validation, reconstruction, or evidence organization.
3. Initialize or verify project state and audit integrity.
4. Record hypotheses and assumptions explicitly.
5. Generate candidate source or assembly without promoting it to fact. For local-model generation, preserve the exact prompt, raw response, normalized candidate, provider profile, and attempt history.
6. Compile with recorded toolchain identities and exact arguments. Resolve every relocation from explicit evidence before comparing candidate bytes.
7. Compare using the declared byte, structural, dynamic, symbolic, or integration verifier.
8. Preserve counterexamples and contradictions.
9. Accept only the narrow property actually verified.
10. Export deterministic evidence and reproduce it in a clean environment.
