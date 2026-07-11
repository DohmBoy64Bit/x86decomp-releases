# Pipeline Commands

Durable analysis pipeline management with create, run, status, cancel, retry, and stale-recovery operations.

## `pipeline-create`

Create a default durable analysis pipeline manifest.

```bash
x86decomp pipeline-create PROJECT OUTPUT --without-ghidra
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `OUTPUT` | yes | Path for the generated pipeline manifest file |
| `--without-ghidra` | no | Exclude Ghidra export stages from the pipeline |

### Example

```bash
x86decomp pipeline-create ./myproject ./pipelines/default.json

# Without Ghidra stages
x86decomp pipeline-create ./myproject ./pipelines/no-ghidra.json --without-ghidra
```

---

## `pipeline-run`

Run or resume a durable project pipeline.

```bash
x86decomp pipeline-run PROJECT MANIFEST --continue-on-failure
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `MANIFEST` | yes | Path to the pipeline manifest file |
| `--continue-on-failure` | no | Continue running subsequent stages even if a stage fails (default: stop on failure) |

A pipeline run persists its state. Re-running the same manifest resumes from incomplete stages.

### Example

```bash
x86decomp pipeline-run ./myproject ./pipelines/default.json

# Continue past failures
x86decomp pipeline-run ./myproject ./pipelines/default.json --continue-on-failure
```

---

## `pipeline-status`

Show durable pipeline and stage status.

```bash
x86decomp pipeline-status PROJECT PIPELINE_ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `PIPELINE_ID` | yes | Pipeline run identifier |

Returns the overall pipeline status and per-stage status, timing, and any error details.

### Example

```bash
x86decomp pipeline-status ./myproject run-20260711-001
```

---

## `pipeline-cancel`

Cancel a pipeline or one pipeline stage.

```bash
x86decomp pipeline-cancel PROJECT PIPELINE_ID --stage-id ID
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `PIPELINE_ID` | yes | Pipeline run identifier |
| `--stage-id` | no | Cancel a specific stage; if omitted, cancels the entire pipeline |

Cancelled stages are not retried unless explicitly re-queued via `pipeline-retry`.

### Example

```bash
# Cancel entire pipeline
x86decomp pipeline-cancel ./myproject run-20260711-001

# Cancel a specific stage
x86decomp pipeline-cancel ./myproject run-20260711-001 --stage-id ghidra-export
```

---

## `pipeline-retry`

Retry a failed pipeline stage.

```bash
x86decomp pipeline-retry PROJECT PIPELINE_ID STAGE_ID --cascade
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `PIPELINE_ID` | yes | Pipeline run identifier |
| `STAGE_ID` | yes | Stage identifier to retry |
| `--cascade` | no | Also retry all downstream stages that depend on this stage |

!!! tip
    Use `--cascade` when a failed stage invalidates downstream results. Without it, only the specified stage is retried.

### Example

```bash
x86decomp pipeline-retry ./myproject run-20260711-001 ghidra-export

# Retry with all downstream stages
x86decomp pipeline-retry ./myproject run-20260711-001 ghidra-export --cascade
```

---

## `pipeline-recover`

Reset jobs with stale durable runner heartbeats.

```bash
x86decomp pipeline-recover PROJECT --pipeline-id ID --stale-seconds 600
```

| Argument | Required | Description |
|---|---|---|
| `PROJECT` | yes | Path to the project root |
| `--pipeline-id` | no | Restrict recovery to a specific pipeline; if omitted, all pipelines are checked |
| `--stale-seconds` | no | Heartbeat age threshold in seconds for a job to be considered stale (default: `600`) |

Stale jobs are reset to a pending state so they can be re-acquired by a runner.

### Example

```bash
# Recover all stale jobs across all pipelines
x86decomp pipeline-recover ./myproject

# Recover a specific pipeline's stale jobs with a 5-minute threshold
x86decomp pipeline-recover ./myproject --pipeline-id run-20260711-001 --stale-seconds 300
```
