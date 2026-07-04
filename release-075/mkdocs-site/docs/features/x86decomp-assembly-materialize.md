---
title: x86decomp.assembly.materialize
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.assembly.materialize`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/assembly/materialize.py`  
**SHA-256:** `bd19d35efc03ca7bc501fe4b87a028a9c36131d3eeee4a7f98c6aad5bdab2324`  
**Functions/methods:** 14

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-assemblererror-init"></a>

### `AssemblerError.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def AssemblerError.__init__(self, message: str, *, line_numbers: Sequence[int]=()) -> None
```

**Catalog symbol:** `x86decomp.assembly.materialize:AssemblerError.__init__`  
**Visibility:** internal  
**Source line:** 24

<a id="function-instructioncandidate-end"></a>

### `InstructionCandidate.end`

No function or method docstring is declared in the 0.7.5 source.

```python
def InstructionCandidate.end(self) -> int
```

**Catalog symbol:** `x86decomp.assembly.materialize:InstructionCandidate.end`  
**Visibility:** public  
**Source line:** 41

<a id="function-capstone"></a>

### `_capstone`

No function or method docstring is declared in the 0.7.5 source.

```python
def _capstone() -> tuple[Any, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_capstone`  
**Visibility:** internal  
**Source line:** 45

<a id="function-safe-symbol"></a>

### `_safe_symbol`

No function or method docstring is declared in the 0.7.5 source.

```python
def _safe_symbol(name: str) -> bool
```

**Catalog symbol:** `x86decomp.assembly.materialize:_safe_symbol`  
**Visibility:** internal  
**Source line:** 54

<a id="function-preferred-addresses"></a>

### `_preferred_addresses`

No function or method docstring is declared in the 0.7.5 source.

```python
def _preferred_addresses(symbol_map: Mapping[str, SymbolAddress], *, image_base: int) -> dict[int, str]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_preferred_addresses`  
**Visibility:** internal  
**Source line:** 58

<a id="function-replace-address-token"></a>

### `_replace_address_token`

No function or method docstring is declared in the 0.7.5 source.

```python
def _replace_address_token(op_str: str, address: int, symbol: str) -> str | None
```

**Catalog symbol:** `x86decomp.assembly.materialize:_replace_address_token`  
**Visibility:** internal  
**Source line:** 75

<a id="function-instruction-candidates"></a>

### `_instruction_candidates`

No function or method docstring is declared in the 0.7.5 source.

```python
def _instruction_candidates(code: bytes, *, symbol: str, base_address: int, architecture: str, symbol_map: Mapping[str, SymbolAddress], image_base: int) -> tuple[list[InstructionCandidate], set[str]]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_instruction_candidates`  
**Visibility:** internal  
**Source line:** 87

<a id="function-render-source-with-line-map"></a>

### `_render_source_with_line_map`

No function or method docstring is declared in the 0.7.5 source.

```python
def _render_source_with_line_map(*, symbol: str, architecture: str, units: Sequence[InstructionCandidate], fallback_offsets: set[int], externals: set[str]) -> tuple[str, dict[int, int]]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_render_source_with_line_map`  
**Visibility:** internal  
**Source line:** 182

<a id="function-render-source"></a>

### `_render_source`

No function or method docstring is declared in the 0.7.5 source.

```python
def _render_source(*, symbol: str, architecture: str, units: Sequence[InstructionCandidate], fallback_offsets: set[int], externals: set[str]) -> str
```

**Catalog symbol:** `x86decomp.assembly.materialize:_render_source`  
**Visibility:** internal  
**Source line:** 216

<a id="function-discover-assembler"></a>

### `discover_assembler`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_assembler(architecture: str) -> list[str]
```

**Catalog symbol:** `x86decomp.assembly.materialize:discover_assembler`  
**Visibility:** public  
**Source line:** 234

<a id="function-assemble-coff"></a>

### `assemble_coff`

No function or method docstring is declared in the 0.7.5 source.

```python
def assemble_coff(source_path: Path, object_path: Path, *, architecture: str, assembler_command: Sequence[str] | None=None, timeout_seconds: int=60) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:assemble_coff`  
**Visibility:** public  
**Source line:** 257

<a id="function-unit-for-offset"></a>

### `_unit_for_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def _unit_for_offset(units: Sequence[InstructionCandidate], offset: int) -> InstructionCandidate | None
```

**Catalog symbol:** `x86decomp.assembly.materialize:_unit_for_offset`  
**Visibility:** internal  
**Source line:** 309

<a id="function-verify-existing-source"></a>

### `verify_existing_source`

Assemble an existing source file and verify its resolved bytes exactly.

```python
def verify_existing_source(source_path: Path, original_bytes: bytes, *, symbol: str, rva: int, architecture: str, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]], object_path: Path, resolved_path: Path | None=None, image_base: int=0, assembler_command: Sequence[str] | None=None, timeout_seconds: int=60) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:verify_existing_source`  
**Visibility:** public  
**Source line:** 313

<a id="function-materialize-function"></a>

### `materialize_function`

Materialize readable assembly and prove exact bytes, falling back per instruction.

```python
def materialize_function(code: bytes, *, symbol: str, rva: int, architecture: str, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]], source_path: Path, object_path: Path, resolved_path: Path | None=None, image_base: int=0, assembler_command: Sequence[str] | None=None, timeout_seconds: int=60) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:materialize_function`  
**Visibility:** public  
**Source line:** 371
