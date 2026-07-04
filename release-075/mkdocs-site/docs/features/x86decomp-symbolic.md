---
title: x86decomp.symbolic
description: Bounded symbolic equivalence for small pure x86/x86-64 leaf functions.
---

# `x86decomp.symbolic`

Bounded symbolic equivalence for small pure x86/x86-64 leaf functions.

The executor intentionally rejects instructions or addressing modes it cannot
model. A successful UNSAT result is therefore meaningful only for the modeled
instruction subset, configured inputs, explored paths, and selected outputs.

**Area:** Toolkit  
**Source:** `src/x86decomp/symbolic.py`  
**SHA-256:** `93d98f6e85a01a107881131821d5eb04875d310795c4f173448918c5a96fdcd3`  
**Functions/methods:** 24

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-deps"></a>

### `_deps`

No function or method docstring is declared in the 0.7.5 source.

```python
def _deps() -> tuple[Any, Any, Any]
```

**Catalog symbol:** `x86decomp.symbolic:_deps`  
**Visibility:** internal  
**Source line:** 18

<a id="function-symstate-clone"></a>

### `SymState.clone`

No function or method docstring is declared in the 0.7.5 source.

```python
def SymState.clone(self) -> 'SymState'
```

**Catalog symbol:** `x86decomp.symbolic:SymState.clone`  
**Visibility:** public  
**Source line:** 43

<a id="function-aliases"></a>

### `_aliases`

No function or method docstring is declared in the 0.7.5 source.

```python
def _aliases(architecture: str) -> dict[str, tuple[str, int, int]]
```

**Catalog symbol:** `x86decomp.symbolic:_aliases`  
**Visibility:** internal  
**Source line:** 88

<a id="function-read-reg"></a>

### `_read_reg`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_reg(state: SymState, name: str, architecture: str, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_read_reg`  
**Visibility:** internal  
**Source line:** 92

<a id="function-write-reg"></a>

### `_write_reg`

No function or method docstring is declared in the 0.7.5 source.

```python
def _write_reg(state: SymState, name: str, value: Any, architecture: str, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_write_reg`  
**Visibility:** internal  
**Source line:** 104

<a id="function-concrete"></a>

### `_concrete`

No function or method docstring is declared in the 0.7.5 source.

```python
def _concrete(expr: Any, z3: Any) -> int | None
```

**Catalog symbol:** `x86decomp.symbolic:_concrete`  
**Visibility:** internal  
**Source line:** 125

<a id="function-memory-address"></a>

### `_memory_address`

No function or method docstring is declared in the 0.7.5 source.

```python
def _memory_address(instruction: Any, operand: Any, state: SymState, architecture: str, engine: Any, z3: Any) -> int
```

**Catalog symbol:** `x86decomp.symbolic:_memory_address`  
**Visibility:** internal  
**Source line:** 130

<a id="function-read-memory"></a>

### `_read_memory`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_memory(state: SymState, address: int, width: int, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_read_memory`  
**Visibility:** internal  
**Source line:** 149

<a id="function-write-memory"></a>

### `_write_memory`

No function or method docstring is declared in the 0.7.5 source.

```python
def _write_memory(state: SymState, address: int, width: int, value: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_write_memory`  
**Visibility:** internal  
**Source line:** 160

<a id="function-read-operand"></a>

### `_read_operand`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_operand(instruction: Any, operand: Any, state: SymState, architecture: str, engine: Any, x86_const: Any, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_read_operand`  
**Visibility:** internal  
**Source line:** 171

<a id="function-write-operand"></a>

### `_write_operand`

No function or method docstring is declared in the 0.7.5 source.

```python
def _write_operand(instruction: Any, operand: Any, value: Any, state: SymState, architecture: str, engine: Any, x86_const: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_write_operand`  
**Visibility:** internal  
**Source line:** 183

<a id="function-coerce-pair"></a>

### `_coerce_pair`

No function or method docstring is declared in the 0.7.5 source.

```python
def _coerce_pair(left: Any, right: Any, z3: Any) -> tuple[Any, Any]
```

**Catalog symbol:** `x86decomp.symbolic:_coerce_pair`  
**Visibility:** internal  
**Source line:** 195

