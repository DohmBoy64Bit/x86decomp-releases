---
title: x86decomp_testkit.logging_utils
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-logging-utils.html
---

<a id="function-jsonleventlogger-init"></a>
<a id="function-jsonleventlogger-emit"></a>
<a id="function-configure-logging"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.logging_utils

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 3 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/logging_utils.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `973448e1f8708f80d4efebeec3246c51f90f35e6e1088a620d363b9767af0e8c`.

## Functions and methods

Metadata: internal · line 15

### JsonlEventLogger.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, path: Path)
```

**Catalog symbol:** `x86decomp_testkit.logging_utils:JsonlEventLogger.__init__`

Metadata: public · line 19

### JsonlEventLogger.emit

No function or method docstring is declared in the v0.7.4 source.

```
def emit(self, event: str, **fields: Any) -> None
```

**Catalog symbol:** `x86decomp_testkit.logging_utils:JsonlEventLogger.emit`

Metadata: public · line 32

### configure_logging

No function or method docstring is declared in the v0.7.4 source.

```
def configure_logging(output_directory: Path, verbose: bool = False) -> tuple[logging.Logger, JsonlEventLogger]
```

**Catalog symbol:** `x86decomp_testkit.logging_utils:configure_logging`
