---
title: x86decomp_testkit.config
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-config.html
---

<a id="function-testconfig-to-dict"></a>
<a id="function-testconfig-from-dict"></a>
<a id="function-load-config"></a>
<a id="function-save-config"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.config

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 4 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/config.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `766a7f68f96c2658782d99f806ea342fb09bfa734fd22de5fb890a60b0004427`.

## Functions and methods

Metadata: public · line 31

### TestConfig.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.config:TestConfig.to_dict`

Metadata: public · line 52

### TestConfig.from_dict

No function or method docstring is declared in the v0.7.4 source.

```
def from_dict(cls, data: dict[str, Any], base: Path | None = None) -> 'TestConfig'
```

**Catalog symbol:** `x86decomp_testkit.config:TestConfig.from_dict`

Metadata: public · line 84

### load_config

No function or method docstring is declared in the v0.7.4 source.

```
def load_config(path: Path) -> TestConfig
```

**Catalog symbol:** `x86decomp_testkit.config:load_config`

Metadata: public · line 91

### save_config

No function or method docstring is declared in the v0.7.4 source.

```
def save_config(config: TestConfig, path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.config:save_config`
