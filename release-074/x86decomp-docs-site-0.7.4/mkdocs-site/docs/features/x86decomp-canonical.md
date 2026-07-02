---
title: x86decomp.canonical
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-canonical.html
---

<a id="function-subparsers"></a>
<a id="function-source-parsers"></a>
<a id="function-group-parsers"></a>
<a id="function-leaf-parsers"></a>
<a id="function-route-owner"></a>
<a id="function-canonical-routes"></a>
<a id="function-canonical-groups"></a>
<a id="function-command-catalog"></a>
<a id="function-register-canonical-commands"></a>
<a id="function-dispatch"></a>
<a id="function-build-parser"></a>
<a id="function-main"></a>

Section: Source-derived feature and function reference

# x86decomp.canonical

No module docstring is declared in the v0.7.4 source.

Metadata: core · current · 12 functions/methods

**Source:** `src/x86decomp/canonical.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4424ac7f4214c0af367791e1cba7268b5bc1d9ff0d7fa4f56d4c94fff6eae782`.

## Functions and methods

Metadata: internal · line 64

### _subparsers

No function or method docstring is declared in the v0.7.4 source.

```
def _subparsers(parser: argparse.ArgumentParser) -> argparse._SubParsersAction[argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_subparsers`

Metadata: internal · line 71

### _source_parsers

No function or method docstring is declared in the v0.7.4 source.

```
def _source_parsers() -> dict[str, argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_source_parsers`

Metadata: internal · line 78

### _group_parsers

No function or method docstring is declared in the v0.7.4 source.

```
def _group_parsers() -> dict[tuple[str, str], argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_group_parsers`

Metadata: internal · line 86

### _leaf_parsers

No function or method docstring is declared in the v0.7.4 source.

```
def _leaf_parsers() -> dict[tuple[str, str, str], argparse.ArgumentParser]
```

**Catalog symbol:** `x86decomp.canonical:_leaf_parsers`

Metadata: internal · line 94

### _route_owner

No function or method docstring is declared in the v0.7.4 source.

```
def _route_owner(group: str, action: str, owners: tuple[str, ...]) -> str
```

**Catalog symbol:** `x86decomp.canonical:_route_owner`

Metadata: public · line 114

### canonical_routes

No function or method docstring is declared in the v0.7.4 source.

```
def canonical_routes() -> tuple[dict[str, str], ...]
```

**Catalog symbol:** `x86decomp.canonical:canonical_routes`

Metadata: public · line 125

### canonical_groups

No function or method docstring is declared in the v0.7.4 source.

```
def canonical_groups() -> tuple[str, ...]
```

**Catalog symbol:** `x86decomp.canonical:canonical_groups`

Metadata: public · line 129

### command_catalog

No function or method docstring is declared in the v0.7.4 source.

```
def command_catalog(*, group: str | None = None, owner: str | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.canonical:command_catalog`

Metadata: public · line 152

### register_canonical_commands

No function or method docstring is declared in the v0.7.4 source.

```
def register_canonical_commands(subparsers: Any) -> None
```

**Catalog symbol:** `x86decomp.canonical:register_canonical_commands`

Metadata: public · line 195

### dispatch

No function or method docstring is declared in the v0.7.4 source.

```
def dispatch(args: argparse.Namespace) -> Any
```

**Catalog symbol:** `x86decomp.canonical:dispatch`

Metadata: public · line 204

### build_parser

No function or method docstring is declared in the v0.7.4 source.

```
def build_parser(*, prog: str = 'x86decomp') -> argparse.ArgumentParser
```

**Catalog symbol:** `x86decomp.canonical:build_parser`

Metadata: public · line 214

### main

No function or method docstring is declared in the v0.7.4 source.

```
def main(argv: list[str] | None = None) -> int
```

**Catalog symbol:** `x86decomp.canonical:main`
