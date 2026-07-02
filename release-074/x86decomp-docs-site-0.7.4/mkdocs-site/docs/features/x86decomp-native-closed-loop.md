---
title: x86decomp.native.closed_loop
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-closed-loop.html
---

<a id="function-closedloop-init"></a>
<a id="function-closedloop-run"></a>
<a id="function-closedloop-show"></a>
<a id="function-closedloop-list"></a>

Section: Source-derived feature and function reference

# x86decomp.native.closed_loop

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 4 functions/methods

**Source:** `src/x86decomp/native/closed_loop.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `2928f6d9ecd646ec05c4cc204048ef0c303865b68e8ae45862aa81cfed3c758b`.

## Functions and methods

Metadata: internal · line 15

### ClosedLoop.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.closed_loop:ClosedLoop.__init__`

Metadata: public · line 17

### ClosedLoop.run

No function or method docstring is declared in the v0.7.4 source.

```
def run(self, function_id: str, source_path: Path, compile_command: list[str], candidate_path: Path, original_path: Path, rva: int, slot_size: int, *, symbol: str | None = None, policy: str = 'trailing-padding', execute: bool = False, timeout_seconds: int = 120, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.closed_loop:ClosedLoop.run`

Metadata: public · line 37

### ClosedLoop.show

No function or method docstring is declared in the v0.7.4 source.

```
def show(self, loop_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.closed_loop:ClosedLoop.show`

Metadata: public · line 43

### ClosedLoop.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.closed_loop:ClosedLoop.list`
