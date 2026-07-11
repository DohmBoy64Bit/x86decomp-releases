# Static Analysis

Static analysis is the extraction of facts from binaries without execution. The toolkit
provides PE parsing, instruction decoding, COFF analysis, MSVC metadata scanning, linker
map analysis, and COMDAT resolution — all producing evidence-backed reports.

## PE Parsing

Parse PE32 and PE32+ metadata:

```bash
x86decomp inspect-pe --binary original/game.exe
```

### Output Includes

- **DOS and PE headers**: Machine type, timestamp, subsystem.
- **Section table**: Name, virtual address/size, raw offset/size, characteristics.
- **Data directories**: Export, import, resource, exception, TLS, debug, etc.
- **Import table**: DLLs and imported symbols with ordinals.
- **Export table**: Exported symbols with ordinals and RVAs.
- **Base relocations**: Relocation blocks and entries.
- **Debug directory**: CodeView, POGO, and other debug entries.
- **TLS callbacks**: Thread-local storage callback addresses.
- **Load config**: Security cookie, SEH table, Guard CF metadata.
- **Resources**: Embedded resource tree.

### PE32+ (x86-64) Extensions

- 64-bit optional header (`PE32_PLUS_MAGIC = 0x020B`).
- Runtime function table (`.pdata` section) for exception unwind info.
- 64-bit TLS directory.
- 64-bit import thunks.

## PDB Inspection

When debug symbols are available:

```bash
x86decomp pdb-inspect --pdb original.pdb --pe original/game.exe
```

The `--pe` argument is optional and enables cross-checking PDB sections against PE sections.
PDB inspection extracts:

- **Stream directory**: Named streams and their sizes.
- **DBI stream**: Module list, section contributions, source file info.
- **TPI/IPI streams**: Type records (class, struct, enum, function signature, pointer, array).
- **Public/global symbol streams**: Function and data symbols with RVAs.
- **Section map**: PE section-to-PDB contribution mapping.

## Instruction Decoding

Decode machine code to structured instruction records using Capstone:

```bash
x86decomp disassemble \
  --code "558BEC83EC105356578B7D088B450C" \
  --base-address 0x401000 \
  --architecture x86
```

### Instruction Record

```json
{
  "address": 4198400,
  "address_hex": "0x401000",
  "offset": 0,
  "size": 2,
  "bytes_hex": "55",
  "mnemonic": "push",
  "op_str": "ebp",
  "normalized": "push ebp",
  "branch_target": null,
  "fallthrough": 4198402
}
```

Normalization rewrites ambiguous operand forms (e.g., `C7 45 FC 05 00 00 00` →
`mov dword ptr [ebp - 4], 5`) so cross-tool comparisons are stable.

### Branch Tracking

For each instruction, the decoder reports:

- `branch_target`: Address of direct jump/call target, or `null`.
- `fallthrough`: Address of next sequential instruction, or `null` for unconditional
  jumps and returns.

### Known Address Ranges

Optionally provide known address ranges for resolution:

```bash
x86decomp disassemble \
  --code <hex> \
  --base-address 0x401000 \
  --known-ranges "0x401000-0x401100,0x402000-0x402200"
```

## COFF Analysis

### Inspect

```bash
x86decomp coff-inspect --input build/objects/main.obj
```

Reports:

- Machine type, timestamp, characteristics.
- Section headers and raw data sizes.
- Symbol table with storage class, section number, and auxiliary records.
- Relocation table per section.

### Extract Symbol Payload

```bash
x86decomp coff-extract \
  --input build/objects/main.obj \
  --symbol "_ProcessInput@4" \
  --output extracted.bin
```

Extracts raw bytes for a COFF symbol, accounting for section-relative addressing and
alignment.

### Synthesize COFF

Create COFF objects from raw code and relocation data:

```bash
x86decomp coff-synthesize \
  --output synthetic.obj \
  --machine x86 \
  --section .text \
  --code "<hex>" \
  --relocations '[{"offset": 4, "type": "IMAGE_REL_I386_DIR32", "symbol": "_global_var"}]'
```

## COFF Archive Inspection

Parse `.lib` archives:

```bash
x86decomp coff-archive-inspect --input msvcrt.lib
```

Reports:
- Archive member list (object names).
- Linker member maps (symbol-to-member index).
- Long-name member table.

## MSVC Metadata Scanning

Scan a PE for embedded MSVC metadata structures:

```bash
x86decomp metadata-scan --pe original/game.exe --report metadata.json
```

### Detected Structures

