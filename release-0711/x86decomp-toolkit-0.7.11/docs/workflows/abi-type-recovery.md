# ABI and Type Recovery

**Operation Stormfront** — A fictional first-person shooter compiled with MSVC 6.0 for x86
Windows PE. The target binary contains hundreds of functions whose calling conventions and
parameter types must be recovered before any decompilation can begin.

---

## Scenario

> You have acquired a copy of `stormsoldier.exe`, the retail executable for Operation
> Stormfront. The game shipped in 2001 with no debug symbols. Community analysis has
> identified that the binary uses `stdcall` for exported functions and `thiscall` for C++
> class methods, but most internal helpers have unknown conventions. You need to
> systematically recover ABI contracts and type constraints for every function, resolve
> conflicts, and build a work queue for the decompilation team.

## What you will accomplish

1. Export function artifacts from Ghidra for every function in the binary
2. Import artifacts into the project and the analysis database
3. Create ABI contracts for key functions and validate them with `abi-check`
4. Add type constraints to the analysis database with provenance tracking
5. Detect and resolve conflicting constraints
6. Initialize per-function workflow state
7. Create work-queue tasks and attach evidence-linked claims

## Prerequisites

- x86decomp 0.7.11 installed with Python 3.11+
- Ghidra 11.0+ installed at `/opt/ghidra`
- The target binary: `games/stormfront/stormsoldier.exe`
- A writable project directory: `projects/stormfront-decomp/`
- Install optional dependencies: `pip install x86decomp-toolkit[dynamic,symbolic]`

## Starting file structure

```
games/stormfront/
  stormsoldier.exe           # The target PE (x86, ~4 MB)
  stormsoldier.map           # Optional linker MAP (if available)

projects/stormfront-decomp/  # Empty directory for the project
```

---

## Step 1: Initialize the project

```console
$ x86decomp init games/stormfront/stormsoldier.exe projects/stormfront-decomp/
```

**Explanation:** `init` parses the PE, copies it into `projects/stormfront-decomp/original/`,
creates the full 37-directory project layout, initializes SQLite databases (analysis, work queue,
project state), the content-addressed artifact store, and the project memory ledger. `default_modes`
is set to `["matching", "functional"]`.

**Expected output:**

```json
{
  "schema_version": 3,
  "project_id": "x86d-a1b2c3d4e5f67890-deadbeef",
  "architecture": "x86",
  "default_modes": ["matching", "functional"],
  "binary": {
    "name": "stormsoldier.exe",
    "source_kind": "copied",
    "path": "original/stormsoldier.exe",
    "sha256": "e3b0c44298fc1c149afbf4c8996fb924...",
    "size": 4194304
  },
  "analysis_database": "analysis/database/analysis.sqlite3",
  "work_queue": "work/tasks.sqlite3",
  "status": "initialized"
}
```

**Verification:**

```console
$ x86decomp verify-project projects/stormfront-decomp/
```

Should produce `"valid": true, "failures": []`.

---

## Step 2: Export Ghidra function artifacts

```console
$ x86decomp ghidra-export games/stormfront/stormsoldier.exe \
    ghidra-workspace/ stormfront-functions/ \
    functions-export/ \
    --ghidra-home /opt/ghidra \
    --selector all \
    --overwrite \
    --report reports/ghidra-export.json
```

**Explanation:** `ghidra-export` runs the bundled Ghidra headless export workflow. It creates a
Ghidra project named `stormfront-functions` inside `ghidra-workspace/`, imports `stormsoldier.exe`,
runs analysis with `--selector all` (every recognized function), and exports per-function artifacts
into `functions-export/`. Each artifact directory contains `function.json` (metadata, address, size),
`decompiled.c` (decompiler output), `disassembly.jsonl` (instruction records), and `cfg.json`
(control-flow graph). The `--overwrite` flag replaces any existing export. The `--timeout` defaults
to 3600 seconds.

**Expected output structure:**

```
functions-export/
  export.json                  # Export manifest with function list and hashes
  sub_401000/
    function.json
    decompiled.c
    disassembly.jsonl
    cfg.json
  sub_401050/
    ...
  sub_4010A0/
    ...
  ... (hundreds of functions)
```

**Verification:**

```console
$ x86decomp artifact-verify functions-export/sub_401000/
```

Should return `"valid": true, "failures": []` — confirms the artifact directory has correct
content hashes.

---

## Step 3: Import function artifacts into the project

```console
$ x86decomp artifact-import projects/stormfront-decomp/ functions-export/
```

