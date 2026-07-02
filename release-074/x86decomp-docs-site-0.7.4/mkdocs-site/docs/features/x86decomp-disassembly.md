---
title: x86decomp.disassembly
description: Independent Capstone-backed x86/x86-64 decoding and normalization.
original_path: features/x86decomp-disassembly.html
---

<a id="function-capstone"></a>
<a id="function-instructionrecord-to-dict"></a>
<a id="function-is-known-address"></a>
<a id="function-decode-instructions"></a>
<a id="function-control-flow-edges"></a>
<a id="function-compare-instruction-streams"></a>
<a id="function-cross-check-ghidra-instructions"></a>

Section: Source-derived feature and function reference

# x86decomp.disassembly

Independent Capstone-backed x86/x86-64 decoding and normalization.

Metadata: core · current · 7 functions/methods

**Source:** `src/x86decomp/disassembly.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `cc86a46f8c8674a6e14304158bd1d2467fb09ccbb00778c116204b0a639638b3`.

## Functions and methods

Metadata: internal · line 14

### _capstone

No function or method docstring is declared in the v0.7.4 source.

```
def _capstone() -> Any
```

**Catalog symbol:** `x86decomp.disassembly:_capstone`

Metadata: public · line 37

### InstructionRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.disassembly:InstructionRecord.to_dict`

Metadata: internal · line 52

### _is_known_address

No function or method docstring is declared in the v0.7.4 source.

```
def _is_known_address(value: int, ranges: Iterable[tuple[int, int]]) -> bool
```

**Catalog symbol:** `x86decomp.disassembly:_is_known_address`

Metadata: public · line 56

### decode_instructions

No function or method docstring is declared in the v0.7.4 source.

```
def decode_instructions(code: bytes, *, base_address: int, architecture: str = 'x86', known_address_ranges: Iterable[tuple[int, int]] = ()) -> list[InstructionRecord]
```

**Catalog symbol:** `x86decomp.disassembly:decode_instructions`

Metadata: public · line 144

### control_flow_edges

No function or method docstring is declared in the v0.7.4 source.

```
def control_flow_edges(records: list[InstructionRecord], *, base_address: int, code_size: int) -> list[tuple[int, int, str]]
```

**Catalog symbol:** `x86decomp.disassembly:control_flow_edges`

Metadata: public · line 157

### compare_instruction_streams

No function or method docstring is declared in the v0.7.4 source.

```
def compare_instruction_streams(target: bytes, candidate: bytes, *, target_base: int, candidate_base: int = 0, architecture: str = 'x86', target_known_ranges: Iterable[tuple[int, int]] = (), candidate_known_ranges: Iterable[tuple[int, int]] = ()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.disassembly:compare_instruction_streams`

Metadata: public · line 219

### cross_check_ghidra_instructions

No function or method docstring is declared in the v0.7.4 source.

```
def cross_check_ghidra_instructions(ghidra_jsonl: Path, code: bytes, *, base_address: int, architecture: str = 'x86', report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.disassembly:cross_check_ghidra_instructions`
