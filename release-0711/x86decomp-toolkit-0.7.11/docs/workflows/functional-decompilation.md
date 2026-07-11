# Functional Decompilation

**Velocity Point** — A fictional arcade-style racing game compiled for x86 Windows PE. The game
makes heavy use of floating-point physics and SIMD instructions, making exact byte-matching
impractical. The team pursues functional decompilation: behaviorally equivalent C source verified
through dynamic, symbolic, and integration testing.

---

## Scenario

> Velocity Point shipped in 2003 as `velocity.exe`. Early compiler lab experiments confirm the
> original compiler was MSVC .NET 2003, but the physics, collision, and rendering functions use
> x87 floating-point and SSE intrinsics whose register allocation resists byte-identical
> reproduction. The team decides to pursue functional decompilation — behavioral equivalence
> verified through Unicorn dynamic validation, Z3 symbolic comparison, and end-to-end integration
> testing against recorded game replays.

## What you will accomplish

1. Initialize the project and export Ghidra artifacts
2. Import function artifacts into the project
3. Create ABI contracts and generate execution harnesses
4. Dynamically validate candidate functions against the original
5. Symbolically validate floating-point equivalence
6. Run integration scenarios against recorded game inputs
7. Track per-function workflow state with evidence and claims
8. Verify claims through the evidence gate

## Prerequisites

- x86decomp 0.7.11 installed with optional dependencies:
  ```
  pip install x86decomp-toolkit[dynamic,symbolic]
  ```
- The target binary `games/velocity/velocity.exe` (x86 PE)
- A functional decompilation project with candidate C sources
- Harness templates and integration scenarios prepared

## Starting file structure

```
games/velocity/
  velocity.exe                # The target PE (x86, ~2.5 MB)
  replays/                    # Recorded game replay files for integration testing
    replay_001.dat
    replay_002.dat

projects/velocity-decomp/     # Empty directory for the project
```

---

## Step 1: Initialize the project

```console
$ x86decomp init games/velocity/velocity.exe projects/velocity-decomp/
```

**Explanation:** `init` parses the PE, copies it into `projects/velocity-decomp/original/`,
creates the full project layout, and initializes all SQLite databases and the content store.

**Verification:**

```console
$ x86decomp verify-project projects/velocity-decomp/
```

Should produce `"valid": true, "failures": []`.

---

## Step 2: Export Ghidra function artifacts

```console
$ x86decomp ghidra-export games/velocity/velocity.exe \
    ghidra-workspace/ velocity-functions/ \
    functions-export/ \
    --ghidra-home /opt/ghidra \
    --selector all \
    --overwrite \
    --report projects/velocity-decomp/reports/ghidra-export.json
```

**Explanation:** `ghidra-export` runs the headless Ghidra export for every recognized function.
The `--scripts-dir` defaults to `ghidra_scripts`. `--selector all` exports every function.
`--overwrite` replaces any existing export output.

---

## Step 3: Import function artifacts into the project

```console
$ x86decomp artifact-import projects/velocity-decomp/ functions-export/
```

**Explanation:** `artifact-import` reads the export manifest and copies verified artifacts into
`projects/velocity-decomp/functions/`. Each artifact is re-verified on import.

**Verify an individual artifact:**

```console
$ x86decomp artifact-verify projects/velocity-decomp/functions/sub_401000/
```

---

## Step 4: Create ABI contracts

Create `projects/velocity-decomp/config/abi/PhysicsTick-401000.json`:

```json
{
  "architecture": "x86",
  "convention": "stdcall",
  "stack_argument_bytes": 4,
  "callee_stack_cleanup": 4,
  "variadic": false,
  "this_register": null,
  "register_arguments": [],
  "return_registers": ["eax"],
  "structure_return": false,
  "floating_point": "x87"
}
```

This contract declares that `PhysicsTick` is a `stdcall` function taking one 4-byte stack
argument and using x87 floating-point (critical for accurate harness emulation).

Create `projects/velocity-decomp/config/abi/CollisionCheck-401200.json`:

```json
{
  "architecture": "x86",
  "convention": "fastcall",
  "stack_argument_bytes": 0,
  "callee_stack_cleanup": 0,
  "variadic": false,
  "this_register": null,
  "register_arguments": ["ecx", "edx"],
  "return_registers": ["eax"],
  "structure_return": false,
  "floating_point": "sse"
}
```

---

## Step 5: Generate execution harnesses

