# Analysis: Metadata Scan

## `x86decomp metadata-scan`

Recovers bounded MSVC metadata from a PE image: RTTI, vtables, unwind info, TLS callbacks, and initializer tables.

### Synopsis

```bash
x86decomp metadata-scan PE [--object OBJ...] [--map MAP] [--report REPORT]
```

### Purpose

Scans a PE image for MSVC-generated metadata structures using pattern matching and section analysis. Recovers:

- **RTTI**: Complete object locators, type descriptors, class hierarchy descriptors, and base class arrays.
- **Vtables**: Virtual function tables identified via RTTI cross-references.
- **Unwind info**: Exception handler and unwind data (`.pdata`/`.xdata`) for both x86 and x86-64.
- **TLS**: Thread-local storage callbacks and data directories.
- **Initializers**: `__xc_a`/`__xc_z` initializer arrays and `__xi_a`/`__xi_z` C++ static initializers.

Optional COFF objects and linker map provide additional cross-reference evidence that strengthens type recovery.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `PE` | Yes | path | PE32 or PE32+ image to scan for MSVC metadata. |

### Options

| Option | Default | Description |
|---|---|---|
| `--object` | `[]` | COFF object path. Repeatable. Each object's symbols and sections are correlated against detected metadata. |
| `--map` | (none) | MSVC-compatible linker map (`.map` file). Provides symbol-to-address mappings that anchor metadata locations. |
| `--report` | (none) | If provided, writes the full metadata analysis result as JSON to this path in addition to stdout. |

### Return fields (selected)

| Field | Description |
|---|---|
| `rtti` | Recovered RTTI structures: locators, type descriptors, hierarchies. |
| `vtables` | Virtual function tables with their addresses and class associations. |
| `unwind` | Exception handler entries and unwind opcodes. |
| `tls` | TLS callback addresses and data directory info. |
| `initializers` | `__xc_a`/`__xc_z` and `__xi_a`/`__xi_z` arrays with function pointers. |

### Example

```bash
x86decomp metadata-scan target.exe \
    --object obj1.obj --object obj2.obj \
    --map target.map \
    --report metadata.json
```

### Related commands

- [`inspect-pe`](pe-pdb.md#x86decomp-inspect-pe) — basic PE structure
- [`pdb-inspect`](pe-pdb.md#x86decomp-pdb-inspect) — PDB type information
- [`cpp-recover`](../reconstruction/cpp-recover.md) — recover C++ class models from metadata
- [`vtable recover`](../reconstruction/cpp-recover.md) — recover vtables from image and metadata report
