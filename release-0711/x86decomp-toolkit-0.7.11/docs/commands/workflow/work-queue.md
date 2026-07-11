# Work Queue Commands

Validated work-queue task management with required validators, proposals, and evidence tracking.

## `work-create`

Create a validated work-queue task.

```bash
x86decomp work-create DATABASE FUNCTION_ID MODE KIND INSTRUCTIONS \
  --validator VALIDATOR... --priority 0
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database |
| `FUNCTION_ID` | yes | Function identifier |
| `MODE` | yes | `matching` or `functional` |
| `KIND` | yes | Task kind (e.g. `decompile`, `abi-recover`, `type-annotate`) |
| `INSTRUCTIONS` | yes | Free-form task instructions |
| `--validator` | yes | Required validator identifier; repeatable for multiple validators |
| `--priority` | no | Task priority; higher values are processed first (default: `0`) |

!!! note "Validators are mandatory"
    At least one `--validator` is required. Each validator must record a result via `work-validate` before the task can be accepted.

### Example

```bash
x86decomp work-create ./db/analysis.db pe-rva:00401000 matching decompile \
  "Produce C source matching the original bytes at RVA 0x401000-0x401050" \
  --validator diff-bytes --validator abi-check --priority 5
```

---

## `work-next`

Show the next eligible work-queue task.

```bash
x86decomp work-next DATABASE --mode {matching,functional}
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database |
| `--mode` | no | Filter to `matching` or `functional` tasks only |

Returns the highest-priority unclaimed task, or an empty result if the queue is exhausted.

### Example

```bash
x86decomp work-next ./db/analysis.db --mode matching
```

---

## `work-claim`

Claim a work-queue task for an assignee.

```bash
x86decomp work-claim DATABASE TASK_ID ASSIGNEE
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database |
| `TASK_ID` | yes | Task identifier |
| `ASSIGNEE` | yes | Assignee name or identifier |

A claimed task is no longer eligible for `work-next` until released or completed.

### Example

```bash
x86decomp work-claim ./db/analysis.db task-42 analyst-sean
```

---

## `work-propose`

Attach a proposal and evidence to a work task.

```bash
x86decomp work-propose DATABASE TASK_ID PROPOSAL --evidence EVID...
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database |
| `TASK_ID` | yes | Task identifier |
| `PROPOSAL` | yes | Path to a JSON proposal file |
| `--evidence` | yes | Evidence identifier; repeatable for multiple evidence records |

The proposal JSON must conform to the work-task proposal schema. Evidence IDs must reference existing evidence records in the project.

### Example

```bash
x86decomp work-propose ./db/analysis.db task-42 ./proposals/task-42.json \
  --evidence ghidra-401000-params --evidence compiler-401000-cdecl
```

---

## `work-validate`

Record a validator result for a work task.

```bash
x86decomp work-validate DATABASE TASK_ID VALIDATOR REPORT_PATH --passed
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database |
| `TASK_ID` | yes | Task identifier |
| `VALIDATOR` | yes | Validator identifier (must match one declared in `--validator` at creation) |
| `REPORT_PATH` | yes | Path to the validator report file |
| `--passed` | no | Flag indicating the validator accepted the proposal |

A task is accepted only when all required validators report `--passed`.

### Example

```bash
x86decomp work-validate ./db/analysis.db task-42 diff-bytes \
  ./reports/matching/401000-byte.json --passed

x86decomp work-validate ./db/analysis.db task-42 abi-check \
  ./reports/matching/401000-abi.json --passed
```