```console
$ x86decomp harness-generate projects/velocity-decomp/config/abi/PhysicsTick-401000.json \
    projects/velocity-decomp/tests/harnesses/PhysicsTick-harness.json \
    --max-instructions 50000 \
    --timeout-ms 2000

$ x86decomp harness-generate projects/velocity-decomp/config/abi/CollisionCheck-401200.json \
    projects/velocity-decomp/tests/harnesses/CollisionCheck-harness.json \
    --pointer-parameters projects/velocity-decomp/config/pointers/CollisionCheck-pointers.json \
    --max-instructions 50000 \
    --timeout-ms 2000
```

**Explanation:** `harness-generate` produces a JSON execution harness from an ABI contract.
The harness specifies initial register values, memory layout, and stub hooks for external calls.
`--pointer-parameters` provides a JSON file describing pointer parameters (memory regions, sizes,
alias constraints) — the harness will initialize and observe those regions. `--no-observe-pointers`
disables pointer observation if all parameters are value types. `--max-instructions` and
`--timeout-ms` set execution bounds.

!!! tip "Harness tuning"
    Edit generated harnesses to add deterministic stubs for any external functions the target
    calls. Without stubs, the Unicorn emulator will fault on `call` instructions to external
    addresses.

---

## Step 6: Compile candidate C sources

Write candidate C source for `PhysicsTick` at
`projects/velocity-decomp/src/functional/PhysicsTick.c`:

```c
#include <stdint.h>

float __stdcall PhysicsTick(float delta_time) {
    static float accumulator = 0.0f;
    accumulator += delta_time;
    if (accumulator > 1.0f) {
        accumulator -= 1.0f;
    }
    return accumulator;
}
```

Compile:

```console
$ x86decomp compile projects/velocity-decomp/config/compiler-profiles/msvc-2003-x86-release.json \
    projects/velocity-decomp/src/functional/PhysicsTick.c \
    projects/velocity-decomp/build/candidates/PhysicsTick.obj \
    --report projects/velocity-decomp/reports/compile-PhysicsTick.json \
    --extra-arg /arch:IA32
```

Extract the compiled bytes for validation:

```console
$ x86decomp coff-extract projects/velocity-decomp/build/candidates/PhysicsTick.obj \
    _PhysicsTick@4 projects/velocity-decomp/build/candidates/PhysicsTick.bin \
    --size 0x80
```

---

## Step 7: Dynamic validation with Unicorn

Prepare the target function bytes (extract the original from the PE at its RVA):

```console
$ x86decomp coff-extract projects/velocity-decomp/original/velocity-extracted-sections/physics.obj \
    _PhysicsTick@4 projects/velocity-decomp/build/targets/PhysicsTick-original.bin \
    --size 0x80
```

Run dynamic validation:

```console
$ x86decomp dynamic-validate projects/velocity-decomp/build/targets/PhysicsTick-original.bin \
    projects/velocity-decomp/build/candidates/PhysicsTick.bin \
    projects/velocity-decomp/tests/harnesses/PhysicsTick-harness.json \
    --target-base 0x401000 \
    --candidate-base 0x500000 \
    --report projects/velocity-decomp/reports/dynamic-PhysicsTick.json
```

**Explanation:** `dynamic-validate` runs both the target and candidate binary blobs through the
Unicorn CPU emulator under identical initial register/memory state (from the harness), then
compares observable side effects: register values, memory writes, and flags. `--target-base` and
`--candidate-base` specify the load addresses for each blob — use different addresses to catch
hardcoded address dependencies in the candidate.

**Expected output:**

```json
{
  "target_base": 4198400,
  "candidate_base": 5242880,
  "instruction_count": 42,
  "differentially_validated": true,
  "register_comparison": {
    "eax": {"match": true, "target": 1065353216, "candidate": 1065353216},
    "ecx": {"match": true},
    "edx": {"match": true}
  },
  "memory_comparison": {
    "regions_compared": 3,
    "mismatched_regions": 0
  },
  "divergences": []
}
```

`differentially_validated: true` with zero divergences means the candidate produces identical
observable state to the original for this bounded execution.

!!! danger "Not a security boundary"
    This validator emulates bounded leaf routines. It does not model a complete Windows process,
    filesystem, or network. External calls are only modeled when the harness provides stubs.

---

## Step 8: Symbolic validation with Z3

For the floating-point collision function, run symbolic comparison:

```console
$ x86decomp symbolic-validate projects/velocity-decomp/build/targets/CollisionCheck-original.bin \
    projects/velocity-decomp/build/candidates/CollisionCheck.bin \
    --architecture x86 \
    --input-register ecx --input-register edx \
    --stack-argument-words 0 \
    --output-register eax \
    --max-steps 1000 \
    --max-paths 64 \
    --report projects/velocity-decomp/reports/symbolic-CollisionCheck.json
```

