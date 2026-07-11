# Reproducibility Commands

Create and verify reproducibility manifests for declared inputs. A missing external tool is never treated as a successful reproduction.

---

## `x86decomp reproduce-create`

Create a reproducibility manifest for declared inputs.

### Purpose

Builds a JSON reproducibility manifest that records the current project state, target pack identity, project structure verification, tool versions, platform metadata, Python environment, and content-addressed storage digests. The manifest declares what is required to reproduce the project's current state. Required external tools can be declared explicitly; their presence and versions are queried but their absence is recorded, not fabricated.

### Syntax

```
x86decomp reproduce-create PROJECT OUTPUT [--required-tool TOOL]...
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root directory |
| `OUTPUT` | yes | path | Output path for the JSON reproducibility manifest |

### Options

| Option | Default | Description |
|---|---|---|
| `--required-tool TOOL` | `[]` | Declare an external tool required for reproduction; repeatable |

### Manifest contents

| Section | Description |
|---|---|
| `project` | Project verification and state check results |
| `target_pack` | Target pack identity and verification |
| `tools` | Declared and discovered tool versions with availability |
| `platform` | OS, architecture, Python version, and runtime metadata |
| `content_store` | Content-addressed storage digest and integrity verification |
| `missing` | Tools declared as required but not available |

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on argument error with argparse diagnostics on stderr

### Example

```console
$ x86decomp reproduce-create ./my-project reproduce/manifest.json \
    --required-tool "msvc-2019-x86-cl" \
    --required-tool "ghidra"
```

---

## `x86decomp reproduce-verify`

Verify a reproducibility manifest and all input hashes.

### Purpose

Re-checks every declaration in a reproducibility manifest: verifies the project structure and state, re-validates the target pack, confirms tool availability and version consistency, and checks content-addressed storage integrity. Reports any deviation from the recorded manifest.

### Syntax

```
x86decomp reproduce-verify PROJECT MANIFEST
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PROJECT` | yes | path | Project root directory |
| `MANIFEST` | yes | path | JSON reproducibility manifest to verify (from `reproduce-create`) |

### Files read

- `PROJECT` — project directory tree
- `MANIFEST` — JSON reproducibility manifest

### Verification checks

| Check | Description |
|---|---|
| Project structure | Project verification and state check |
| Target pack | Target pack integrity verification |
| Tools | Declared tools exist and versions match |
| Content store | Content-addressed storage digest integrity |
| Platform | Platform metadata consistency |

### Exit behavior

- Exit 0 on success with JSON result on stdout
- Exit 2 on any verification failure or missing tool, with structured result

### Example

```console
$ x86decomp reproduce-verify ./my-project reproduce/manifest.json
```

### Related commands

- [release-gate](release-gate.md) — Evaluate release acceptance contracts
- [convergence-analyze](convergence.md) — Measure image convergence
