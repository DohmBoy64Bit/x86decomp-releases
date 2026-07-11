# Analysis: Disassembly

## `x86decomp disassemble`

Decodes bounded machine-code instructions using Capstone.

### Synopsis

```bash
x86decomp disassemble CODE --base BASE --architecture {x86,x86_64} [--report REPORT]
```

### Purpose

Reads raw machine-code bytes from `CODE`, decodes every instruction using the Capstone disassembly engine, and returns a list of instruction records. Each record includes the address, mnemonic, operand string, raw bytes, and size. This is a read-only, non-mutating static analysis operation.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `CODE` | Yes | path | Binary file containing raw machine-code bytes. |
| `--base` | No (default `0`) | int (base-prefixed) | Base virtual address added to each instruction offset. Supports decimal (`4096`), hex (`0x1000`), and octal (`0o10000`). |
| `--architecture` | No (default `x86`) | `x86` or `x86_64` | Target instruction set architecture. |

### Options

| Option | Default | Description |
|---|---|---|
| `--report` | (none) | If provided, writes the full disassembly result as JSON to this path in addition to stdout. |

### Return value

```json
{
  "instructions": [
    {
      "address": 4198400,
      "mnemonic": "push",
      "op_str": "ebp",
      "bytes": "55",
      "size": 1
    }
  ]
}
```

Each instruction record includes:

| Field | Description |
|---|---|
| `address` | `base + offset` virtual address. |
| `mnemonic` | Capstone instruction mnemonic. |
| `op_str` | Capstone operand string (may be empty). |
| `bytes` | Hex-encoded raw instruction bytes. |
| `size` | Instruction length in bytes. |

### Example

```bash
x86decomp disassemble code.bin --base 0x401000 --architecture x86 --report disasm.json
```

### Related commands

- [`crosscheck-ghidra`](#x86decomp-crosscheck-ghidra) — compare toolkit disassembly against Ghidra export

---

## `x86decomp crosscheck-ghidra`

Compares the toolkit's Capstone-based disassembly against a Ghidra instruction export.

### Synopsis

```bash
x86decomp crosscheck-ghidra INSTRUCTIONS_JSONL CODE --base BASE --architecture {x86,x86_64} [--report REPORT]
```

### Purpose

Reads a Ghidra-exported JSONL file of instructions, then independently disassembles the same raw machine-code bytes with Capstone. Compares each instruction at matching addresses and reports mismatches, extra instructions, and missing instructions. This provides an independent cross-verification of the Ghidra disassembly output.

### Arguments

| Argument | Required | Type | Description |
|---|---|---|---|
| `INSTRUCTIONS_JSONL` | Yes | path | Ghidra export file in JSON lines format (one instruction per line). |
| `CODE` | Yes | path | Raw machine-code bytes corresponding to the Ghidra export range. |
| `--base` | **Required** | int (base-prefixed) | Base address for instruction offsets. Must match the address range in the Ghidra export. |
| `--architecture` | No (default `x86`) | `x86` or `x86_64` | Target instruction set architecture. |

### Options

| Option | Default | Description |
|---|---|---|
| `--report` | (none) | If provided, writes the comparison result as JSON to this path in addition to stdout. |

### Return value

The comparison result includes match statistics and per-address mismatch details:

| Field | Description |
|---|---|
| `total_ghidra` | Number of instructions in the Ghidra export. |
| `total_capstone` | Number of instructions decoded by Capstone. |
| `matches` | Number of instructions with identical mnemonics and operands. |
| `mismatches` | Count and list of instruction-level differences. |
| `extra` | Instructions found by Capstone but not in Ghidra. |
| `missing` | Instructions in Ghidra but not decoded by Capstone. |

### Example

```bash
x86decomp crosscheck-ghidra ghidra_export.jsonl code.bin --base 0x401000 --architecture x86 --report crosscheck.json
```

### Related commands

- [`disassemble`](#x86decomp-disassemble) — standalone Capstone disassembly
- [`ghidra-export`](../ghidra/export.md) — export instructions from Ghidra
