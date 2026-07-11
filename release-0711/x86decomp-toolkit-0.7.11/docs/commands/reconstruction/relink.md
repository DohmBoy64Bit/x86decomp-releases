# Relink and Hybrid Generate

Commands for relinking from a reconstruction manifest and generating hybrid
assembly projects.

## `x86decomp relink`

Relink an image from a declared reconstruction manifest.

```console
x86decomp relink MANIFEST --report REPORT
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `MANIFEST` | yes | path | JSON relink manifest |
| `--report` | no | path | Write relink report as JSON |

### Manifest Schema

The relink manifest (schema version 1) is typically produced by `x86decomp linker-plan
--write-relink-manifest`. Required fields:

| Field | Type | Description |
|---|---|---|
| `schema_version` | integer | Must be `1` |
| `linker` | string | Linker executable (e.g., `lld-link`) |
| `objects` | array of strings | COFF object and library paths |
| `output` | string | Output PE path |
| `arguments` | array of strings | Linker command-line arguments |

Optional fields:

| Field | Type | Description |
|---|---|---|
| `reference_image` | string | Path to reference PE for byte comparison |
| `map_file` | string | Path to MAP file for layout reconstruction |
| `layout_objects` | array of strings | Objects for layout correlation (defaults to `objects`) |
| `layout_profile` | string | Path to image profile for whole-image match |
| `environment` | object | Extra environment variables |
| `timeout_seconds` | integer | Linker timeout (default: 300) |
| `inherit_environment` | boolean | Inherit parent process environment (default: true) |

### Linker Invocation

The manifest `arguments` array supports template tokens:

| Token | Substitution |
|---|---|
| `{output}` | Resolved output path |
| `{objects}` | Resolved object paths expanded inline |
| `{response_file}` | Path to a generated `.rsp` file listing all objects |

All paths in the manifest are resolved relative to the manifest file parent directory.

### Post-Link Verification

On success, `relink` performs:

1. **Byte comparison** — `diff-bytes` against `reference_image`
2. **Whole-image match** — `image-match` if `layout_profile` is present
3. **Layout reconstruction** — `layout-reconstruct` if `map_file` is present

### Output

The report includes linker exit code, stdout/stderr, elapsed time, SHA-256 hashes,
byte comparison results, image match results, and layout reconstruction results.

### Example

```console
$ x86decomp relink relink.json --report relink-report.json
```

### Related Commands

- [`linker-plan`](linker.md#x86decomp-linker-plan) — generate the relink manifest
- [`diff-bytes`](../validation/diff-bytes.md) — byte-level comparison
- [`image-match`](image-match.md) — structured image comparison

---

## `x86decomp hybrid-generate`

Compatibility alias for the canonical `x86decomp hybrid generate` command.
Generates a hybrid assembly project from a source project.

```console
x86decomp hybrid-generate PROJECT OUTPUT \
    --architecture {x86,x86_64} \
    --asm-format {bytes,annotated,mnemonic} \
    --image-base 0 \
    --assembler-command-json JSON \
    --symbol-map MAP \
    --overwrite
```

!!! info "Canonical route"
    This command delegates to the canonical `hybrid` capability group.
    It is functionally identical to `x86decomp hybrid generate`.

### Arguments

| Argument | Required | Type | Default | Description |
|---|---|---|---|---|
| `PROJECT` | yes | path | — | Source project root |
| `OUTPUT` | yes | path | — | Output directory |
| `--architecture` | no | `x86`, `x86_64` | `x86` | Target machine architecture |
| `--asm-format` | no | `bytes`, `annotated`, `mnemonic` | `bytes` | Assembly output format |
| `--image-base` | no | integer | `0` | Image base address |
| `--assembler-command-json` | no | JSON string | — | Assembler invocation as JSON array |
| `--symbol-map` | no | path | — | Symbol map for extern resolution |
| `--overwrite` | no | flag | — | Overwrite existing output |

### Assembly Formats

| Format | Description |
|---|---|
| `bytes` | Raw machine-code bytes (conservative default) |
| `annotated` | Disassembly with address and evidence annotations |
| `mnemonic` | Human-readable mnemonic assembly |

### Example

```console
$ x86decomp hybrid-generate my_project build/hybrid_out \
    --architecture x86 \
    --asm-format mnemonic \
    --image-base 0x400000 \
    --symbol-map symbols.json \
    --overwrite
```

Equivalent canonical form:

```console
$ x86decomp hybrid generate my_project build/hybrid_out \
    --architecture x86 \
    --asm-format mnemonic \
    --image-base 0x400000 \
    --symbol-map symbols.json \
    --overwrite
```

### Related Commands

- [`x86decomp hybrid generate`](../canonical.md) — canonical form
- [`x86decomp asm`](../canonical.md) — assembly capability group
