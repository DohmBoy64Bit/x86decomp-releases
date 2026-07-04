---
title: x86decomp.assembly.annotation
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.assembly.annotation`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/assembly/annotation.py`  
**SHA-256:** `193333b07dc91fcfa6add9200b9f9e170c6d3705e169ac7d76056657759a59ef`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-validate-symbol"></a>

### `validate_symbol`

No function or method docstring is declared in the 0.7.5 source.

```python
def validate_symbol(symbol: str) -> str
```

**Catalog symbol:** `x86decomp.assembly.annotation:validate_symbol`  
**Visibility:** public  
**Source line:** 14

<a id="function-render-byte-assembly"></a>

### `render_byte_assembly`

Render the original compatibility form. This output intentionally preserves byte-form assembly semantics.

```python
def render_byte_assembly(symbol: str, code: bytes, architecture: str) -> str
```

**Catalog symbol:** `x86decomp.assembly.annotation:render_byte_assembly`  
**Visibility:** public  
**Source line:** 20

<a id="function-parse-byte-directives"></a>

### `parse_byte_directives`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_byte_directives(text: str) -> bytes
```

**Catalog symbol:** `x86decomp.assembly.annotation:parse_byte_directives`  
**Visibility:** public  
**Source line:** 38

<a id="function-chunk-comments"></a>

### `_chunk_comments`

No function or method docstring is declared in the 0.7.5 source.

```python
def _chunk_comments(code: bytes, *, base_address: int, architecture: str) -> dict[int, list[str]]
```

**Catalog symbol:** `x86decomp.assembly.annotation:_chunk_comments`  
**Visibility:** internal  
**Source line:** 60

<a id="function-render-annotated-assembly"></a>

### `render_annotated_assembly`

Render byte-identical directives with idempotent Capstone comments.

```python
def render_annotated_assembly(symbol: str, code: bytes, architecture: str, *, base_address: int) -> str
```

**Catalog symbol:** `x86decomp.assembly.annotation:render_annotated_assembly`  
**Visibility:** public  
**Source line:** 70

<a id="function-annotate-source"></a>

### `annotate_source`

No function or method docstring is declared in the 0.7.5 source.

```python
def annotate_source(source: Path, output: Path, *, symbol: str, architecture: str, base_address: int) -> dict[str, object]
```

**Catalog symbol:** `x86decomp.assembly.annotation:annotate_source`  
**Visibility:** public  
**Source line:** 92

<a id="function-byte-directive-lines"></a>

### `byte_directive_lines`

No function or method docstring is declared in the 0.7.5 source.

```python
def byte_directive_lines(code: bytes, *, indent: str='  ') -> Iterable[str]
```

**Catalog symbol:** `x86decomp.assembly.annotation:byte_directive_lines`  
**Visibility:** public  
**Source line:** 116
