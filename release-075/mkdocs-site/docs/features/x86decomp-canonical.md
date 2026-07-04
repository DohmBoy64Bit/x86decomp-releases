---
title: x86decomp.canonical
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.canonical`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/canonical.py`  
**SHA-256:** `a525a07fb95f10e5895a43517cdc3ff0a13df421b87195dc687629a02fd1bdd8`  
**Functions/methods:** 12

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-subparsers"></a>

### `_subparsers`

No function or method docstring is declared in the 0.7.5 source.

```python
def _subparsers(parser: argparse.ArgumentParser) -> argparse._SubParsersAction[argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_subparsers`  
**Visibility:** internal  
**Source line:** 64

<a id="function-source-parsers"></a>

### `_source_parsers`

No function or method docstring is declared in the 0.7.5 source.

```python
def _source_parsers() -> dict[str, argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_source_parsers`  
**Visibility:** internal  
**Source line:** 71

<a id="function-group-parsers"></a>

### `_group_parsers`

No function or method docstring is declared in the 0.7.5 source.

```python
def _group_parsers() -> dict[tuple[str, str], argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_group_parsers`  
**Visibility:** internal  
**Source line:** 78

<a id="function-leaf-parsers"></a>

### `_leaf_parsers`

No function or method docstring is declared in the 0.7.5 source.

```python
def _leaf_parsers() -> dict[tuple[str, str, str], argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_leaf_parsers`  
**Visibility:** internal  
**Source line:** 86

<a id="function-route-owner"></a>

### `_route_owner`

No function or method docstring is declared in the 0.7.5 source.

```python
def _route_owner(group: str, action: str, owners: tuple[str, ...]) -> str
```

**Catalog symbol:** `x86decomp.canonical:_route_owner`  
**Visibility:** internal  
**Source line:** 94

<a id="function-canonical-routes"></a>

### `canonical_routes`

No function or method docstring is declared in the 0.7.5 source.

```python
def canonical_routes() -> tuple[dict[str, str], ...]
```

**Catalog symbol:** `x86decomp.canonical:canonical_routes`  
**Visibility:** public  
**Source line:** 114

<a id="function-canonical-groups"></a>

### `canonical_groups`

No function or method docstring is declared in the 0.7.5 source.

```python
def canonical_groups() -> tuple[str, ...]
```

**Catalog symbol:** `x86decomp.canonical:canonical_groups`  
**Visibility:** public  
**Source line:** 125

<a id="function-command-catalog"></a>

### `command_catalog`

No function or method docstring is declared in the 0.7.5 source.

```python
def command_catalog(*, group: str | None=None, owner: str | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.canonical:command_catalog`  
**Visibility:** public  
**Source line:** 129

<a id="function-register-canonical-commands"></a>

### `register_canonical_commands`

No function or method docstring is declared in the 0.7.5 source.

```python
def register_canonical_commands(subparsers: Any) -> None
```

**Catalog symbol:** `x86decomp.canonical:register_canonical_commands`  
**Visibility:** public  
**Source line:** 152

<a id="function-dispatch"></a>

### `dispatch`

No function or method docstring is declared in the 0.7.5 source.

```python
def dispatch(args: argparse.Namespace) -> Any
```

**Catalog symbol:** `x86decomp.canonical:dispatch`  
**Visibility:** public  
**Source line:** 195

<a id="function-build-parser"></a>

### `build_parser`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_parser(*, prog: str='x86decomp') -> argparse.ArgumentParser
```

**Catalog symbol:** `x86decomp.canonical:build_parser`  
**Visibility:** public  
**Source line:** 204

<a id="function-main"></a>

### `main`

No function or method docstring is declared in the 0.7.5 source.

```python
def main(argv: list[str] | None=None) -> int
```

**Catalog symbol:** `x86decomp.canonical:main`  
**Visibility:** public  
**Source line:** 214