| Structure | Location | Purpose |
|---|---|---|
| **RTTI** | `.rdata` or `.data` | `RTTICompleteObjectLocator`, `RTTIClassHierarchyDescriptor`, `RTTIBaseClassDescriptor` chains |
| **VTables** | `.rdata` | Virtual function tables (arrays of function pointers) |
| **Unwind info** | `.pdata` (PE32+) or embedded | Exception handler chains, unwind opcodes |
| **TLS** | PE data directory | Thread-local storage initializers and callbacks |
| **Type descriptors** | `.rdata` | `type_info` structures for `dynamic_cast`/`typeid` |
| **Throw info** | `.rdata` | `ThrowInfo`, `CatchableType` arrays for C++ exceptions |
| **Security cookie** | Load config | `/GS` buffer overflow protection cookie |

### RTTI Chain Walking

The scanner follows RTTI chains:

```
RTTICompleteObjectLocator
  └─ TypeDescriptor (mangled class name)
  └─ RTTIClassHierarchyDescriptor
       ├─ RTTIBaseClassDescriptor (this class)
       └─ RTTIBaseClassDescriptor (base class)
```

Each link provides evidence about class size, vtable offset, and inheritance relationships.

## Linker Map Analysis

Parse MSVC MAP files:

```bash
x86decomp linker-plan \
  --pe original/game.exe \
  --map original/game.map \
  --objects build/objects/*.obj
```

The MAP parser extracts:

- **Preferred load address**: The image base at link time.
- **Timestamp**: When the MAP was produced.
- **Section contributions**: Object file → section → RVA → size.
- **Public symbols**: Symbol name → RVA mapping.

See [Linker Reconstruction](linker-reconstruction.md) for the full reconstruction workflow.

## COMDAT Resolution

COMDAT sections implement C++ inline functions and template instantiations. Multiple objects
may define the same COMDAT; the linker picks one based on selection rules.

```bash
# Handled internally by linker-plan; not a standalone CLI command.
# The COMDAT resolution logic is in coff.py:resolve_comdats()
```

The resolver:

1. Collects all COMDAT symbols across supplied objects.
2. Groups symbols by COMDAT selection key.
3. Applies selection rules: pick largest, pick first, associative, etc.
4. Records the selection in the reconstruction plan.

## Cross-Check: Toolkit vs Ghidra

Validate toolkit disassembly against Ghidra's output:

```bash
x86decomp crosscheck-ghidra \
  --code <hex> \
  --base-address 0x401000 \
  --ghidra-export ghidra-export.json \
  --report crosscheck-report.json
```

This compares instruction boundaries, mnemonics, operand normalization, and branch targets.
Differences are categorized:

| Category | Severity | Example |
|---|---|---|
| `mnemonic_mismatch` | High | Toolkit decodes `mov`, Ghidra decodes `lea` |
| `operand_mismatch` | Medium | Same mnemonic, different operand formatting |
| `boundary_mismatch` | Critical | Different instruction boundaries |
| `normalized_match` | None | Different operand text, same canonical form |
| `branch_target_mismatch` | Medium | Different computed branch targets |

!!! danger "Boundary mismatches"
    A boundary mismatch means the two tools disagree on where one instruction ends and the
    next begins. All subsequent comparisons for that function are invalid. This usually
    indicates a data-in-code region or an unsupported instruction prefix.

## Evidence Integration

Static analysis results feed the evidence system:

```bash
# PE parsing as binary_bytes evidence
x86decomp evidence-add --project . \
  --kind binary_bytes \
  --source "PE32 header for game.exe" \
  --locator "pe:game.exe:offset:0:size:1024" \
  --assertion "PE header identifies x86 architecture, 4 sections, entry at 0x401000" \
  --independent-group "pe-parser" \
  --file "./reports/pe-headers.bin"

# Disassembly as static_analysis evidence
x86decomp evidence-add --project . \
  --kind static_analysis \
  --source "Capstone 5.0.1 x86 decoding" \
  --locator "disasm:pe:game.exe:rva:0x401000:size:256" \
  --assertion "Function at 0x401000 contains 42 instructions, stdcall convention" \
  --independent-group "capstone-disasm" \
  --file "./reports/disasm-401000.json"

# Metadata scan as static_analysis evidence
x86decomp evidence-add --project . \
  --kind static_analysis \
  --source "MSVC metadata scanner" \
  --locator "metadata:pe:game.exe:vtable:0x41A000" \
  --assertion "VTable at 0x41A000 has 5 virtual function entries" \
  --independent-group "msvc-metadata" \
  --file "./reports/vtable-41A000.json"
```

## Tool Snapshots

Record the current tool environment:

```bash
x86decomp snapshot-tools --output tools.json --ghidra-home /opt/ghidra
```

Captures paths and versions of: Python, Java, GCC, Clang, lld-link, objdiff-cli, and
`analyzeHeadless` (if `--ghidra-home` is provided).
