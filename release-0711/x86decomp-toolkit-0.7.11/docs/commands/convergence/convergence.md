# convergence-analyze

## `x86decomp convergence-analyze`

Measure image convergence between a reference and candidate image, with optional history tracking.

### Purpose

Compares a reference PE image against a candidate (rebuilt) PE image using a target-specific layout profile. Classifies observed differences — byte mismatches, section divergences, relocation differences, PE header field differences — and ranks next actions by impact. Optionally compares against a previous report to measure progress and appends the result to a convergence history file.

### Syntax

```
x86decomp convergence-analyze REFERENCE CANDIDATE [--profile PROFILE] [--previous PREV] [--report REPORT] [--history PATH]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `REFERENCE` | yes | path | Reference (original) PE image |
| `CANDIDATE` | yes | path | Candidate (rebuilt) PE image to compare |

### Options

| Option | Default | Description |
|---|---|---|
| `--profile PROFILE` | none | JSON image layout profile (from `image-profile`); recommended for accurate section matching |
| `--previous PREV` | none | Path to a previous convergence report for delta/progress analysis |
| `--report REPORT` | none | Write structured JSON convergence report to this path |
| `--history PATH` | none | Append the current result to a convergence history JSONL file |

### Analysis output

| Field | Description |
|---|---|
| `reference_sha256` | SHA-256 of the reference image |
| `candidate_sha256` | SHA-256 of the candidate image |
| `total_bytes` | Total image size in bytes |
| `matching_bytes` | Number of bytes that match |
| `mismatching_bytes` | Number of bytes that differ |
| `convergence_ratio` | Ratio of matching bytes to total bytes |
| `section_results` | Per-section comparison with match/mismatch counts |
| `remaining_actions` | Ranked list of next actions for improving convergence |
| `previous_comparison` | Delta from `--previous` report (if provided) |
| `history_entry` | Appended history line (if `--history` is specified) |

### Classification

Differences are classified by section kind:
- `executable` — `.text` and similar code sections
- `read_only_data` — `.rdata`, `.pdata`, `.xdata`
- `writable_data` — `.data`, `.bss`
- `resources` — `.rsrc`
- `relocations` — `.reloc`

The engine never claims causality unless the mismatch falls inside a declared PE field or normalization range.

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp convergence-analyze original.exe rebuilt.exe \
    --profile profiles/image-profile.json \
    --previous reports/convergence-v1.json \
    --report reports/convergence-v2.json \
    --history convergence-history.jsonl
```

### Related commands

- [image-profile](../reconstruction/image-match.md) — Derive a whole-image layout profile
- [image-match](../reconstruction/image-match.md) — Compare complete PE images
- [release-gate](release-gate.md) — Evaluate release acceptance contracts
