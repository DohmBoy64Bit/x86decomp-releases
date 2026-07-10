---
title: Decompilation acceleration workflow
description: 0.7.11 helpers for moving from function evidence to accepted, source-organized reconstruction work.
---

# Decompilation acceleration workflow

The 0.7.11 acceleration commands remove manual glue around local-model jobs, accepted-source promotion, source-address annotations, C++ metadata scaffolding, triage, playability smoke plans, assets, and mod/regression manifests.

The commands are bounded helpers. They do not claim original source recovery, semantic proof, or successful matching unless an input validator report already proves the requested gate.

## New command families

| Family | Purpose |
| --- | --- |
| `llm job-create`, `llm job-from-range` | Materialize local-LLM job JSON from verified function evidence or explicit bytes. |
| `llm batch-create`, `llm batch-match` | Build and process job queues while recording blocked reasons. |
| `candidate promote` | Copy a validated candidate into an accepted source stage and optionally update workflow state. |
| `source-map annotate`, `source-map verify` | Preserve original address identity in human-readable source files. |
| `module assign`, `module suggest` | Maintain and propose source-module ownership without guessing original names. |
| `type propagate`, `headers synthesize-project` | Create reviewable type/header propagation plans and provisional headers. |
| `vtable recover`, `class scaffold` | Extract C++ metadata evidence and create provisional class scaffolds. |
| `diff explain` | Convert mismatch reports into diagnostic hints. |
| `triage next`, `playability smoke-plan` | Generate contributor queues and integration-test scaffolds. |
| `asset inventory`, `mod branch-init`, `regression compare` | Track game assets, intentional mod branches, and regression comparison manifests. |

## Trust boundary

These helpers are designed to speed up project movement, not to weaken verification. Model output remains untrusted. Source promotion requires an accepted validation report. Module suggestions and class scaffolds are review aids and explicitly do not claim original source names or declarations.


# v0.7.11 universal acceleration commands

These commands turn lessons from real projects into reusable, project-neutral workflows. They are bounded helpers: they emit manifests, reports, source candidates, or safe derived files; they do not claim recovered original source or validation success unless a validator report proves it.

## Function discovery and reconciliation

```powershell
x86decomp function discover target.text --profile prologue --architecture x86 --output reports\functions\discover.json
x86decomp function reconcile reports\functions\discover.json --output reports\functions\reconciled.json
x86decomp function sort reports\functions\reconciled.json --key rva --output reports\functions\sorted.json
x86decomp function classify reports\functions\sorted.json --output reports\functions\classified.json
```

The profile name is generic. `prologue` and `ret-boundary` are heuristic profiles, not MSVC-only promises.

## Pattern recipes before LLM search

```powershell
x86decomp pattern catalog --output reports\patterns\catalog.json
x86decomp pattern scan functions\ranges --output reports\patterns\scan.json
x86decomp pattern generate reports\patterns\scan.json generated\patterns
x86decomp pattern match generated\patterns\pattern-generation-report.json --output reports\patterns\triage.json
```

Generated pattern source is unaccepted until it compiles and passes matching or functional validation.

## Text-section swap workflow

```powershell
x86decomp image-text compose project\text.bin --function-list reports\functions\sorted.json
x86decomp text-swap plan original.exe project\text.bin reports\text-swap\plan.json --section-name .text
x86decomp text-swap inject reports\text-swap\plan.json --output build\text-swap.exe
x86decomp text-swap verify reports\text-swap\plan.json build\text-swap.exe --output reports\text-swap\verify.json
```

This is a container-preserving intermediate workflow. It is not a full relink claim.

## Project accounting and mod-source policy

```powershell
x86decomp project health --project project --output reports\health.json
x86decomp progress reconcile --project project --output reports\progress.json
x86decomp source-stage classify --project project --output reports\source-stage.json
x86decomp release-policy moddable-source --project project --output reports\moddable-source.json
```

The source-stage policy distinguishes assembly fallbacks, byte wrappers, generated candidates, and human-reviewed source so byte-preserving wrappers do not masquerade as mod-ready decompilation.

## GhidraMCP and hygiene helpers

```powershell
x86decomp ghidra-mcp probe http://127.0.0.1:8080
x86decomp ghidra-mcp functions http://127.0.0.1:8080 --output reports\ghidra-mcp\functions.json
x86decomp ghidra-mcp decompile http://127.0.0.1:8080 0x401000 --output reports\ghidra-mcp\401000.json
x86decomp project doctor-paths . --project project --output reports\paths.json
x86decomp script-port audit scripts --output reports\script-port.json
```

MCP responses are captured as external observations. They are not trusted source.

## Runtime, subsystem, and toolchain helpers

```powershell
x86decomp runtime-analysis identify --project project --output reports\runtime.json
x86decomp subsystem detect project --output reports\subsystems.json
x86decomp game-pattern state-machine project --output reports\state-machines.json
x86decomp toolchain hash-tree tools\local-msvc reports\toolchain-hashes.json
x86decomp toolchain verify-local reports\toolchain-hashes.json
x86decomp toolchain redact-package tools\local-msvc release\toolchain-redacted --manifest reports\toolchain-hashes.json
```

Toolchain packaging records hashes and instructions; it intentionally does not claim redistribution rights for proprietary compilers.
