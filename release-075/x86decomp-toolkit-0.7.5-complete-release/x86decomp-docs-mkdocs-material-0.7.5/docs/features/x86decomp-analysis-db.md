---
title: x86decomp.analysis_db
description: SQLite-backed global symbol, type, reference, and constraint database.
---

# `x86decomp.analysis_db`

SQLite-backed global symbol, type, reference, and constraint database.

**Area:** Toolkit  
**Source:** `src/x86decomp/analysis_db.py`  
**SHA-256:** `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-analysisdatabase-init"></a>

### `AnalysisDatabase.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.__init__(self, path: Path)
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.__init__`  
**Visibility:** internal  
**Source line:** 71

<a id="function-analysisdatabase-close"></a>

### `AnalysisDatabase.close`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.close(self) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.close`  
**Visibility:** public  
**Source line:** 78

<a id="function-analysisdatabase-enter"></a>

### `AnalysisDatabase.__enter__`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.__enter__(self) -> 'AnalysisDatabase'
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.__enter__`  
**Visibility:** internal  
**Source line:** 81

<a id="function-analysisdatabase-exit"></a>

### `AnalysisDatabase.__exit__`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.__exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.__exit__`  
**Visibility:** internal  
**Source line:** 84

<a id="function-analysisdatabase-upsert-entity"></a>

### `AnalysisDatabase.upsert_entity`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.upsert_entity(self, *, entity_id: str, kind: str, name: str | None, address_rva: int | None, provenance: str, confidence: float | None=None, accepted: bool=False, metadata: dict[str, Any] | None=None) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.upsert_entity`  
**Visibility:** public  
**Source line:** 91

<a id="function-analysisdatabase-add-reference"></a>

### `AnalysisDatabase.add_reference`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.add_reference(self, *, source_entity: str, target_entity: str | None, source_rva: int | None, target_rva: int | None, kind: str, provenance: str, metadata: dict[str, Any] | None=None) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.add_reference`  
**Visibility:** public  
**Source line:** 120

<a id="function-analysisdatabase-add-type-constraint"></a>

### `AnalysisDatabase.add_type_constraint`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.add_type_constraint(self, *, subject_entity: str, relation: str, object_value: str, provenance: str, evidence_id: str | None=None, confidence: float | None=None, status: str='proposed') -> int
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.add_type_constraint`  
**Visibility:** public  
**Source line:** 138

<a id="function-analysisdatabase-detect-constraint-conflicts"></a>

### `AnalysisDatabase.detect_constraint_conflicts`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.detect_constraint_conflicts(self, subject_entity: str, relation: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.detect_constraint_conflicts`  
**Visibility:** public  
**Source line:** 159

<a id="function-analysisdatabase-accept-constraint"></a>

### `AnalysisDatabase.accept_constraint`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.accept_constraint(self, constraint_id: int) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.accept_constraint`  
**Visibility:** public  
**Source line:** 174

<a id="function-analysisdatabase-ingest-function-artifact"></a>

### `AnalysisDatabase.ingest_function_artifact`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.ingest_function_artifact(self, artifact_dir: Path, *, image_base: int=0) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.ingest_function_artifact`  
**Visibility:** public  
**Source line:** 186

<a id="function-analysisdatabase-query"></a>

### `AnalysisDatabase.query`

No function or method docstring is declared in the 0.7.5 source.

```python
def AnalysisDatabase.query(self, sql: str, parameters: Iterable[Any]=()) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.query`  
**Visibility:** public  
**Source line:** 241