**Explanation:** `artifact-import` reads the `export.json` manifest, verifies each artifact
directory's integrity, and copies validated artifacts into `projects/stormfront-decomp/functions/`.
Each function gets its own subdirectory. Artifacts are re-verified on import.

**Expected output per function:**

```json
{
  "artifact_dir": "/path/to/projects/stormfront-decomp/functions/sub_401000",
  "verification": {
    "valid": true,
    "failures": []
  }
}
```

---

## Step 4: Ingest artifacts into the analysis database

```console
$ x86decomp db-ingest projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    functions-export/export.json \
    --image-base 0x400000
```

**Explanation:** `db-ingest` reads the export manifest and populates the analysis database with
function metadata (address, name, size, instruction count) for every exported function. The
`--image-base 0x400000` is the typical x86 PE base address; adjust if `inspect-pe` reports a
different `image_base`.

**Verification — query ingested functions:**

```console
$ x86decomp db-query projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    "SELECT function_id, name, start_rva, end_rva FROM functions LIMIT 5"
```

---

## Step 5: Create ABI contracts for candidate functions

Create `contracts/sub_401000-abi.json`:

```json
{
  "architecture": "x86",
  "convention": "stdcall",
  "stack_argument_bytes": 12,
  "callee_stack_cleanup": 12,
  "variadic": false,
  "this_register": null,
  "register_arguments": [],
  "return_registers": ["eax"],
  "structure_return": false,
  "floating_point": "none"
}
```

This contract hypothesizes that `sub_401000` is a `stdcall` function taking 12 bytes of stack
arguments (three 4-byte parameters), cleaning its own stack with `ret 0C`.

---

## Step 6: Validate ABI contracts with abi-check

Extract the raw function bytes first (from the original binary, using the RVA and size from the
artifact):

```console
$ x86decomp abi-check functions/sub_401000/code.bin \
    contracts/sub_401000-abi.json \
    --base 0x401000 \
    --report reports/sub_401000-abi.json
```

**Explanation:** `abi-check` disassembles the binary code blob and statically checks whether
observed instruction patterns conform to the declared ABI contract. It verifies prologue/epilogue
structure, register usage, stack frame management, parameter access patterns, and return value
handling. The `--base` address ensures correct branch target interpretation during disassembly.

**Expected output (abbreviated):**

```json
{
  "kind": "bounded_static_abi_validation",
  "contract": {
    "convention": "stdcall",
    "stack_argument_bytes": 12,
    "callee_stack_cleanup": 12
  },
  "checks": [
    {
      "name": "callee_stack_cleanup",
      "passed": true,
      "expected": 12,
      "observed": 12,
      "strength": "direct_epilogue_observation"
    }
  ],
  "compatible_with_observed_code": true,
  "semantic_or_full_abi_equivalence_claimed": false
}
```

!!! warning "ABI checks are bounded"
    `compatible_with_observed_code: true` means the code does not contradict the contract.
    It is NOT a claim of full semantic ABI equivalence. The check strength field
    (e.g., `direct_epilogue_observation`) indicates how strong the evidence is.

---

## Step 7: Add type constraints to the analysis database

For each parameter of each function, add provenance-bearing type constraints:

```console
$ x86decomp db-constraint-add projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    "pe-rva:00401000:arg_0" has_type "int*" \
    "ghidra-parameter-analysis" \
    --confidence 0.85

$ x86decomp db-constraint-add projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    "pe-rva:00401000:arg_1" has_type "size_t" \
    "ghidra-parameter-analysis" \
    --confidence 0.80

$ x86decomp db-constraint-add projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    "pe-rva:00401000:arg_2" has_type "uint32_t" \
    "static-stack-analysis" \
    --confidence 0.90

$ x86decomp db-constraint-add projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    "pe-rva:00401000" has_calling_convention "stdcall" \
    "abi-check-report" \
    --evidence-id ev-abi-401000 \
    --confidence 0.98
```

**Explanation:** `db-constraint-add` inserts a constraint record with the subject entity
(e.g., `pe-rva:00401000:arg_0`), a relation (`has_type`), an object value (`int*`), and a provenance
string. Optional `--evidence-id` links to an evidence record. Optional `--confidence` records a
confidence score as a float.

!!! tip "Constraint subjects"
    Use consistent naming: `pe-rva:ADDRESS:arg_N` for parameters, `pe-rva:ADDRESS` for
    function-level properties like calling convention.

---

## Step 8: Detect constraint conflicts

