---
title: x86decomp.disassembly
description: Independent Capstone-backed x86/x86-64 decoding and normalization.
---

# `x86decomp.disassembly`

Independent Capstone-backed x86/x86-64 decoding and normalization.

**Area:** Toolkit  
**Source:** `src/x86decomp/disassembly.py`  
**SHA-256:** `cc86a46f8c8674a6e14304158bd1d2467fb09ccbb00778c116204b0a639638b3`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-capstone"></a>

### `_capstone`

No function or method docstring is declared in the 0.7.5 source.

```python
def _capstone() -> Any
```

**Catalog symbol:** `x86decomp.disassembly:_capstone`  
**Visibility:** internal  
**Source line:** 14

<a id="function-instructionrecord-to-dict"></a>

### `InstructionRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def InstructionRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.disassembly:InstructionRecord.to_dict`  
**Visibility:** public  
**Source line:** 37

<a id="function-is-known-address"></a>

### `_is_known_address`

No function or method docstring is declared in the 0.7.5 source.

```python
def _is_known_address(value: int, ranges: Iterable[tuple[int, int]]) -> bool
```

**Catalog symbol:** `x86decomp.disassembly:_is_known_address`  
**Visibility:** internal  
**Source line:** 52

<a id="function-decode-instructions"></a>

### `decode_instructions`

No function or method docstring is declared in the 0.7.5 source.

```python
def decode_instructions(code: bytes, *, base_address: int, architecture: str='x86', known_address_ranges: Iterable[tuple[int, int]]=()) -> list[InstructionRecord]
```

**Catalog symbol:** `x86decomp.disassembly:decode_instructions`  
**Visibility:** public  
**Source line:** 56

<a id="function-control-flow-edges"></a>

### `control_flow_edges`

No function or method docstring is declared in the 0.7.5 source.

```python
def control_flow_edges(records: list[InstructionRecord], *, base_address: int, code_size: int) -> list[tuple[int, int, str]]
```

**Catalog symbol:** `x86decomp.disassembly:control_flow_edges`  
**Visibility:** public  
**Source line:** 144

<a id="function-compare-instruction-streams"></a>

### `compare_instruction_streams`

No function or method docstring is declared in the 0.7.5 source.

```python
def compare_instruction_streams(target: bytes, candidate: bytes, *, target_base: int, candidate_base: int=0, architecture: str='x86', target_known_ranges: Iterable[tuple[int, int]]=(), candidate_known_ranges: Iterable[tuple[int, int]]=()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.disassembly:compare_instruction_streams`  
**Visibility:** public  
**Source line:** 157

<a id="function-cross-check-ghidra-instructions"></a>

### `cross_check_ghidra_instructions`

No function or method docstring is declared in the 0.7.5 source.

```python
def cross_check_ghidra_instructions(ghidra_jsonl: Path, code: bytes, *, base_address: int, architecture: str='x86', report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.disassembly:cross_check_ghidra_instructions`  
**Visibility:** public  
**Source line:** 219
