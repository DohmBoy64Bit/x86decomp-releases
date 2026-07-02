---
title: x86decomp.assembly.materialize
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-assembly-materialize.html
---

<a id="function-assemblererror-init"></a>
<a id="function-instructioncandidate-end"></a>
<a id="function-capstone"></a>
<a id="function-safe-symbol"></a>
<a id="function-preferred-addresses"></a>
<a id="function-replace-address-token"></a>
<a id="function-instruction-candidates"></a>
<a id="function-render-source-with-line-map"></a>
<a id="function-render-source"></a>
<a id="function-discover-assembler"></a>
<a id="function-assemble-coff"></a>
<a id="function-unit-for-offset"></a>
<a id="function-verify-existing-source"></a>
<a id="function-materialize-function"></a>

Section: Source-derived feature and function reference

# x86decomp.assembly.materialize

No module docstring is declared in the v0.7.4 source.

Metadata: assembly · current · 14 functions/methods

**Source:** `src/x86decomp/assembly/materialize.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `709e23ed78dd9f4f143ea56407326b42cf86e91fc86faee1aa73483dae354f2d`.

## Functions and methods

Metadata: internal · line 23

### AssemblerError.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, message: str, *, line_numbers: Sequence[int] = ()) -> None
```

**Catalog symbol:** `x86decomp.assembly.materialize:AssemblerError.__init__`

Metadata: public · line 40

### InstructionCandidate.end

No function or method docstring is declared in the v0.7.4 source.

```
def end(self) -> int
```

**Catalog symbol:** `x86decomp.assembly.materialize:InstructionCandidate.end`

Metadata: internal · line 44

### _capstone

No function or method docstring is declared in the v0.7.4 source.

```
def _capstone() -> tuple[Any, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_capstone`

Metadata: internal · line 53

### _safe_symbol

No function or method docstring is declared in the v0.7.4 source.

```
def _safe_symbol(name: str) -> bool
```

**Catalog symbol:** `x86decomp.assembly.materialize:_safe_symbol`

Metadata: internal · line 57

### _preferred_addresses

No function or method docstring is declared in the v0.7.4 source.

```
def _preferred_addresses(symbol_map: Mapping[str, SymbolAddress], *, image_base: int) -> dict[int, str]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_preferred_addresses`

Metadata: internal · line 74

### _replace_address_token

No function or method docstring is declared in the v0.7.4 source.

```
def _replace_address_token(op_str: str, address: int, symbol: str) -> str | None
```

**Catalog symbol:** `x86decomp.assembly.materialize:_replace_address_token`

Metadata: internal · line 86

### _instruction_candidates

No function or method docstring is declared in the v0.7.4 source.

```
def _instruction_candidates(code: bytes, *, symbol: str, base_address: int, architecture: str, symbol_map: Mapping[str, SymbolAddress], image_base: int) -> tuple[list[InstructionCandidate], set[str]]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_instruction_candidates`

Metadata: internal · line 181

### _render_source_with_line_map

No function or method docstring is declared in the v0.7.4 source.

```
def _render_source_with_line_map(*, symbol: str, architecture: str, units: Sequence[InstructionCandidate], fallback_offsets: set[int], externals: set[str]) -> tuple[str, dict[int, int]]
```

**Catalog symbol:** `x86decomp.assembly.materialize:_render_source_with_line_map`

Metadata: internal · line 215

### _render_source

No function or method docstring is declared in the v0.7.4 source.

```
def _render_source(*, symbol: str, architecture: str, units: Sequence[InstructionCandidate], fallback_offsets: set[int], externals: set[str]) -> str
```

**Catalog symbol:** `x86decomp.assembly.materialize:_render_source`

Metadata: public · line 233

### discover_assembler

No function or method docstring is declared in the v0.7.4 source.

```
def discover_assembler(architecture: str) -> list[str]
```

**Catalog symbol:** `x86decomp.assembly.materialize:discover_assembler`

Metadata: public · line 252

### assemble_coff

No function or method docstring is declared in the v0.7.4 source.

```
def assemble_coff(source_path: Path, object_path: Path, *, architecture: str, assembler_command: Sequence[str] | None = None, timeout_seconds: int = 60) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:assemble_coff`

Metadata: internal · line 304

### _unit_for_offset

No function or method docstring is declared in the v0.7.4 source.

```
def _unit_for_offset(units: Sequence[InstructionCandidate], offset: int) -> InstructionCandidate | None
```

**Catalog symbol:** `x86decomp.assembly.materialize:_unit_for_offset`

Metadata: public · line 308

### verify_existing_source

Assemble an existing source file and verify its resolved bytes exactly.

```
def verify_existing_source(source_path: Path, original_bytes: bytes, *, symbol: str, rva: int, architecture: str, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]], object_path: Path, resolved_path: Path | None = None, image_base: int = 0, assembler_command: Sequence[str] | None = None, timeout_seconds: int = 60) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:verify_existing_source`

Metadata: public · line 366

### materialize_function

Materialize readable assembly and prove exact bytes, falling back per instruction.

```
def materialize_function(code: bytes, *, symbol: str, rva: int, architecture: str, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]], source_path: Path, object_path: Path, resolved_path: Path | None = None, image_base: int = 0, assembler_command: Sequence[str] | None = None, timeout_seconds: int = 60) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.materialize:materialize_function`
