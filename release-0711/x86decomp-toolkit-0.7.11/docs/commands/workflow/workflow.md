# Workflow Commands

Per-function decompilation workflow tracking with independent matching and functional status pipelines.

## `workflow-init`

Initialize per-function workflow state.

```bash
x86decomp workflow-init PROJECT FUNCTION_ID --mode {matching,functional}
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `FUNCTION_ID` | yes | Function identifier (e.g. `pe-rva:00401000`) |
| `--mode` | no | One or more decompilation modes; repeatable. If omitted, both modes are selected |

### Modes

| Value | Description |
|---|---|
| `matching` | Byte-identical reproduction |
| `functional` | Behaviorally equivalent reproduction |

!!! warning "Mode selection is immutable after initialization"
    `selected_modes` cannot be changed on an existing workflow. Delete the workflow directory and re-initialize if different modes are needed.

### Examples

```bash
# Both modes (default)
x86decomp workflow-init ./myproject pe-rva:00401000

# Matching only
x86decomp workflow-init ./myproject pe-rva:00401000 --mode matching

# Both modes explicitly
x86decomp workflow-init ./myproject pe-rva:00401000 --mode matching --mode functional
```

---

## `workflow-show`

Show validated per-function workflow state.

```bash
x86decomp workflow-show PROJECT FUNCTION_ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `FUNCTION_ID` | yes | Function identifier |

### Example

```bash
x86decomp workflow-show ./myproject pe-rva:00401000
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

---

## `workflow-update`

Update validated per-function workflow state.

```bash
x86decomp workflow-update PROJECT FUNCTION_ID \
  --source-stage STAGE \
  --matching-status STATUS \
  --functional-status STATUS \
  --candidate PATH \
  --compiler-profile PROFILE \
  --report-kind KIND \
  --report-path PATH \
  --blocker TEXT \
  --allow-regression
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `FUNCTION_ID` | yes | Function identifier |
| `--source-stage` | no | Source stage value from `SourceStage` enum |
| `--matching-status` | no | Matching status value from `MatchingStatus` enum |
| `--functional-status` | no | Functional status value from `FunctionalStatus` enum |
| `--candidate` | no | Path to active candidate source file |
| `--compiler-profile` | no | Compiler profile identifier |
| `--report-kind` | no | Report kind key for the reports map |
| `--report-path` | no | Path to the report file |
| `--blocker` | no | Blocker description text |
| `--allow-regression` | no | Permit moving to a lower-ranked status |

### Source stages

| Value | Meaning |
|---|---|
| `original_bytes` | No C source exists yet |
| `generated_assembly` | Assembly listing produced from original bytes |
| `decompiler_candidate` | C source from an automated decompiler |
| `human_candidate` | C source written or refined by a human |
| `accepted_source` | C source that passed its mode's acceptance gate |

### Matching statuses

| Value | Meaning |
|---|---|
| `not_started` | No matching work has begun |
| `decompiled` | C source exists (unverified) |
| `compiles` | Source compiles successfully |
| `abi_compatible` | ABI contract verified |
| `instruction_similar` | Instructions are structurally similar |
| `byte_matched` | Relocation-resolved bytes are identical |
| `image_integrated` | Function integrated into the PE image |
| `full_relink_validated` | Full relink produces the original image |
| `blocked` | Progress is blocked |

### Functional statuses

| Value | Meaning |
|---|---|
| `not_started` | No functional work has begun |
| `decompiled` | C source exists (unverified) |
| `compiles` | Source compiles successfully |
| `abi_compatible` | ABI contract verified |
| `differentially_validated` | Differential execution passed |
| `symbolically_bounded` | Symbolic comparison passed |
| `integration_validated` | Integration scenario tests passed |
| `blocked` | Progress is blocked |

!!! tip "Monotonic by default"
    Status advancement is monotonic. Use `--allow-regression` to move backward (e.g., from `byte_matched` to `compiles`). Rolling back does not update linked artifacts or evidence records.

!!! danger "Mode guard"
    The command rejects status changes for modes that are not selected for this function. Check with `workflow-show` first.

### Examples

```bash
# Advance matching status to compiles
x86decomp workflow-update ./myproject pe-rva:00401000 \
  --matching-status compiles \
  --source-stage human_candidate \
  --candidate src/matched/00401000.c \
  --compiler-profile msvc-2019-x86-release

# Record a byte-match report
x86decomp workflow-update ./myproject pe-rva:00401000 \
  --matching-status byte_matched \
  --report-kind byte_match \
  --report-path reports/matching/00401000-byte.json

# Mark a blocker
x86decomp workflow-update ./myproject pe-rva:00401000 \
  --matching-status blocked \
  --blocker "Unresolved indirect call through vtable at 0x401050"

# Allow regression
x86decomp workflow-update ./myproject pe-rva:00401000 \
  --matching-status compiles \
  --allow-regression
```
