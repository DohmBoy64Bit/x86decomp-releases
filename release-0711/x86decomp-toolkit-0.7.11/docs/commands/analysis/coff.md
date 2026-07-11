# Analysis: COFF Commands

Commands for inspecting, extracting, synthesizing, and resolving COFF (Common Object File Format) objects and static libraries.

---

## `x86decomp coff-inspect`

Inspects COFF object metadata, symbols, and relocations.

### Synopsis

```bash
x86decomp coff-inspect OBJECT
```

### Purpose

Parses a COFF object file and returns its full structure: file header (machine type, section count, timestamp, characteristics), section headers, symbol table, and relocation entries. This is a read-only, non-mutating static analysis operation.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `OBJECT` | Yes | path | COFF object file (`.obj`) to inspect. |

### Return fields

| Field | Description |
|---|---|
| `machine` | Target machine type (e.g., `0x014C` for x86). |
| `architecture` | `"x86"` or `"x86_64"`. |
| `section_count` | Number of sections. |
| `symbol_count` | Number of symbols in the symbol table. |
| `symbols` | Per-symbol name, value, section number, type, storage class, auxiliary records. |
| `sections` | Per-section name, size, raw data offset, relocation count, characteristics, COMDAT info. |
| `relocations` | Per-section relocation entries: virtual address, symbol table index, type. |

### Example

```bash
x86decomp coff-inspect function.obj
```

### Related commands

- [`lib-inspect`](#x86decomp-lib-inspect) — inspect static/import libraries
- [`coff-extract`](#x86decomp-coff-extract) — extract a symbol payload

---

## `x86decomp lib-inspect`

Inspects a COFF archive (static library or import library).

### Synopsis

```bash
x86decomp lib-inspect LIBRARY
```

### Purpose

Parses a COFF archive file (`.lib`) and returns its member list, linker symbol table, and per-member metadata. This is a read-only, non-mutating static analysis operation.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `LIBRARY` | Yes | path | COFF archive file (`.lib`) to inspect. |

### Return fields

| Field | Description |
|---|---|
| `member_count` | Total number of archive members. |
| `linker_symbols` | Number of symbols in the archive symbol table. |
| `members` | Per-member name, kind (`coff_object` or `import_object`), size, and offset. |

### Example

```bash
x86decomp lib-inspect libc.lib
```

### Related commands

- [`coff-inspect`](#x86decomp-coff-inspect) — inspect individual COFF objects
- [`coff-comdat-resolve`](#x86decomp-coff-comdat-resolve) — resolve COMDAT groups

---

## `x86decomp coff-extract`

Extracts one symbol's payload bytes from a COFF object.

### Synopsis

```bash
x86decomp coff-extract OBJECT SYMBOL OUTPUT [--size SIZE]
```

### Purpose

Parses the COFF object, locates the named symbol, and writes its raw data bytes to `OUTPUT`. Optionally truncates or validates against an expected `--size`.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `OBJECT` | Yes | path | COFF object file to extract from. |
| `SYMBOL` | Yes | string | Symbol name to locate in the symbol table. |
| `OUTPUT` | Yes | path | Destination file for raw symbol data bytes. Parent directories are created automatically. |

### Options

| Option | Default | Description |
|---|---|---|
| `--size` | (none) | Expected symbol size in bytes (base-prefixed). When provided, the extracted payload is truncated or validated to this size. |

### Example

```bash
x86decomp coff-extract function.obj _myFunction raw_bytes.bin --size 0x200
```

### Related commands

- [`coff-inspect`](#x86decomp-coff-inspect) — find symbol names and sizes first
- [`diff-function`](../validation/diff-function.md) — compare extracted symbol to a PE function

---

## `x86decomp coff-synthesize`

Creates a synthetic COFF object from raw machine code and relocation records.

### Synopsis

```bash
x86decomp coff-synthesize CODE SYMBOL OUTPUT --architecture {x86,x86_64} [--relocations RELOCATIONS]
```

### Purpose

Reads raw machine-code bytes from `CODE`, wraps them as a COFF object with the given symbol name, and writes the complete COFF to `OUTPUT`. Optionally applies relocation entries from a JSON file. The output machine type is `0x014C` for x86 and `0x8664` for x86-64.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `CODE` | Yes | path | File containing raw machine-code bytes for the `.text` section. |
| `SYMBOL` | Yes | string | Symbol name for the synthesized function. |
| `OUTPUT` | Yes | path | Destination path for the generated COFF object. |

### Options

| Option | Default | Description |
|---|---|---|
| `--architecture` | `x86` | `x86` or `x86_64`. Determines the COFF machine type. |
| `--relocations` | (none) | JSON file containing relocation entries. Each entry must have `offset` (int), `type` (int), and optionally `symbol_index` (int, default 0) and `symbol_name` (string). |

### Relocation entry schema

```json
[
  {
    "offset": 1,
    "type": 20,
    "symbol_index": 0,
    "symbol_name": "__imp__ExitProcess@4"
  }
]
```

### Example

```bash
x86decomp coff-synthesize code.bin _myFunc synth.obj --architecture x86 --relocations relocs.json
```

### Related commands

- [`coff-inspect`](#x86decomp-coff-inspect) — verify the synthesized object
- [`coff-extract`](#x86decomp-coff-extract) — extract a symbol from a real COFF object

---

## `x86decomp coff-comdat-resolve`

Resolves COMDAT groups across multiple COFF objects.

### Synopsis

```bash
x86decomp coff-comdat-resolve OBJECTS... [--report REPORT]
```

### Purpose

Parses all supplied COFF objects, identifies COMDAT sections (sections with the `IMAGE_SCN_LNK_COMDAT` flag), and resolves duplicate COMDAT groups by selecting one definition per group. This is useful for understanding which objects contribute which COMDAT sections in a link.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `OBJECTS...` | Yes (1+) | paths | One or more COFF object files to analyze. |

### Options

| Option | Default | Description |
|---|---|---|
| `--report` | (none) | If provided, writes the resolved COMDAT result as JSON to this path in addition to stdout. |

### Example

```bash
x86decomp coff-comdat-resolve obj1.obj obj2.obj obj3.obj --report comdat_report.json
```

### Related commands

- [`coff-inspect`](#x86decomp-coff-inspect) — inspect individual objects for COMDAT sections
- [`linker-plan`](../reconstruction/linker.md) — build a linker reconstruction plan using COFF objects