**Explanation:** `symbolic-validate` lifts both binary blobs into symbolic expressions, constructs
an equivalence query with symbolic inputs fed through both implementations, and proves or disproves
output equivalence using Z3. `--input-register` marks registers as symbolic inputs.
`--output-register` selects which registers to compare after execution — if omitted, all
general-purpose registers are compared. `--max-steps` and `--max-paths` bound the exploration.

**Expected output:**

```json
{
  "result": "equivalent",
  "steps_explored": 156,
  "paths_explored": 4,
  "counterexample": null
}
```

`result: "equivalent"` means Z3 proved that no path diverges on the observed outputs for the
declared symbolic inputs. This is a stronger guarantee than dynamic validation but is still bounded
to the modeled instruction subset and explored paths.

!!! note "Equivalence scope"
    A successful `UNSAT` result only covers the modeled instruction subset, symbolic inputs,
    explored paths, and selected output registers. It does not prove identity under all
    possible inputs, memory states, or untracked side effects.

---

## Step 9: Create integration scenarios

Create `projects/velocity-decomp/tests/integration/scenarios.json`:

```json
{
  "scenarios": [
    {
      "name": "replay_001_physics_tick",
      "target": "{artifact}/velocity-original.exe",
      "candidate": "{artifact}/velocity-rebuilt.exe",
      "observations": {
        "exit_code": 0,
        "stdout_sha256": "a1b2c3d4..."
      },
      "arguments": ["--replay", "{workdir}/replay_001.dat", "--headless"]
    },
    {
      "name": "replay_002_collision",
      "target": "{artifact}/velocity-original.exe",
      "candidate": "{artifact}/velocity-rebuilt.exe",
      "observations": {
        "exit_code": 0,
        "file_outputs": [
          {"path": "{workdir}/physics_log.txt", "sha256": "e5f6a7b8..."}
        ]
      },
      "arguments": ["--replay", "{workdir}/replay_002.dat", "--headless", "--log-physics"]
    }
  ]
}
```

Run the integration scenarios:

```console
$ x86decomp integration-run projects/velocity-decomp/tests/integration/scenarios.json \
    --allow-host-execution \
    --report projects/velocity-decomp/reports/integration-results.json
```

**Explanation:** `integration-run` reads the integration manifest and executes each scenario.
Both the target (original) and candidate (rebuilt) executables are run in temporary working
directories with identical arguments. Only declared observations (exit code, stdout hash, file
outputs) are compared. Finite scenarios are never treated as universal equivalence proof.

!!! danger "Host execution requires explicit authorization"
    Integration scenarios execute real Windows binaries. The toolkit refuses to run them
    without the `--allow-host-execution` flag. Only enable this when you have verified the
    executables and trust the manifest.

**Expected output:**

```json
{
  "scenarios_run": 2,
  "passed": 2,
  "failed": 0,
  "results": [
    {
      "name": "replay_001_physics_tick",
      "passed": true,
      "observations_matched": 3,
      "observations_total": 3
    }
  ]
}
```

---

## Step 10: Initialize and update per-function workflows

```console
$ x86decomp workflow-init projects/velocity-decomp/ pe-rva:00401000 --mode functional
$ x86decomp workflow-init projects/velocity-decomp/ pe-rva:00401200 --mode functional
```

**Explanation:** `workflow-init` creates per-function workflow state. `--mode functional` enables
only the functional pipeline — matching status cannot be advanced.

Advance workflow states after validation:

```console
$ x86decomp workflow-update projects/velocity-decomp/ pe-rva:00401000 \
    --functional-status differentially_validated \
    --source-stage human_candidate \
    --candidate src/functional/PhysicsTick.c \
    --compiler-profile msvc-2003-x86-release \
    --report-kind dynamic_validation \
    --report-path reports/dynamic-PhysicsTick.json

$ x86decomp workflow-update projects/velocity-decomp/ pe-rva:00401200 \
    --functional-status symbolically_bounded \
    --source-stage human_candidate \
    --candidate src/functional/CollisionCheck.c \
    --compiler-profile msvc-2003-x86-release \
    --report-kind symbolic_validation \
    --report-path reports/symbolic-CollisionCheck.json
```

**Explanation:** `workflow-update` advances the functional status along the pipeline:
`not_started → decompiled → compiles → abi_compatible → differentially_validated →
symbolically_bounded → integration_validated`. Status advancement is monotonic by default;
use `--allow-regression` to move backward.

**Verify state:**

```console
$ x86decomp workflow-show projects/velocity-decomp/ pe-rva:00401000
```

