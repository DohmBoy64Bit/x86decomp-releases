---
title: x86decomp.assembly.annotation
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-assembly-annotation.html
---

<a id="function-validate-symbol"></a>
<a id="function-render-byte-assembly"></a>
<a id="function-parse-byte-directives"></a>
<a id="function-chunk-comments"></a>
<a id="function-render-annotated-assembly"></a>
<a id="function-annotate-source"></a>
<a id="function-byte-directive-lines"></a>

Section: Source-derived feature and function reference

# x86decomp.assembly.annotation

No module docstring is declared in the v0.7.4 source.

Metadata: assembly · current · 7 functions/methods

**Source:** `src/x86decomp/assembly/annotation.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `193333b07dc91fcfa6add9200b9f9e170c6d3705e169ac7d76056657759a59ef`.

## Functions and methods

Metadata: public · line 14

### validate_symbol

No function or method docstring is declared in the v0.7.4 source.

```
def validate_symbol(symbol: str) -> str
```

**Catalog symbol:** `x86decomp.assembly.annotation:validate_symbol`

Metadata: public · line 20

### render_byte_assembly

Render the original compatibility form. This output intentionally preserves byte-form assembly semantics.

```
def render_byte_assembly(symbol: str, code: bytes, architecture: str) -> str
```

**Catalog symbol:** `x86decomp.assembly.annotation:render_byte_assembly`

Metadata: public · line 38

### parse_byte_directives

No function or method docstring is declared in the v0.7.4 source.

```
def parse_byte_directives(text: str) -> bytes
```

**Catalog symbol:** `x86decomp.assembly.annotation:parse_byte_directives`

Metadata: internal · line 60

### _chunk_comments

No function or method docstring is declared in the v0.7.4 source.

```
def _chunk_comments(code: bytes, *, base_address: int, architecture: str) -> dict[int, list[str]]
```

**Catalog symbol:** `x86decomp.assembly.annotation:_chunk_comments`

Metadata: public · line 70

### render_annotated_assembly

Render byte-identical directives with idempotent Capstone comments.

```
def render_annotated_assembly(symbol: str, code: bytes, architecture: str, *, base_address: int) -> str
```

**Catalog symbol:** `x86decomp.assembly.annotation:render_annotated_assembly`

Metadata: public · line 92

### annotate_source

No function or method docstring is declared in the v0.7.4 source.

```
def annotate_source(source: Path, output: Path, *, symbol: str, architecture: str, base_address: int) -> dict[str, object]
```

**Catalog symbol:** `x86decomp.assembly.annotation:annotate_source`

Metadata: public · line 116

### byte_directive_lines

No function or method docstring is declared in the v0.7.4 source.

```
def byte_directive_lines(code: bytes, *, indent: str = '  ') -> Iterable[str]
```

**Catalog symbol:** `x86decomp.assembly.annotation:byte_directive_lines`
