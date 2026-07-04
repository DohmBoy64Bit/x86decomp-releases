---
title: x86decomp.governance.plugins
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.plugins`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/plugins.py`  
**SHA-256:** `1e339929f3ac6981f3338305eab797bc72ebcb5cf0b8717bbe3aef8a2df76ef7`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-pluginregistry-init"></a>

### `PluginRegistry.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.__init__`  
**Visibility:** internal  
**Source line:** 17

<a id="function-pluginregistry-validate-manifest"></a>

### `PluginRegistry.validate_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.validate_manifest`  
**Visibility:** public  
**Source line:** 22

<a id="function-pluginregistry-install"></a>

### `PluginRegistry.install`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.install(self, manifest_path: str | Path, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.install`  
**Visibility:** public  
**Source line:** 35

<a id="function-pluginregistry-get"></a>

### `PluginRegistry.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.get(self, plugin_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.get`  
**Visibility:** public  
**Source line:** 52

<a id="function-pluginregistry-list"></a>

### `PluginRegistry.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.list`  
**Visibility:** public  
**Source line:** 62

<a id="function-pluginregistry-doctor"></a>

### `PluginRegistry.doctor`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.doctor(self, plugin_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.doctor`  
**Visibility:** public  
**Source line:** 67

<a id="function-pluginregistry-invoke"></a>

### `PluginRegistry.invoke`

No function or method docstring is declared in the 0.7.5 source.

```python
def PluginRegistry.invoke(self, plugin_id: str, capability: str, request: dict[str, Any], *, timeout_seconds: int=60, max_output_bytes: int=16 * 1024 * 1024, actor: str='system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.invoke`  
**Visibility:** public  
**Source line:** 77
