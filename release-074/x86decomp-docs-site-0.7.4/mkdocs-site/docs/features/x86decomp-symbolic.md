---
title: x86decomp.symbolic
description: Bounded symbolic equivalence for small pure x86/x86-64 leaf functions.
original_path: features/x86decomp-symbolic.html
---

<a id="function-deps"></a>
<a id="function-symstate-clone"></a>
<a id="function-aliases"></a>
<a id="function-read-reg"></a>
<a id="function-write-reg"></a>
<a id="function-concrete"></a>
<a id="function-memory-address"></a>
<a id="function-read-memory"></a>
<a id="function-write-memory"></a>
<a id="function-read-operand"></a>
<a id="function-write-operand"></a>
<a id="function-coerce-pair"></a>
<a id="function-set-logic-flags"></a>
<a id="function-set-add-flags"></a>
<a id="function-set-sub-flags"></a>
<a id="function-condition"></a>
<a id="function-condition-for-family"></a>
<a id="function-set-adc-flags"></a>
<a id="function-set-sbb-flags"></a>
<a id="function-is-sat"></a>
<a id="function-symbolic-execute"></a>
<a id="function-constraint-formula"></a>
<a id="function-bounded-symbolic-compare"></a>
<a id="function-bounded-symbolic-compare-files"></a>

Section: Source-derived feature and function reference

# x86decomp.symbolic

Bounded symbolic equivalence for small pure x86/x86-64 leaf functions.

Metadata: core · current · 24 functions/methods

**Source:** `src/x86decomp/symbolic.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3`.

## Functions and methods

Metadata: internal · line 18

### _deps

No function or method docstring is declared in the v0.7.4 source.

```
def _deps() -> tuple[Any, Any, Any]
```

**Catalog symbol:** `x86decomp.symbolic:_deps`

Metadata: public · line 43

### SymState.clone

No function or method docstring is declared in the v0.7.4 source.

```
def clone(self) -> 'SymState'
```

**Catalog symbol:** `x86decomp.symbolic:SymState.clone`

Metadata: internal · line 88

### _aliases

No function or method docstring is declared in the v0.7.4 source.

```
def _aliases(architecture: str) -> dict[str, tuple[str, int, int]]
```

**Catalog symbol:** `x86decomp.symbolic:_aliases`

Metadata: internal · line 92

### _read_reg

No function or method docstring is declared in the v0.7.4 source.

```
def _read_reg(state: SymState, name: str, architecture: str, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_read_reg`

Metadata: internal · line 104

### _write_reg

No function or method docstring is declared in the v0.7.4 source.

```
def _write_reg(state: SymState, name: str, value: Any, architecture: str, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_write_reg`

Metadata: internal · line 125

### _concrete

No function or method docstring is declared in the v0.7.4 source.

```
def _concrete(expr: Any, z3: Any) -> int | None
```

**Catalog symbol:** `x86decomp.symbolic:_concrete`

Metadata: internal · line 130

### _memory_address

No function or method docstring is declared in the v0.7.4 source.

```
def _memory_address(instruction: Any, operand: Any, state: SymState, architecture: str, engine: Any, z3: Any) -> int
```

**Catalog symbol:** `x86decomp.symbolic:_memory_address`

Metadata: internal · line 149

### _read_memory

No function or method docstring is declared in the v0.7.4 source.

```
def _read_memory(state: SymState, address: int, width: int, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_read_memory`

Metadata: internal · line 160

### _write_memory

No function or method docstring is declared in the v0.7.4 source.

```
def _write_memory(state: SymState, address: int, width: int, value: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_write_memory`

Metadata: internal · line 171

### _read_operand

No function or method docstring is declared in the v0.7.4 source.

```
def _read_operand(instruction: Any, operand: Any, state: SymState, architecture: str, engine: Any, x86_const: Any, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_read_operand`

Metadata: internal · line 183

### _write_operand

No function or method docstring is declared in the v0.7.4 source.

```
def _write_operand(instruction: Any, operand: Any, value: Any, state: SymState, architecture: str, engine: Any, x86_const: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_write_operand`

Metadata: internal · line 195

### _coerce_pair

No function or method docstring is declared in the v0.7.4 source.

```
def _coerce_pair(left: Any, right: Any, z3: Any) -> tuple[Any, Any]
```

**Catalog symbol:** `x86decomp.symbolic:_coerce_pair`

Metadata: internal · line 204

### _set_logic_flags

No function or method docstring is declared in the v0.7.4 source.

```
def _set_logic_flags(state: SymState, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_logic_flags`

Metadata: internal · line 211

### _set_add_flags

No function or method docstring is declared in the v0.7.4 source.

```
def _set_add_flags(state: SymState, left: Any, right: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_add_flags`

Metadata: internal · line 223

### _set_sub_flags

No function or method docstring is declared in the v0.7.4 source.

```
def _set_sub_flags(state: SymState, left: Any, right: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_sub_flags`

Metadata: internal · line 235

### _condition

No function or method docstring is declared in the v0.7.4 source.

```
def _condition(mnemonic: str, flags: dict[str, Any], z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_condition`

Metadata: internal · line 254

### _condition_for_family

Resolve Jcc, SETcc, and CMOVcc names through the same flag model.

```
def _condition_for_family(mnemonic: str, flags: dict[str, Any], z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_condition_for_family`

Metadata: internal · line 278

### _set_adc_flags

No function or method docstring is declared in the v0.7.4 source.

```
def _set_adc_flags(state: SymState, left: Any, right: Any, carry: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_adc_flags`

Metadata: internal · line 294

### _set_sbb_flags

No function or method docstring is declared in the v0.7.4 source.

```
def _set_sbb_flags(state: SymState, left: Any, right: Any, borrow: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_sbb_flags`

Metadata: internal · line 309

### _is_sat

No function or method docstring is declared in the v0.7.4 source.

```
def _is_sat(constraints: list[Any], z3: Any) -> bool
```

**Catalog symbol:** `x86decomp.symbolic:_is_sat`

Metadata: public · line 315

### symbolic_execute

No function or method docstring is declared in the v0.7.4 source.

```
def symbolic_execute(code: bytes, *, architecture: str = 'x86', base_address: int = 1048576, input_registers: tuple[str, ...] = (), stack_argument_words: int = 0, output_registers: tuple[str, ...] | None = None, max_steps: int = 1000, max_paths: int = 64) -> tuple[list[Outcome], dict[str, Any]]
```

**Catalog symbol:** `x86decomp.symbolic:symbolic_execute`

Metadata: internal · line 601

### _constraint_formula

No function or method docstring is declared in the v0.7.4 source.

```
def _constraint_formula(outcome: Outcome, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_constraint_formula`

Metadata: public · line 605

### bounded_symbolic_compare

No function or method docstring is declared in the v0.7.4 source.

```
def bounded_symbolic_compare(target: bytes, candidate: bytes, *, architecture: str = 'x86', input_registers: tuple[str, ...] = (), stack_argument_words: int = 0, output_registers: tuple[str, ...] | None = None, max_steps: int = 1000, max_paths: int = 64, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.symbolic:bounded_symbolic_compare`

Metadata: public · line 684

### bounded_symbolic_compare_files

No function or method docstring is declared in the v0.7.4 source.

```
def bounded_symbolic_compare_files(target_path: Path, candidate_path: Path, **kwargs: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.symbolic:bounded_symbolic_compare_files`
