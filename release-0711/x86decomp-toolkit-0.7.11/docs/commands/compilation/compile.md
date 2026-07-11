# compile / compile-worker

## `x86decomp compile`

Compile one source file deterministically under a declared compiler profile.

### Purpose

Runs an external compiler as specified by a JSON compiler profile, capturing
output hash, tool versions, environment, and timing into a structured
compilation report. Designed for matching decompilation workflows where
compiler identity and exact argument sets must be reproduced.

### Syntax

```
x86decomp compile PROFILE SOURCE OUTPUT [--report REPORT] [--extra-arg ARG]... [--cache DIR]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROFILE` | yes | path | JSON compiler profile (schema version 1 or 2) |
| `SOURCE` | yes | path | Source file to compile |
| `OUTPUT` | yes | path | Output file path (directory must exist or be creatable) |

### Options

| Option | Default | Description |
|---|---|---|
| `--report REPORT` | none | Write structured JSON compilation report to this path |
| `--extra-arg ARG` | `[]` | Append an extra argument to the profile's argument list; repeatable |
| `--cache DIR` | none | Content-addressed compiler cache directory; avoids redundant builds |

### Profiles

The compiler profile is a JSON document (schema version 1 or 2) with these required fields:

```
schema_version, id, executable, arguments, timeout_seconds, output_kind
```

`arguments` must include the `{source}` and `{output}` substitution tokens.

### Files read

- `PROFILE` — compiler profile JSON
- `SOURCE` — source file to compile

### Files written

- `OUTPUT` — compiler output (object file, binary, etc.)
- `--report REPORT` — structured JSON compilation report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp compile profiles/msvc-2019-x86-release.json src/candidate.c build/candidate.obj \
    --report build/compile-report.json \
    --extra-arg /O2 --extra-arg /Oi \
    --cache .compiler-cache
```

---

## `x86decomp compile-worker`

Run a bounded isolation compilation worker — local or containerized.

### Purpose

Copies declared inputs into an ephemeral workspace and invokes the compiler
profile through a bounded local or container worker. Local mode is not a
security boundary; container mode is the production isolation option.

### Syntax

```
x86decomp compile-worker PROFILE SOURCE OUTPUT [--isolation {local_bounded,container}] [--container-image IMAGE] [--cache DIR] [--report REPORT]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROFILE` | yes | path | JSON compiler profile (same format as `compile`) |
| `SOURCE` | yes | path | Source file (must be a regular file, not a symlink) |
| `OUTPUT` | yes | path | Output file path (parent directory created if needed) |

### Options

| Option | Default | Description |
|---|---|---|
| `--isolation {local_bounded,container}` | `local_bounded` | Isolation strategy for the compilation worker |
| `--container-image IMAGE` | none | Container image name; required when `--isolation container` |
| `--cache DIR` | none | Content-addressed compiler cache directory |
| `--report REPORT` | none | Write structured JSON compilation report to this path |

### Accepted values

- `--isolation`: `local_bounded` runs in a temporary workspace on the host; `container` runs in the specified container image
- `--container-image`: any valid container image reference

### Files read

- `PROFILE` — compiler profile JSON
- `SOURCE` — source file copied to ephemeral workspace

### Files written

- `OUTPUT` — compiler output, copied from ephemeral workspace
- `--report REPORT` — structured JSON compilation report

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr
- Exit 2 on runtime error with JSON `{"error": ..., "message": ...}` on stderr

### Example

```console
$ x86decomp compile-worker profiles/msvc-2019-x86-release.json src/candidate.c build/candidate.obj \
    --isolation container \
    --container-image ghcr.io/example/msvc-2019:latest \
    --cache .compiler-cache \
    --report build/worker-report.json
```

!!! warning "Local mode is not a security boundary"
    `--isolation local_bounded` executes the compiler directly on the host within a
    temporary directory. Use `--isolation container` when compiling untrusted source
    or profiles.

### Related commands

- [compiler-lab](compiler-lab.md) — Matrix experiments across multiple profiles and arguments
- [toolchain-register / toolchain-verify](toolchains.md) — Register and verify compiler executables
