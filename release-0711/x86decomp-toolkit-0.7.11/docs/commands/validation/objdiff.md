# objdiff-run

Run an objdiff-compatible comparison manifest.

### Purpose

Executes the external `objdiff-cli` tool (or a declared alternative) with the
arguments, target, and candidate files specified in a version-1 manifest.
objdiff's CLI/configuration evolves independently — this adapter executes an
explicit argument array, captures provenance, and imports the declared output
without hard-coding unstable flags.

### Syntax

```
x86decomp objdiff-run MANIFEST [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `MANIFEST` | yes | path | JSON manifest (schema version 1) specifying target, candidate, and objdiff arguments |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON report capturing objdiff provenance and output to this path |

### Manifest format

The manifest is a JSON document with schema version 1:

```json
{
    "schema_version": 1,
    "executable": "objdiff-cli",
    "target": "original/Game.exe",
    "candidate": "build/Game.exe",
    "arguments": [
        "diff",
        "--target", "{target}",
        "--candidate", "{candidate}",
        "--output", "{output}"
    ]
}
```

| Field | Required | Description |
|---|---|---|
| `schema_version` | yes | Must be `1` |
| `executable` | no | objdiff executable name or path (default: `objdiff-cli`); resolved from PATH if not absolute |
| `target` | yes | Path to the reference/ground-truth object or binary |
| `candidate` | yes | Path to the rebuilt object or binary |
| `arguments` | yes | Non-empty array of argument strings to pass to objdiff |

### Argument tokens

The `arguments` array supports these substitution tokens:

| Token | Replaced with |
|---|---|
| `{target}` | Resolved absolute path to the target file |
| `{candidate}` | Resolved absolute path to the candidate file |
| `{output}` | Path to a temporary output file in the ephemeral work directory |
| `{workdir}` | Path to the ephemeral work directory |

At minimum, `{target}` and `{candidate}` must appear in the arguments.

### Execution

1. Resolves the `executable` from PATH or an absolute path
2. Verifies target and candidate files exist
3. Creates a temporary work directory
4. Expands argument tokens
5. Runs objdiff as a subprocess with a timeout
6. Captures exit code, stdout, stderr, and the output file if one was declared
7. Records provenance (command line, timings, working directory) in the result

### Output structure

| Field | Description |
|---|---|
| `exit_code` | objdiff process exit code |
| `elapsed` | Wall-clock and CPU time in seconds |
| `stdout` | Captured standard output |
| `stderr` | Captured standard error |
| `output` | Contents of the declared output file (if `{output}` was used and the file exists) |
| `manifest` | Copy of the manifest used |
| `resolved_executable` | Absolute path to the objdiff binary that was executed |

### Files read

- `MANIFEST` — objdiff manifest JSON
- Target and candidate files referenced in the manifest

### Files written

- `--report REPORT` — structured JSON run report
- Declared output file via `{output}` token (may be in temporary directory)

### Exit behavior

- Exit 0 on success with JSON result on stdout (even if objdiff itself returns non-zero)
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 with `ExternalToolError` if objdiff executable is unavailable
- Exit 2 with `ContractError` if the manifest is invalid or target/candidate are missing

### Example

```console
$ x86decomp objdiff-run objdiff-manifest.json --report build/objdiff-report.json
```

With manifest:

```json
{
    "schema_version": 1,
    "executable": "objdiff-cli",
    "target": "original/Game.exe",
    "candidate": "build/Game.exe",
    "arguments": [
        "diff",
        "--target", "{target}",
        "--candidate", "{candidate}",
        "--output", "{output}",
        "--format", "json"
    ]
}
```

!!! note "objdiff is an external tool"
    `objdiff-run` is a real external-tool boundary, not a fake diff. The adapter
    does not hard-code objdiff flags — it passes through any argument array you
    declare. This means the manifest is version-bound to your installed objdiff
    CLI. Review the objdiff help (`objdiff-cli --help`) before writing a manifest.

!!! warning "Version coupling"
    objdiff's CLI changes between versions. If your manifest arguments are rejected
    by objdiff, check your objdiff version and update the argument array. The
    toolkit does not validate argument compatibility.

### Related commands

- [diff-bytes](diff-bytes.md) — Direct byte-for-byte comparison (no external tool)
- [compiler-lab](../compilation/compiler-lab.md) — Automated matrix comparison using compile+diff
- [diff-function](diff-function.md) — PE function to COFF symbol comparison
