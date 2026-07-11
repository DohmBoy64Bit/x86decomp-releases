# Analysis: PE and PDB

## `x86decomp inspect-pe`

Parses PE32 or PE32+ metadata from a Windows PE binary.

### Synopsis

```bash
x86decomp inspect-pe BINARY
```

### Purpose

Parses the full PE structure: DOS header, NT headers, file header, optional header, section headers, data directories (imports, exports, relocations, resources, TLS, debug, etc.), and section data bounds. Returns the complete `PEImage.to_dict()` representation. This is a read-only, non-mutating static analysis operation.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `BINARY` | Yes | path | PE32 or PE32+ file to parse. |

### Options

None.

### Return fields (selected)

| Field | Description |
|---|---|
| `architecture` | `"x86"` or `"x86_64"`. |
| `file_sha256` | SHA-256 of the entire file. |
| `machine` | PE machine type (e.g., `0x014C` for x86, `0x8664` for x86-64). |
| `image_base` | Preferred load address. |
| `entry_rva` | Entry point RVA. |
| `number_of_sections` | Section count. |
| `size_of_image` | Total image size in memory. |
| `characteristics` | File characteristics flags. |
| `sections` | Per-section name, virtual address, virtual size, raw size, characteristics. |
| `imports` | Imported DLLs and symbols. |
| `exports` | Exported symbols (if any). |
| `relocations` | Base relocations (if present). |

### Sibling command

The same function is available as the compatibility alias:
```bash
x86decomp project inspect-pe BINARY
```

### Example

```bash
x86decomp inspect-pe target.exe
```

```json
{
  "architecture": "x86",
  "file_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "machine": 332,
  "image_base": 4194304,
  "entry_rva": 4096,
  "number_of_sections": 4,
  "size_of_image": 655360,
  "characteristics": 271,
  "sections": [
    {"name": ".text", "virtual_address": 4096, "virtual_size": 81920, "raw_size": 81920, "characteristics": 1610612768}
  ],
  "imports": [{"dll": "KERNEL32.dll", "symbols": ["GetProcAddress", "LoadLibraryA"]}]
}
```

### Related commands

- [`pdb-inspect`](#x86decomp-pdb-inspect) — inspect companion PDB
- [`metadata-scan`](metadata.md) — recover MSVC RTTI/vtable metadata
- [`init`](../project/init-verify.md#x86decomp-init) — uses `inspect-pe` internally to auto-detect architecture

---

## `x86decomp pdb-inspect`

Inspects an MSF 7.0 PDB file and optionally cross-references it against a companion PE.

### Synopsis

```bash
x86decomp pdb-inspect PDB [--pe PE_PATH]
```

### Purpose

Parses an MSF 7.0 PDB (Program Database) file. The MSF 7.0 format is the debug information container used by modern MSVC toolchains. When `--pe` is supplied, the parser matches DBI stream source file information, section contributions, and public/global symbol records against the corresponding PE image.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PDB` | Yes | path | MSF 7.0 PDB file to parse. |
| `--pe` | No | path | Companion PE file. When provided, DBI and symbol records are matched against the PE sections and image. |

### Return fields (selected)

| Field | Description |
|---|---|
| `pdb_header` | MSF SuperBlock: block size, free block map, number of directory bytes. |
| `dbi` | Debug information stream: module list, section contributions, source info, stream sizes. |
| `dbi.source_info.unique_files` | Set of source filenames referenced in the DBI stream. |
| `public_symbols` | Public symbol records (name, section, offset) if `--pe` provided. |
| `global_symbols` | Global symbol records if `--pe` provided. |
| `sections` | Section contribution records mapped to PE sections if `--pe` provided. |
| `type_info` | Type information stream summary. |

### Example

```bash
x86decomp pdb-inspect target.pdb --pe target.exe
```

### Related commands

- [`inspect-pe`](#x86decomp-inspect-pe) — parse the PE binary
- [`metadata-scan`](metadata.md) — recover MSVC RTTI, vtables, unwind, TLS metadata
- [`target-pack-infer`](../project/target-pack.md#x86decomp-target-pack-infer) — include PDB evidence in a target pack
