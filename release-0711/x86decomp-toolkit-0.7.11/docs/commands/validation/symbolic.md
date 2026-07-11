# symbolic-validate / angr-validate / symbolic-memory-validate

## `x86decomp symbolic-validate`

Symbolically compare two bounded binary functions using Z3.

### Purpose

Lifts two x86 or x86-64 binary blobs into symbolic expressions, constructs an
equivalence query with symbolic inputs fed through both implementations, and
proves or disproves output equivalence using Z3. Bounded: limited to the
instruction subset the executor models, explored paths, and selected output
registers. A successful `UNSAT` result means no path diverges on the observed
outputs — not that the functions are identical in all respects.

### Syntax

```
x86decomp symbolic-validate TARGET CANDIDATE
    [--architecture {x86,x86_64}]
    [--input-register REG]...
    [--stack-argument-words N]
    [--output-register REG]...
    [--max-steps N]
    [--max-paths N]
    [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET` | yes | path | Reference binary blob |
| `CANDIDATE` | yes | path | Candidate binary blob to validate |

### Options

| Option | Default | Description |
|---|---|---|
| `--architecture {x86,x86_64}` | `x86` | Target instruction set architecture |
| `--input-register REG` | `[]` | Register to mark as symbolic input (repeatable; e.g. `eax`, `ecx`) |
| `--stack-argument-words N` | `0` | Number of 4-byte stack argument words to mark as symbolic (x86) or 8-byte (x86_64) |
| `--output-register REG` | none | Register to compare after execution (repeatable); if omitted, all general-purpose registers are compared |
| `--max-steps N` | `1000` | Maximum execution steps per path |
| `--max-paths N` | `64` | Maximum execution paths to explore |
| `--report REPORT` | none | Write structured JSON validation report to this path |

### Dependencies

Requires Capstone and z3-solver. Install with:

```console
$ pip install x86decomp-toolkit[symbolic]
```

### Accepted values

- `--architecture`: `x86` or `x86_64`
- `--input-register`: Standard x86/x86_64 register names (case-insensitive). Repeat for multiple registers.
- `--output-register`: Same register set. If not specified, the result compares all modeled general-purpose registers.
- `--max-steps`, `--max-paths`: Positive integers controlling the exploration bound
- `--stack-argument-words`: Non-negative integer

### Output

| Field | Description |
|---|---|
| `result` | `equivalent` if Z3 proved equivalence, `divergent` if a counterexample was found, `bounded_by_steps` or `bounded_by_paths` if exploration was truncated |
| `counterexample` | If divergent: concrete input values and output register values for both sides that differ |
| `steps_explored` | Number of steps taken before the result |
| `paths_explored` | Number of paths explored |

### Files read

- `TARGET` — reference binary blob
- `CANDIDATE` — candidate binary blob

### Files written

- `--report REPORT` — structured JSON validation report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 with `ExternalToolError` if Capstone or z3-solver is not installed

### Example

```console
$ x86decomp symbolic-validate original/math_func.bin build/math_func.bin \
    --architecture x86 \
    --input-register eax --input-register ecx \
    --stack-argument-words 1 \
    --output-register eax --output-register edx \
    --max-steps 500 --max-paths 32 \
    --report build/symbolic-report.json
```

---

## `x86decomp angr-validate`

Compare binary functions with the optional angr backend.

### Purpose

Same interface and semantics as `symbolic-validate`, but uses angr and claripy
as the symbolic execution engine instead of the built-in Z3 executor. angr
handles a broader instruction set and may explore different paths, but results
are scoped identically to the selected architecture, input/output registers,
path/step limits, and code blobs.

### Syntax

```
x86decomp angr-validate TARGET CANDIDATE
    [--architecture {x86,x86_64}]
    [--input-register REG]...
    [--stack-argument-words N]
    [--output-register REG]...
    [--max-steps N]
    [--max-paths N]
    [--report REPORT]
```

### Arguments and options

Identical to [`symbolic-validate`](#x86decomp-symbolic-validate). All arguments, options, and
defaults are the same.

### Dependencies

Requires angr. Install with:

```console
$ pip install x86decomp-toolkit[symbolic] angr
```

### Example

```console
$ x86decomp angr-validate original/math_func.bin build/math_func.bin \
    --architecture x86 \
    --input-register eax --input-register ecx \
    --output-register eax \
    --max-steps 500 --max-paths 32 \
    --report build/angr-report.json
```

---

## `x86decomp symbolic-memory-validate`

angr comparison with symbolic memory region bases and alias constraints.

### Purpose

Extends `angr-validate` with symbolic memory aliasing: the harness specifies
memory regions whose base addresses are treated as symbolic, and the comparison
checks equivalence under all possible alias relationships between those
regions. This catches bugs where two pointers might independently alias the
same memory in one implementation but not the other.

### Syntax

```
x86decomp symbolic-memory-validate TARGET CANDIDATE HARNESS [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `TARGET` | yes | path | Reference binary blob |
| `CANDIDATE` | yes | path | Candidate binary blob |
| `HARNESS` | yes | path | JSON harness specifying symbolic memory regions and alias constraints |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON validation report to this path |

### Dependencies

Requires angr and claripy. Install with:

```console
$ pip install x86decomp-toolkit[symbolic] angr
```

### Harness format

The JSON harness defines memory regions with symbolic base addresses. The angr
backend enumerates all alias relationships (which regions may overlap) and
checks equivalence for each case.

### Files read

- `TARGET` — reference binary blob
- `CANDIDATE` — candidate binary blob
- `HARNESS` — JSON harness with symbolic memory declarations

### Files written

- `--report REPORT` — structured JSON validation report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr
- Exit 2 with `ExternalToolError` if angr is not installed

### Example

```console
$ x86decomp symbolic-memory-validate original/func.bin build/func.bin harnesses/memory-harness.json \
    --report build/symbolic-memory-report.json
```

!!! note "Default vs. angr backend"
    `symbolic-validate` uses the built-in Capstone+Z3 executor, which is simpler,
    faster, and fully deterministic. `angr-validate` and `symbolic-memory-validate`
    use angr for broader instruction coverage and memory aliasing but are
    non-deterministic (path explosion heuristics). Use the built-in backend first;
    fall back to angr when it rejects unsupported instructions or memory operand types.

!!! warning "Equivalence scope"
    A successful `UNSAT` (equivalent) result is only meaningful for the modeled
    instruction subset, symbolic inputs, explored paths, and selected output
    registers. It does not prove the functions are identical under all possible
    inputs, memory states, or untracked side effects (flags, memory writes outside
    observed regions).

### Related commands

- [diff-bytes](diff-bytes.md) — Byte-for-byte comparison
- [diff-function](diff-function.md) — PE function to COFF symbol comparison
- [dynamic-validate](dynamic.md) — Differential execution via Unicorn emulation
