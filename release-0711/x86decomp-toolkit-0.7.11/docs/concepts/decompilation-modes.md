# Decompilation Modes

Every function in x86decomp operates under one or both decompilation modes:
**matching** (binary-identical reproduction) and **functional** (behaviorally equivalent
reproduction). A function can participate in both modes simultaneously.

## Mode Definitions

| Mode | Goal | Acceptance Criterion |
|---|---|---|
| `matching` | The compiled C source produces bytes identical to the original binary | `byte_matched` or `full_relink_validated` |
| `functional` | The compiled C source exhibits equivalent observable behavior | `differentially_validated`, `symbolically_bounded`, or `integration_validated` |

## Default Configuration

Every function workflow initializes with both modes enabled:

```json
{
  "function_id": "pe-rva:00401000",
  "selected_modes": ["functional", "matching"],
  "matching_status": "not_started",
  "functional_status": "not_started"
}
```

## Mode Selection

### Initialize with Custom Modes

```bash
x86decomp workflow-init --function rva:0x401000 --modes matching
```

This creates a workflow tracking only the matching status pipeline. The `functional_status`
field remains `not_started` but cannot be advanced because the functional mode is not selected.

### Initialize with Both Modes (Default)

```bash
x86decomp workflow-init --function rva:0x401000
```

Omitting `--modes` defaults to `["matching", "functional"]`.

!!! warning "Mode selection is immutable after initialization"
    You cannot change `selected_modes` on an existing workflow. If you need different modes,
    delete the workflow directory and re-initialize.

## Independent Status Tracking

Matching and functional progress are tracked independently. A function can be:

- `byte_matched` (matching) but `not_started` (functional) — byte-identical but untested at runtime.
- `differentially_validated` (functional) but `compiles` (matching) — behaviorally correct but
  not byte-identical (e.g., different register allocation).
- Both `byte_matched` AND `differentially_validated` — the gold standard.

```json
{
  "function_id": "pe-rva:00401500",
  "selected_modes": ["functional", "matching"],
  "matching_status": "byte_matched",
  "functional_status": "differentially_validated"
}
```

## Mode-Aware Commands

Commands that advance status check whether the target mode is enabled:

```bash
# This fails if matching mode is not selected for this function
x86decomp workflow-update --function pe-rva:00401000 --matching status=byte_matched
```

The error:

```
ContractError: matching status cannot change when matching mode is disabled
```

## Hybrid Projects

A project typically pursues both modes for different functions:

| Function Type | Strategy |
|---|---|
| Core engine functions | Full matching (byte-identical) |
| I/O, platform, glue code | Functional (behavioral equivalence) |
| UI, rendering | Functional (difficult to match due to floating-point variation) |
| Standard library shims | Matching if possible; functional fallback |

The project-level `project.json` records nothing about mode selection — modes are per-function,
stored in `functions/<function_id>/workflow.json`.

## Source Stages

Alongside matching/functional tracking, every function has a `source_stage`:

| Stage | Meaning |
|---|---|
| `original_bytes` | No C source exists yet |
| `generated_assembly` | Assembly listing produced from original bytes |
| `decompiler_candidate` | C source from an automated decompiler (e.g., Hex-Rays, Ghidra) |
| `human_candidate` | C source written or refined by a human |
| `accepted_source` | C source that passed its mode's acceptance gate |

The source stage is independent of the matching/functional status. A function can have
`accepted_source` and a matching status of `compiles` if the source compiles but doesn't
yet produce identical bytes.

## Workflow Display

```bash
x86decomp workflow-show --project . --function pe-rva:00401000
```

```json
{
  "function_id": "pe-rva:00401000",
  "selected_modes": ["functional", "matching"],
  "source_stage": "human_candidate",
  "matching_status": "compiles",
  "functional_status": "differentially_validated",
  "active_candidate": "src/matched/00401000.c",
  "compiler_profile": "config/compiler-profiles/msvc-2019-x86-release.json",
  "reports": {
    "abi_check": "reports/matching/00401000-abi.json",
    "byte_comparison": "reports/matching/00401000-byte.json"
  },
  "blockers": []
}
```

!!! tip "Check mode before running expensive validation"
    Run `x86decomp workflow-show` before `dynamic-validate` or `symbolic-validate`. If functional
    mode is disabled, those validations are wasted work.

## Workflow Initialization with RVA

The RVA-based shorthand:

```bash
x86decomp workflow-init --project ./myproject --function pe-rva:00401000
```

Is equivalent to:

```bash
x86decomp workflow-init --project ./myproject --rva 0x401000
```

Both produce the same `functions/pe-rva_00401000/workflow.json` file.

## Status Regressions

Status advancement is monotonic by default. To move backward:

```bash
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=compiles --allow-regression
```

Without `--allow-regression`, the command rejects any status that ranks lower than the
current status in the progression order.

!!! danger "Regression side effects"
    Rolling back `byte_matched` to `compiles` does not update linked artifacts or evidence
    records. You must manually re-validate claims that referenced the old status.
