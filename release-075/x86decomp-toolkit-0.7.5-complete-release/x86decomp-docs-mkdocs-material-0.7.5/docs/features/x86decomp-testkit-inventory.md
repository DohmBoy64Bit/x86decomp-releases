---
title: x86decomp_testkit.inventory
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp_testkit.inventory`

No module docstring is declared in the 0.7.5 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/inventory.py`  
**SHA-256:** `d7c60ef575fc20122b84c635d9cdd8875dd629cabaa9a6f7810aaa1b306242a4`  
**Functions/methods:** 15

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-publicsymbol-symbol-id"></a>

### `PublicSymbol.symbol_id`

No function or method docstring is declared in the 0.7.5 source.

```python
def PublicSymbol.symbol_id(self) -> str
```

**Catalog symbol:** `x86decomp_testkit.inventory:PublicSymbol.symbol_id`  
**Visibility:** public  
**Source line:** 24

<a id="function-publicsymbol-to-dict"></a>

### `PublicSymbol.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def PublicSymbol.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:PublicSymbol.to_dict`  
**Visibility:** public  
**Source line:** 27

<a id="function-direct-body-lines"></a>

### `_direct_body_lines`

No function or method docstring is declared in the 0.7.5 source.

```python
def _direct_body_lines(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[int, ...]
```

**Catalog symbol:** `x86decomp_testkit.inventory:_direct_body_lines`  
**Visibility:** internal  
**Source line:** 38

<a id="function-python-files"></a>

### `_python_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def _python_files(toolkit_root: Path) -> list[Path]
```

**Catalog symbol:** `x86decomp_testkit.inventory:_python_files`  
**Visibility:** internal  
**Source line:** 51

<a id="function-module-name"></a>

### `_module_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _module_name(toolkit_root: Path, path: Path) -> str
```

**Catalog symbol:** `x86decomp_testkit.inventory:_module_name`  
**Visibility:** internal  
**Source line:** 58

<a id="function-discover-symbols"></a>

### `_discover_symbols`

No function or method docstring is declared in the 0.7.5 source.

```python
def _discover_symbols(toolkit_root: Path, *, public_only: bool) -> list[PublicSymbol]
```

**Catalog symbol:** `x86decomp_testkit.inventory:_discover_symbols`  
**Visibility:** internal  
**Source line:** 67

<a id="function-discover-public-symbols"></a>

### `discover_public_symbols`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_public_symbols(toolkit_root: Path) -> list[PublicSymbol]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_public_symbols`  
**Visibility:** public  
**Source line:** 99

<a id="function-discover-all-function-symbols"></a>

### `discover_all_function_symbols`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_all_function_symbols(toolkit_root: Path) -> list[PublicSymbol]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_all_function_symbols`  
**Visibility:** public  
**Source line:** 103

<a id="function-discover-modules"></a>

### `discover_modules`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_modules(toolkit_root: Path) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_modules`  
**Visibility:** public  
**Source line:** 107

<a id="function-discover-schemas"></a>

### `discover_schemas`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_schemas(toolkit_root: Path) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_schemas`  
**Visibility:** public  
**Source line:** 111

<a id="function-discover-ghidra-scripts"></a>

### `discover_ghidra_scripts`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_ghidra_scripts(toolkit_root: Path) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_ghidra_scripts`  
**Visibility:** public  
**Source line:** 116

<a id="function-discover-cli-commands"></a>

### `discover_cli_commands`

No function or method docstring is declared in the 0.7.5 source.

```python
def discover_cli_commands(toolkit_root: Path, python_executable: str=sys.executable) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_cli_commands`  
**Visibility:** public  
**Source line:** 121

<a id="function-build-inventory"></a>

### `build_inventory`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_inventory(toolkit_root: Path, python_executable: str=sys.executable) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:build_inventory`  
**Visibility:** public  
**Source line:** 141

<a id="function-load-feature-catalog"></a>

### `load_feature_catalog`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_feature_catalog(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:load_feature_catalog`  
**Visibility:** public  
**Source line:** 155

<a id="function-audit-catalog"></a>

### `audit_catalog`

No function or method docstring is declared in the 0.7.5 source.

```python
def audit_catalog(inventory: dict[str, Any], catalog: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:audit_catalog`  
**Visibility:** public  
**Source line:** 162
