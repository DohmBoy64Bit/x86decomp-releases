---
title: x86decomp.governance.plugins
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-plugins.html
---

<a id="function-pluginregistry-init"></a>
<a id="function-pluginregistry-validate-manifest"></a>
<a id="function-pluginregistry-install"></a>
<a id="function-pluginregistry-get"></a>
<a id="function-pluginregistry-list"></a>
<a id="function-pluginregistry-doctor"></a>
<a id="function-pluginregistry-invoke"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.plugins

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 7 functions/methods

**Source:** `src/x86decomp/governance/plugins.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `49a8f980b23b66c8c08b31355f52524b05119e3aabcedfd7c5e9f5ec0cbbc083`.

## Functions and methods

Metadata: internal · line 16

### PluginRegistry.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.__init__`

Metadata: public · line 21

### PluginRegistry.validate_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.validate_manifest`

Metadata: public · line 34

### PluginRegistry.install

No function or method docstring is declared in the v0.7.4 source.

```
def install(self, manifest_path: str | Path, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.install`

Metadata: public · line 51

### PluginRegistry.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, plugin_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.get`

Metadata: public · line 61

### PluginRegistry.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.list`

Metadata: public · line 66

### PluginRegistry.doctor

No function or method docstring is declared in the v0.7.4 source.

```
def doctor(self, plugin_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.doctor`

Metadata: public · line 76

### PluginRegistry.invoke

No function or method docstring is declared in the v0.7.4 source.

```
def invoke(self, plugin_id: str, capability: str, request: dict[str, Any], *, timeout_seconds: int = 60, max_output_bytes: int = 16 * 1024 * 1024, actor: str = 'system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.plugins:PluginRegistry.invoke`