```json
{
  "function_id": "pe-rva:00401000",
  "selected_modes": ["functional"],
  "source_stage": "human_candidate",
  "matching_status": "not_started",
  "functional_status": "differentially_validated",
  "active_candidate": "src/functional/PhysicsTick.c",
  "compiler_profile": "msvc-2003-x86-release",
  "reports": {
    "dynamic_validation": "reports/dynamic-PhysicsTick.json"
  },
  "blockers": []
}
```

---

## Step 11: Add evidence records

```console
$ x86decomp evidence-add projects/velocity-decomp/ \
    --kind dynamic_trace \
    --source "Unicorn dynamic validator" \
    --locator "function PhysicsTick at RVA 0x401000" \
    --assertion "Candidate differentially_validated against original: 42 instructions, 0 divergences" \
    --independent-group "dynamic-validation" \
    --file reports/dynamic-PhysicsTick.json \
    --id ev-dynamic-PhysicsTick

$ x86decomp evidence-add projects/velocity-decomp/ \
    --kind dynamic_trace \
    --source "Z3 symbolic validator" \
    --locator "function CollisionCheck at RVA 0x401200" \
    --assertion "Candidate symbolically equivalent to original: 156 steps, 4 paths, UNSAT" \
    --independent-group "symbolic-validation" \
    --file reports/symbolic-CollisionCheck.json \
    --id ev-symbolic-CollisionCheck

$ x86decomp evidence-add projects/velocity-decomp/ \
    --kind dynamic_trace \
    --source "Integration test runner" \
    --locator "scenario replay_001_physics_tick" \
    --assertion "Rebuilt executable produces identical output to original for replay 001" \
    --independent-group "integration-testing" \
    --file reports/integration-results.json \
    --id ev-integration-001
```

**Explanation:** All three validation results are recorded as `dynamic_trace` evidence (the kind
that covers runtime and emulated observations). Each record belongs to a different `--independent-group`,
which is required for claim verification (claims need 3 distinct groups).

---

## Step 12: Create and verify claims

```console
$ x86decomp claim-create projects/velocity-decomp/ \
    --subject "pe-rva:00401000" \
    --predicate "is_functionally_equivalent" \
    --object "true" \
    --evidence ev-dynamic-PhysicsTick ev-integration-001 \
    --id claim-PhysicsTick-functional

$ x86decomp claim-create projects/velocity-decomp/ \
    --subject "pe-rva:00401200" \
    --predicate "is_functionally_equivalent" \
    --object "true" \
    --evidence ev-symbolic-CollisionCheck ev-integration-001 \
    --id claim-CollisionCheck-functional
```

**Explanation:** `claim-create` creates an evidence-linked claim. Claims start in `proposed` state
and progress through `corroborated` to `verified` as more evidence is attached.

**Attach the integration evidence to both claims:**

```console
$ x86decomp claim-attach projects/velocity-decomp/ claim-PhysicsTick-functional ev-integration-001
$ x86decomp claim-attach projects/velocity-decomp/ claim-CollisionCheck-functional ev-integration-001
```

**Verify claims:**

```console
$ x86decomp claim-verify projects/velocity-decomp/ claim-PhysicsTick-functional
$ x86decomp claim-verify projects/velocity-decomp/ claim-CollisionCheck-functional
```

**Expected output (PhysicsTick):**

```json
{
  "claim_id": "claim-PhysicsTick-functional",
  "state": "corroborated",
  "evidence_count": 2,
  "independent_groups": 2,
  "distinct_kinds": 1,
  "contradictions": [],
  "verification_gate": {
    "required_evidence": 3,
    "required_groups": 3,
    "required_kinds": 2,
    "meets_threshold": false
  }
}
```

`state: "corroborated"` and `meets_threshold: false` — the claim needs one more evidence record
from a new independent group and a second evidence kind to reach `verified`.

Add a human review evidence record and a static analysis record to satisfy the gate:

```console
$ x86decomp evidence-add projects/velocity-decomp/ \
    --kind human_review \
    --source "Analyst: Sean" \
    --locator "function PhysicsTick at RVA 0x401000" \
    --assertion "Reviewed disassembly, harness configuration, and candidate C source. All match expected behavior." \
    --independent-group "human-review" \
    --id ev-human-PhysicsTick

$ x86decomp claim-attach projects/velocity-decomp/ claim-PhysicsTick-functional ev-human-PhysicsTick

$ x86decomp claim-verify projects/velocity-decomp/ claim-PhysicsTick-functional
```

