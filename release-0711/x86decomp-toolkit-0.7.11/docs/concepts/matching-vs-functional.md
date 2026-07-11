# Matching vs Functional

Every function advances through one or both status pipelines. Matching tracks byte-level
identity with the original binary. Functional tracks behavioral equivalence. The two
pipelines are independent — progress in one does not imply progress in the other.

## Matching Status Pipeline

The matching pipeline asks: "Does the compiled source produce bytes identical to the original?"

| Status | Requirement | Verification |
|---|---|---|
| `not_started` | No matching work has begun | — |
| `decompiled` | C source exists for the function | Human review of candidate |
| `compiles` | Source compiles without error under the target compiler profile | `compile` command succeeds |
| `abi_compatible` | Compiled code follows the declared ABI contract | `abi-check` passes |
| `instruction_similar` | Disassembly of compiled code is structurally similar to original | `diff-function` or `objdiff-run` shows high similarity |
| `byte_matched` | Compiled object bytes are identical to original after relocation resolution | `diff-bytes` returns `equal: true` |
| `image_integrated` | Compilation unit is linked into a PE image as a replacement | `patch-image` succeeds |
| `full_relink_validated` | Complete PE is reconstructed and byte-identical | `relink` produces hash-matching image |
| `blocked` | Progress is halted by an unresolved issue | Blocker listed in workflow |

### Advancing Matching Status

```bash
# Initialize
x86decomp workflow-init --project . --rva 0x401000 --modes matching

# After writing C source
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=decompiled

# After successful compilation
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=compiles \
  --active-candidate src/matched/00401000.c \
  --compiler-profile config/compiler-profiles/msvc-2019-x86.json

# After ABI check passes
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=abi_compatible \
  --report-kind abi_check --report-path reports/matching/00401000-abi.json

# After byte comparison succeeds
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=byte_matched \
  --report-kind byte_match --report-path reports/matching/00401000-byte.json

# Record a blocker
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=blocked \
  --blocker "Compiler generates extra push/pop in debug mode"
```

## Functional Status Pipeline

The functional pipeline asks: "Does the compiled source behave identically?"

| Status | Requirement | Verification |
|---|---|---|
| `not_started` | No functional work has begun | — |
| `decompiled` | C source exists for the function | Human review |
| `compiles` | Source compiles without error | `compile` succeeds |
| `abi_compatible` | Compiled code follows the declared ABI contract | `abi-check` passes |
| `differentially_validated` | Compiled and original functions produce identical output for test inputs | `dynamic-validate` passes |
| `symbolically_bounded` | Symbolic execution validates equivalence within bounded input space | `symbolic-validate` or `angr-validate` passes |
| `integration_validated` | Function behaves correctly within the full linked image | Integration scenarios pass |
| `blocked` | Progress is halted by an unresolved issue | Blocker listed in workflow |

### Advancing Functional Status

```bash
# After differential validation
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --functional status=differentially_validated \
  --report-kind dynamic_validate --report-path reports/functional/00401000-dynamic.json

# After symbolic validation
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --functional status=symbolically_bounded \
  --report-kind symbolic_validate --report-path reports/functional/00401000-symbolic.json
```

## When to Use Each Mode

!!! tip "Matching is for preservation"
    Use matching when you need to prove that every byte of the original binary can be
    reproduced from source. This is the standard for archival decompilation projects
    (SM64, Ocarina of Time, etc.).

!!! tip "Functional is for portability"
    Use functional when the goal is a working native port, not archival byte-perfect
    reproduction. Acceptable for platform shims, rendering code, and I/O.

### Scenario: Core Math Function

A `sqrt_approx` function at `0x401000`:

- **Matching target**: You have the original MSVC 2019 compiler, the source is straightforward
  C math with no platform dependencies, and you want byte-level proof.
- **Approach**: Matching mode only. Chase `full_relink_validated`.
- **Effort**: High — every codegen difference must be resolved.

### Scenario: DirectX Wrapper

A `CreateDevice` wrapper at `0x402000`:

- **Functional target**: The function calls external DirectX APIs. Byte-matching is impractical
  because the API surface is version-dependent.
- **Approach**: Functional mode only. Chase `differentially_validated`.
- **Effort**: Moderate — write equivalent logic, validate with test inputs.

### Scenario: Hot-Loop String Parser

A `ParseConfig` function at `0x403000`:

- **Both targets**: The function has no external dependencies, is performance-critical, and you
  want both byte-matching AND behavioral validation.
- **Approach**: Both modes. Matching first (byte-identical proves correctness implicitly), then
  functional validation as a double-check.
- **Effort**: Highest — must satisfy both gates.

## Checking Convergence

Functions that reach high status in both modes are considered converged:

```bash
x86decomp convergence-analyze --project .
```

This produces a report showing how many functions are at each status level in each mode,
plus a "converged" count for functions that are byte_matched + (differentially_validated or
symbolically_bounded).

## Blockers

When a function hits an obstacle, record it as a blocker:

```bash
x86decomp workflow-update --project . --function pe-rva:00401000 \
  --matching status=blocked \
  --blocker "MSVC 2019 19.29.30133 required; only 19.29.30136 available"
```

Blockers are additive — they accumulate in the workflow. There is no command to remove a
blocker; you update the status to a non-blocked value to clear the blocker list.

!!! note
    The `blocked` status is terminal until manually cleared. Functions blocked in matching
    mode can still advance in functional mode, and vice versa.

## Encoded Ordering

The status values have a strict ordinal ordering used for regression checks:

```python
_MATCHING_ORDER = {
    "not_started": 0, "decompiled": 1, "compiles": 2,
    "abi_compatible": 3, "instruction_similar": 4, "byte_matched": 5,
    "image_integrated": 6, "full_relink_validated": 7,
    "blocked": -1,
}
_FUNCTIONAL_ORDER = {
    "not_started": 0, "decompiled": 1, "compiles": 2,
    "abi_compatible": 3, "differentially_validated": 4,
    "symbolically_bounded": 5, "integration_validated": 6,
    "blocked": -1,
}
```

`blocked` is always -1 (outside the normal ordering) — you can go from `blocked` to any
other status without `--allow-regression`.

## Report Attachments

Each status advancement can attach a named report:

| Status | Typical Report Kind | Example Path |
|---|---|---|
| `compiles` | `compile_report` | `build/compiler/00401000-compile.json` |
| `abi_compatible` | `abi_check` | `reports/matching/00401000-abi.json` |
| `byte_matched` | `byte_match` | `reports/matching/00401000-byte.json` |
| `differentially_validated` | `dynamic_validate` | `reports/functional/00401000-dynamic.json` |
| `symbolically_bounded` | `symbolic_validate` | `reports/functional/00401000-symbolic.json` |
| `full_relink_validated` | `relink_report` | `reports/convergence/relink.json` |

Reports are stored as key-value pairs in the workflow's `reports` dict.
