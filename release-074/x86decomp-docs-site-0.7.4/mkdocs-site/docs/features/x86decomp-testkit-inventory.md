---
title: x86decomp_testkit.inventory
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-inventory.html
---

<a id="function-publicsymbol-symbol-id"></a>
<a id="function-publicsymbol-to-dict"></a>
<a id="function-direct-body-lines"></a>
<a id="function-python-files"></a>
<a id="function-module-name"></a>
<a id="function-discover-symbols"></a>
<a id="function-discover-public-symbols"></a>
<a id="function-discover-all-function-symbols"></a>
<a id="function-discover-modules"></a>
<a id="function-discover-schemas"></a>
<a id="function-discover-ghidra-scripts"></a>
<a id="function-discover-cli-commands"></a>
<a id="function-build-inventory"></a>
<a id="function-load-feature-catalog"></a>
<a id="function-audit-catalog"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.inventory

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 15 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/inventory.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `d7c60ef575fc20122b84c635d9cdd8875dd629cabaa9a6f7810aaa1b306242a4`.

## Functions and methods

Metadata: public · line 24

### PublicSymbol.symbol_id

No function or method docstring is declared in the v0.7.4 source.

```
def symbol_id(self) -> str
```

**Catalog symbol:** `x86decomp_testkit.inventory:PublicSymbol.symbol_id`

Metadata: public · line 27

### PublicSymbol.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:PublicSymbol.to_dict`

Metadata: internal · line 38

### _direct_body_lines

No function or method docstring is declared in the v0.7.4 source.

```
def _direct_body_lines(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[int, ...]
```

**Catalog symbol:** `x86decomp_testkit.inventory:_direct_body_lines`

Metadata: internal · line 51

### _python_files

No function or method docstring is declared in the v0.7.4 source.

```
def _python_files(toolkit_root: Path) -> list[Path]
```

**Catalog symbol:** `x86decomp_testkit.inventory:_python_files`

Metadata: internal · line 58

### _module_name

No function or method docstring is declared in the v0.7.4 source.

```
def _module_name(toolkit_root: Path, path: Path) -> str
```

**Catalog symbol:** `x86decomp_testkit.inventory:_module_name`

Metadata: internal · line 67

### _discover_symbols

No function or method docstring is declared in the v0.7.4 source.

```
def _discover_symbols(toolkit_root: Path, *, public_only: bool) -> list[PublicSymbol]
```

**Catalog symbol:** `x86decomp_testkit.inventory:_discover_symbols`

Metadata: public · line 99

### discover_public_symbols

No function or method docstring is declared in the v0.7.4 source.

```
def discover_public_symbols(toolkit_root: Path) -> list[PublicSymbol]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_public_symbols`

Metadata: public · line 103

### discover_all_function_symbols

No function or method docstring is declared in the v0.7.4 source.

```
def discover_all_function_symbols(toolkit_root: Path) -> list[PublicSymbol]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_all_function_symbols`

Metadata: public · line 107

### discover_modules

No function or method docstring is declared in the v0.7.4 source.

```
def discover_modules(toolkit_root: Path) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_modules`

Metadata: public · line 111

### discover_schemas

No function or method docstring is declared in the v0.7.4 source.

```
def discover_schemas(toolkit_root: Path) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_schemas`

Metadata: public · line 116

### discover_ghidra_scripts

No function or method docstring is declared in the v0.7.4 source.

```
def discover_ghidra_scripts(toolkit_root: Path) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_ghidra_scripts`

Metadata: public · line 121

### discover_cli_commands

No function or method docstring is declared in the v0.7.4 source.

```
def discover_cli_commands(toolkit_root: Path, python_executable: str = sys.executable) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.inventory:discover_cli_commands`

Metadata: public · line 141

### build_inventory

No function or method docstring is declared in the v0.7.4 source.

```
def build_inventory(toolkit_root: Path, python_executable: str = sys.executable) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:build_inventory`

Metadata: public · line 155

### load_feature_catalog

No function or method docstring is declared in the v0.7.4 source.

```
def load_feature_catalog(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:load_feature_catalog`

Metadata: public · line 162

### audit_catalog

No function or method docstring is declared in the v0.7.4 source.

```
def audit_catalog(inventory: dict[str, Any], catalog: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.inventory:audit_catalog`