Now `state: "verified"` with `meets_threshold: true`.

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `dynamic-validate` crashes with `ExternalToolError` | Unicorn not installed | `pip install x86decomp-toolkit[dynamic]` |
| `symbolic-validate` reports instruction not supported | Built-in executor doesn't handle a specific instruction | Fall back to `angr-validate` which handles a broader instruction set |
| `dynamic-validate` produces divergences on `eflags` | Different flag side effects from instruction selection | Add `eflags` to the harness's ignored-flags mask, or adjust the candidate source |
| `integration-run` fails without `--allow-host-execution` | Safety gate — toolkit refuses host execution without explicit authorization | Add `--allow-host-execution` only after verifying executables and manifest |
| `harness-generate` produces incomplete harness | External calls in the target function have no stubs | Edit the harness JSON to add stub hooks for each `call` instruction target |
| `workflow-update` rejects functional status change | Matching mode is the only mode enabled | Re-init the workflow with `--mode functional` or delete and re-create |

---

## Related reference pages

- [Decompilation Modes concept](../concepts/decompilation-modes.md) — Matching vs functional pipelines
- [ABI and Types concept](../concepts/abi-and-types.md) — ABI contracts and conventions
- [Evidence and Claims concept](../concepts/evidence-and-claims.md) — Evidence gate requirements
- [Workflow Commands](../commands/workflow/workflow.md) — `workflow-init`, `workflow-show`, `workflow-update`
- [dynamic-validate command](../commands/validation/dynamic.md) — Unicorn differential execution
- [symbolic-validate command](../commands/validation/symbolic.md) — Z3 and angr symbolic comparison
- [harness-generate command](../commands/reconstruction/harness.md) — Execution harness generation
- [integration-run command](../commands/integration/integration-run.md) — Integration scenario execution
- [Evidence and Claims Commands](../commands/workflow/evidence-claims.md) — `evidence-add`, `claim-create`, `claim-verify`
- [compile command](../commands/compilation/compile.md) — Compile candidate sources
- [ghidra-export command](../commands/ghidra/export.md) — Ghidra export workflow

---

## Optional extensions

1. **angr validation** — If the built-in Z3 executor rejects unsupported instructions, use the
   angr backend which handles a broader instruction set:

   ```console
   $ x86decomp angr-validate target.bin candidate.bin \
       --architecture x86 \
       --input-register ecx --input-register edx \
       --output-register eax \
       --max-steps 500 --max-paths 32 \
       --report reports/angr-report.json
   ```

   Results are scoped identically but angr may explore different paths. Note that angr is
   non-deterministic due to path explosion heuristics.

2. **Symbolic memory validation** — For functions that operate on pointer parameters with possible
   aliasing, use `symbolic-memory-validate`:

   ```console
   $ x86decomp symbolic-memory-validate target.bin candidate.bin harnesses/memory-harness.json \
       --report reports/symbolic-memory-report.json
   ```

   This enumerates all alias relationships between symbolic memory regions and checks equivalence
   for each case.

3. **DynamoRIO coverage** — Trace the original game with DynamoRIO to identify which functions
   are actually exercised by real gameplay:

   ```console
   $ x86decomp drcov-run games/velocity/velocity.exe drcov-output/ \
       --drrun /opt/dynamorio/bin64/drrun.exe \
       --program-arg "--replay" --program-arg "replays/replay_001.dat" \
       --timeout 60 \
       --report reports/drcov-report.json
   ```

   Parse the coverage log:

   ```console
   $ x86decomp drcov-parse drcov-output/drcov.velocity.exe.0000.proc.log
   ```

   Only validate functions that are covered by real gameplay — uncovered functions may be dead
   code or debug-only paths.

4. **Benchmark integration** — Add functional validation cases to a benchmark manifest for CI:

   ```json
   {
     "kind": "dynamic",
     "label": "PhysicsTick_functional",
     "target": "bin/PhysicsTick-original.bin",
     "candidate": "bin/PhysicsTick-candidate.bin",
     "harness": "harnesses/PhysicsTick-harness.json",
     "expect": {"differentially_validated": true}
   }
   ```

   Run with `x86decomp benchmark-run benchmarks/functional-validation.json`.

5. **Pipeline automation** — Create a pipeline that chains compile → coff-extract → dynamic-validate
   → symbolic-validate → workflow-update for every function with functional mode enabled:

   ```console
   $ x86decomp pipeline-create projects/velocity-decomp/ \
       projects/velocity-decomp/orchestration/pipelines/functional-pipeline.json \
       --without-ghidra

   $ x86decomp pipeline-run projects/velocity-decomp/ \
       projects/velocity-decomp/orchestration/pipelines/functional-pipeline.json
   ```
