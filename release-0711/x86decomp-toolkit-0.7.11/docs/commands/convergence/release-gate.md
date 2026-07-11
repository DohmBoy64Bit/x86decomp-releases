# release-gate

## `x86decomp release-gate`

Evaluate explicit target release acceptance contracts.

### Purpose

Aggregates exact project-state, evidence, workflow, pipeline, reproducibility, security, and image-convergence records into a release acceptance evaluation. Each contract (workflow, pipeline, reproduction, security, convergence) is evaluated independently. The gate never upgrades a missing report into a pass and never treats the three-source rule as a guarantee of semantic truth.

### Syntax

```
x86decomp release-gate PROJECT [--reproduction-manifest PATH] [--security-report PATH] [--convergence-report PATH] [--require-workflows] [--require-verified-claims] [--require-succeeded-pipelines] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root directory |

### Options

| Option | Default | Description |
|---|---|---|
| `--reproduction-manifest PATH` | none | JSON reproducibility manifest (from `reproduce-create`) |
| `--security-report PATH` | none | JSON security audit report (from `security-audit`) |
| `--convergence-report PATH` | none | JSON convergence report (from `convergence-analyze`) |
| `--require-workflows` | false | Require all functions to meet minimum workflow state thresholds |
| `--require-verified-claims` | false | Require all claims to have sufficient independent evidence |
| `--require-succeeded-pipelines` | false | Require all pipelines to have succeeded |
| `--report REPORT` | none | Write structured JSON gate evaluation report to this path |

### Gate evaluation

| Gate | Source | Criterion |
|---|---|---|
| **Project state** | Project check | Valid structure, no unrepaired issues |
| **Target pack** | Target pack verification | Pack identity and integrity verified |
| **Workflow** | Per-function workflow state | Matching ≥ `compiles`, Functional ≥ `differentially_validated` (when `--require-workflows`) |
| **Pipeline** | Pipeline orchestrator | All pipelines succeeded (when `--require-succeeded-pipelines`) |
| **Reproducibility** | Reproduction manifest | Manifest verified, all inputs present (when `--reproduction-manifest` provided) |
| **Security** | Security audit report | No blocking findings (when `--security-report` provided) |
| **Convergence** | Convergence report | Convergence ratio meets threshold (when `--convergence-report` provided) |
| **Claims** | Evidence store | All claims have ≥3 independent evidence groups (when `--require-verified-claims`) |

### Result

The gate returns a structured evaluation with:

- `passed` — boolean; true only if every enabled contract is satisfied
- `contracts` — per-contract pass/fail with detailed failure reasons
- `summary` — human-readable summary of gate status

### Exit behavior

- Exit 0 on success (gate result reported in JSON, passing or failing is data not exit code)
- Exit 2 on argument error with argparse diagnostics on stderr

### Example

```console
$ x86decomp release-gate ./my-project \
    --reproduction-manifest reproduce/manifest.json \
    --security-report reports/security-audit.json \
    --convergence-report reports/convergence-v2.json \
    --require-workflows \
    --require-verified-claims \
    --require-succeeded-pipelines \
    --report reports/release-gate.json
```

### Related commands

- [reproduce-create](reproduce.md#x86decomp-reproduce-create) — Create reproducibility manifest
- [reproduce-verify](reproduce.md#x86decomp-reproduce-verify) — Verify reproducibility manifest
- [security-audit](../security/audit.md#x86decomp-security-audit) — Security audit
- [convergence-analyze](convergence.md) — Image convergence measurement