<a id="function-set-logic-flags"></a>

### `_set_logic_flags`

No function or method docstring is declared in the 0.7.5 source.

```python
def _set_logic_flags(state: SymState, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_logic_flags`  
**Visibility:** internal  
**Source line:** 204

<a id="function-set-add-flags"></a>

### `_set_add_flags`

No function or method docstring is declared in the 0.7.5 source.

```python
def _set_add_flags(state: SymState, left: Any, right: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_add_flags`  
**Visibility:** internal  
**Source line:** 211

<a id="function-set-sub-flags"></a>

### `_set_sub_flags`

No function or method docstring is declared in the 0.7.5 source.

```python
def _set_sub_flags(state: SymState, left: Any, right: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_sub_flags`  
**Visibility:** internal  
**Source line:** 223

<a id="function-condition"></a>

### `_condition`

No function or method docstring is declared in the 0.7.5 source.

```python
def _condition(mnemonic: str, flags: dict[str, Any], z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_condition`  
**Visibility:** internal  
**Source line:** 235

<a id="function-condition-for-family"></a>

### `_condition_for_family`

Resolve Jcc, SETcc, and CMOVcc names through the same flag model.

```python
def _condition_for_family(mnemonic: str, flags: dict[str, Any], z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_condition_for_family`  
**Visibility:** internal  
**Source line:** 254

<a id="function-set-adc-flags"></a>

### `_set_adc_flags`

No function or method docstring is declared in the 0.7.5 source.

```python
def _set_adc_flags(state: SymState, left: Any, right: Any, carry: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_adc_flags`  
**Visibility:** internal  
**Source line:** 278

<a id="function-set-sbb-flags"></a>

### `_set_sbb_flags`

No function or method docstring is declared in the 0.7.5 source.

```python
def _set_sbb_flags(state: SymState, left: Any, right: Any, borrow: Any, result: Any, z3: Any) -> None
```

**Catalog symbol:** `x86decomp.symbolic:_set_sbb_flags`  
**Visibility:** internal  
**Source line:** 294

<a id="function-is-sat"></a>

### `_is_sat`

No function or method docstring is declared in the 0.7.5 source.

```python
def _is_sat(constraints: list[Any], z3: Any) -> bool
```

**Catalog symbol:** `x86decomp.symbolic:_is_sat`  
**Visibility:** internal  
**Source line:** 309

<a id="function-symbolic-execute"></a>

### `symbolic_execute`

No function or method docstring is declared in the 0.7.5 source.

```python
def symbolic_execute(code: bytes, *, architecture: str='x86', base_address: int=1048576, input_registers: tuple[str, ...]=(), stack_argument_words: int=0, output_registers: tuple[str, ...] | None=None, max_steps: int=1000, max_paths: int=64) -> tuple[list[Outcome], dict[str, Any]]
```

**Catalog symbol:** `x86decomp.symbolic:symbolic_execute`  
**Visibility:** public  
**Source line:** 315

<a id="function-constraint-formula"></a>

### `_constraint_formula`

No function or method docstring is declared in the 0.7.5 source.

```python
def _constraint_formula(outcome: Outcome, z3: Any) -> Any
```

**Catalog symbol:** `x86decomp.symbolic:_constraint_formula`  
**Visibility:** internal  
**Source line:** 601

<a id="function-bounded-symbolic-compare"></a>

### `bounded_symbolic_compare`

No function or method docstring is declared in the 0.7.5 source.

```python
def bounded_symbolic_compare(target: bytes, candidate: bytes, *, architecture: str='x86', input_registers: tuple[str, ...]=(), stack_argument_words: int=0, output_registers: tuple[str, ...] | None=None, max_steps: int=1000, max_paths: int=64, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.symbolic:bounded_symbolic_compare`  
**Visibility:** public  
**Source line:** 605

<a id="function-bounded-symbolic-compare-files"></a>

### `bounded_symbolic_compare_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def bounded_symbolic_compare_files(target_path: Path, candidate_path: Path, **kwargs: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.symbolic:bounded_symbolic_compare_files`  
**Visibility:** public  
**Source line:** 684
