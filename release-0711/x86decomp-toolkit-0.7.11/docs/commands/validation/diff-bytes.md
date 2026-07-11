# diff-bytes

Compare two files byte-for-byte with bounded mismatch reporting.

### Purpose

Performs an exact byte-for-byte comparison of two arbitrary binary files.
Reports mismatched byte positions and values up to a configurable limit.
Computes prefix and suffix matching spans and overall similarity ratio.

### Syntax

```
x86decomp diff-bytes TARGET CANDIDATE [--report REPORT] [--max-mismatches N]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET` | yes | path | Reference file (ground truth) |
| `CANDIDATE` | yes | path | File to compare against the target |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON diff report to this path |
| `--max-mismatches N` | `64` | Maximum number of mismatches to report (must be positive) |

### Output structure

The comparison result includes:

| Field | Description |
|---|---|
| `match` | `true` if both files are identical, `false` otherwise |
| `length` | Lengths: `{"target": N, "candidate": N, "common": N}` |
| `prefix` | Number of matching bytes from the start |
| `suffix` | Number of matching bytes from the end (beyond prefix) |
| `similarity` | `SequenceMatcher` ratio (0.0 – 1.0) |
| `mismatches` | Array of `{"offset": N, "target": B, "candidate": B}` up to `max_mismatches` |
| `target_sha256` | SHA-256 of target file |
| `candidate_sha256` | SHA-256 of candidate file |

### Files read

- `TARGET` — reference file
- `CANDIDATE` — comparison file

### Files written

- `--report REPORT` — structured JSON comparison report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp diff-bytes original/game.exe build/rebuilt.exe \
    --report build/diff-bytes-report.json \
    --max-mismatches 128
```

!!! tip "Report always reflects bounded analysis"
    When the number of mismatches exceeds `--max-mismatches`, the report captures
    the first N mismatches. The `match` field is still `false`. Increase the limit
    or use SHA-256 comparison (`match` derived from hash equality) as a fast pre-check.

### Related commands

- [diff-function](diff-function.md) — Compare a linked PE function to a COFF symbol
- [dynamic-validate](dynamic.md) — Differential execution comparison via Unicorn
- [symbolic-validate / angr-validate](symbolic.md) — Symbolic equivalence via Z3 or angr