```console
$ x86decomp db-constraint-conflicts projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    "pe-rva:00401000:arg_0" has_type
```

**Explanation:** `db-constraint-conflicts` returns pairs of constraints for the same subject and
relation that have different object values. For example, if one analyst proposed `int*` and another
proposed `float*` for `arg_0`, they would appear as a conflict.

**Expected output when conflicts exist:**

```json
[
  {
    "constraint_id": 3,
    "subject": "pe-rva:00401000:arg_0",
    "relation": "has_type",
    "object_value": "int*",
    "provenance": "ghidra-parameter-analysis",
    "confidence": 0.85
  },
  {
    "constraint_id": 17,
    "subject": "pe-rva:00401000:arg_0",
    "relation": "has_type",
    "object_value": "float*",
    "provenance": "dynamic-trace-analysis",
    "confidence": 0.72
  }
]
```

---

## Step 9: Resolve conflicts by accepting constraints

```console
$ x86decomp db-constraint-accept projects/stormfront-decomp/analysis/database/analysis.sqlite3 3
```

**Explanation:** `db-constraint-accept` marks the selected constraint as accepted and rejects all
other conflicting constraints for the same subject and relation. Always run `db-constraint-conflicts`
first to review all conflicting values before accepting.

**Expected output:**

```json
{"accepted": 3}
```

---

## Step 10: Initialize per-function workflow states

```console
$ x86decomp workflow-init projects/stormfront-decomp/ pe-rva:00401000 --mode matching
$ x86decomp workflow-init projects/stormfront-decomp/ pe-rva:00401100 --mode matching
$ x86decomp workflow-init projects/stormfront-decomp/ pe-rva:00401200 --mode matching --mode functional
```

**Explanation:** `workflow-init` creates per-function workflow tracking at
`functions/pe-rva_00401000/workflow.json`. Each function gets its own workflow file with independent
matching and functional status pipelines. The `--mode` flag selects which mode pipelines are active;
omit it to enable both.

**Verify a workflow:**

```console
$ x86decomp workflow-show projects/stormfront-decomp/ pe-rva:00401000
```

```json
{
  "function_id": "pe-rva:00401000",
  "selected_modes": ["matching"],
  "source_stage": "original_bytes",
  "matching_status": "not_started",
  "functional_status": "not_started",
  "active_candidate": null,
  "compiler_profile": null,
  "reports": {},
  "blockers": []
}
```

---

## Step 11: Create work-queue tasks for the team

```console
$ x86decomp work-create projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    pe-rva:00401000 matching decompile \
    "Produce matching C source for sub_401000. ABI: stdcall, args: (int*, size_t, uint32_t). Size: 0x50 bytes." \
    --validator diff-bytes --validator abi-check --priority 5

$ x86decomp work-create projects/stormfront-decomp/analysis/database/analysis.sqlite3 \
    pe-rva:00401100 matching decompile \
    "Produce matching C source for sub_401100. ABI: cdecl, args: (const char*, int). Size: 0x40 bytes." \
    --validator diff-bytes --validator abi-check --priority 3
```

**Explanation:** `work-create` adds a task to the SQLite work queue. `MODE` is `matching` or
`functional`. `KIND` is a free-form task kind (e.g., `decompile`, `abi-recover`, `type-annotate`).
`INSTRUCTIONS` are free-form text describing the task. `--validator` names the validators that must
pass before the task is accepted — at least one is required. `--priority` controls task ordering;
higher values are processed first.

**Verify queue state:**

```console
$ x86decomp work-next projects/stormfront-decomp/analysis/database/analysis.sqlite3 --mode matching
```

---

## Step 12: Add evidence records for constraints

```console
$ x86decomp evidence-add projects/stormfront-decomp/ \
    --kind static_analysis \
    --source "Ghidra 11.0 parameter analysis" \
    --locator "function sub_401000" \
    --assertion "sub_401000 arg_0 is int* based on ecx dereference at 0x401008" \
    --independent-group "ghidra-analysis" \
    --id ev-ghidra-401000-arg0

$ x86decomp evidence-add projects/stormfront-decomp/ \
    --kind static_analysis \
    --source "abi-check validator" \
    --locator "function sub_401000" \
    --assertion "sub_401000 conforms to stdcall convention with 12 bytes callee cleanup" \
    --independent-group "abi-validation" \
    --file reports/sub_401000-abi.json \
    --id ev-abi-401000-stdcall
```

