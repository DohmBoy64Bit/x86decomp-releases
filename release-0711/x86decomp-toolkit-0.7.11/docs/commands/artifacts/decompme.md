# decompme-pack

## `x86decomp decompme-pack`

Create a decomp.me-compatible packet from a function artifact.

### Purpose

Builds a local, reviewable function packet from a validated function artifact that is structurally compatible with decomp.me. The packet intentionally does not contact decomp.me. The artifact's Ghidra human-readable listing is retained as source material and labeled non-canonical because decomp.me or compiler syntax may require target-specific conversion.

### Syntax

```
x86decomp decompme-pack ARTIFACT_DIR OUTPUT_DIR [--overwrite]
```

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `ARTIFACT_DIR` | yes | path | Function artifact directory containing `function.json` |
| `OUTPUT_DIR` | yes | path | Directory to write the decomp.me-compatible packet |

### Options

| Option | Default | Description |
|---|---|---|
| `--overwrite` | false | Allow overwriting an existing output directory |

### Files read

- `ARTIFACT_DIR/function.json` — function manifest
- `ARTIFACT_DIR/*` — disassembly, source, and listing files

### Files written

- `OUTPUT_DIR/` — decomp.me-compatible packet with manifest, scratch context, and source files

### Packet contents

| File | Description |
|---|---|
| `metadata.json` | Packet metadata with function identity |
| `scratch.txt` | Assembler scratch context (binary bytes in hex) |
| `target.s` or similar | Disassembly or decompiled source |
| `ghidra-listing.txt` | Optional Ghidra human-readable listing (labeled non-canonical) |

!!! info "No network contact"
    This command operates entirely locally. It does not upload data to decomp.me or any
    external service. Use the decomp.me web interface separately if you choose to share
    the packet.

### Example

```console
$ x86decomp decompme-pack exported/function_pe-rva-00001234/ \
    packets/function_00001234/ \
    --overwrite
```

### Related commands

- [artifact-import](artifact.md#x86decomp-artifact-import) — Import function artifact into project
- [artifact-verify](artifact.md#x86decomp-artifact-verify) — Verify function artifact integrity