**Explanation:** `evidence-add` records a provenance-bearing observation. `--kind` selects from
seven evidence categories (`binary_bytes`, `static_analysis`, `dynamic_trace`, `compiler_output`,
`debug_symbol`, `external_document`, `human_review`). `--independent-group` names the evidence
group — claims later require at least 3 distinct groups. `--file` optionally attaches a backing
file whose SHA-256 is recorded for integrity verification.

---

## Step 13: Create evidence-linked claims

```console
$ x86decomp claim-create projects/stormfront-decomp/ \
    --subject "pe-rva:00401000" \
    --predicate "has_calling_convention" \
    --object "stdcall" \
    --evidence ev-abi-401000-stdcall ev-ghidra-401000-arg0 \
    --id claim-401000-cconv

$ x86decomp claim-create projects/stormfront-decomp/ \
    --subject "pe-rva:00401000:arg_0" \
    --predicate "has_type" \
    --object "int*" \
    --evidence ev-ghidra-401000-arg0 \
    --id claim-401000-arg0-type
```

**Explanation:** `claim-create` creates an evidence-linked claim with subject-predicate-object
structure. Claims start in `proposed` state. They progress to `corroborated` (2 evidence records)
and `verified` (3 records, 3 independent groups, 2 distinct kinds, all file hashes match, no
contradictions).

**Verify claims:**

```console
$ x86decomp claim-verify projects/stormfront-decomp/ claim-401000-cconv
```

This returns the claim's current state and a breakdown of evidence counts, groups, kinds, and
any contradictions.

---

## Common failure cases and recovery

| Failure | Likely cause | Recovery |
|---|---|---|
| `artifact-verify` returns `valid: false` | Artifact directory was modified after export | Re-run `ghidra-export` with `--overwrite` |
| `db-constraint-conflicts` returns empty array but conflicts are expected | Constraints use different `subject` strings | Ensure consistent naming: `pe-rva:ADDRESS:arg_N` |
| `abi-check` rejects a valid contract | Base address mismatch causes wrong instruction decoding | Verify `--base` matches the function's actual RVA from `function.json` |
| `ghidra-export` times out | Large binary with `--selector all` | Increase `--timeout` (default 3600s) or use `--selector` with a function name filter |
| `workflow-init` fails | Function already has an initialized workflow | Delete `functions/pe-rva_ADDRESS/` directory and re-initialize |
| `db-ingest` fails to parse artifact | Export manifest path is incorrect | Pass the `export.json` file from the Ghidra export output, not individual function directories |

---

## Related reference pages

- [ABI and Types concept](../concepts/abi-and-types.md) — ABI contracts, type constraints, C++ recovery
- [Evidence and Claims concept](../concepts/evidence-and-claims.md) — 7 evidence kinds, verification gate
- [Workflow Commands](../commands/workflow/workflow.md) — `workflow-init`, `workflow-show`, `workflow-update`
- [Analysis Database Commands](../commands/workflow/analysis-db.md) — `db-ingest`, `db-constraint-add`, `db-constraint-conflicts`, `db-constraint-accept`
- [Evidence and Claims Commands](../commands/workflow/evidence-claims.md) — `evidence-add`, `claim-create`, `claim-verify`
- [Work Queue Commands](../commands/workflow/work-queue.md) — `work-create`, `work-next`, `work-claim`, `work-validate`
- [abi-check command](../commands/validation/abi.md) — ABI contract validation
- [ghidra-export command](../commands/ghidra/export.md) — Ghidra export workflow
- [artifact-import command](../commands/artifacts/artifact.md) — Artifact import and verification

---

## Optional extensions

1. **C++ member functions** — After recovering `thiscall` conventions, run `x86decomp cpp-recover`
   against the PE to identify vtables and class hierarchies. Create ABI contracts with
   `"convention": "thiscall"` and `"this_register": "ecx"`.

2. **Dynamic validation** — Use `x86decomp harness-generate` to produce execution harnesses from
   ABI contracts, then `x86decomp dynamic-validate` to differentially execute the original vs.
   candidate function under Unicorn.

3. **Automated pipeline** — Create a pipeline with `x86decomp pipeline-create` that chains
   ghidra-export → artifact-import → db-ingest → abi-check for all exported functions.

4. **decomp.me integration** — Use `x86decomp decompme-pack` to create decomp.me-compatible packets
   from artifact directories for community review of type constraints.

5. **Multi-analyst workflow** — Use `work-claim` to assign tasks to analysts, `work-propose` to
   attach proposals with evidence, and `work-validate` to record validator results. A task is
   accepted only when all declared validators report `--passed`.
