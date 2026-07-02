---
title: x86decomp.analysis_db
description: SQLite-backed global symbol, type, reference, and constraint database.
original_path: features/x86decomp-analysis-db.html
---

<a id="function-analysisdatabase-init"></a>
<a id="function-analysisdatabase-close"></a>
<a id="function-analysisdatabase-enter"></a>
<a id="function-analysisdatabase-exit"></a>
<a id="function-analysisdatabase-upsert-entity"></a>
<a id="function-analysisdatabase-add-reference"></a>
<a id="function-analysisdatabase-add-type-constraint"></a>
<a id="function-analysisdatabase-detect-constraint-conflicts"></a>
<a id="function-analysisdatabase-accept-constraint"></a>
<a id="function-analysisdatabase-ingest-function-artifact"></a>
<a id="function-analysisdatabase-query"></a>

Section: Source-derived feature and function reference

# x86decomp.analysis_db

SQLite-backed global symbol, type, reference, and constraint database.

Metadata: core · current · 11 functions/methods

**Source:** `src/x86decomp/analysis_db.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `409e503d6c264dba48a00e1d1afc475ce735cf25f1ec4aab7ac41b07ed5b9bad`.

## Functions and methods

Metadata: internal · line 71

### AnalysisDatabase.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, path: Path)
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.__init__`

Metadata: public · line 78

### AnalysisDatabase.close

No function or method docstring is declared in the v0.7.4 source.

```
def close(self) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.close`

Metadata: internal · line 81

### AnalysisDatabase.__enter__

No function or method docstring is declared in the v0.7.4 source.

```
def __enter__(self) -> 'AnalysisDatabase'
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.__enter__`

Metadata: internal · line 84

### AnalysisDatabase.__exit__

No function or method docstring is declared in the v0.7.4 source.

```
def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.__exit__`

Metadata: public · line 91

### AnalysisDatabase.upsert_entity

No function or method docstring is declared in the v0.7.4 source.

```
def upsert_entity(self, *, entity_id: str, kind: str, name: str | None, address_rva: int | None, provenance: str, confidence: float | None = None, accepted: bool = False, metadata: dict[str, Any] | None = None) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.upsert_entity`

Metadata: public · line 120

### AnalysisDatabase.add_reference

No function or method docstring is declared in the v0.7.4 source.

```
def add_reference(self, *, source_entity: str, target_entity: str | None, source_rva: int | None, target_rva: int | None, kind: str, provenance: str, metadata: dict[str, Any] | None = None) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.add_reference`

Metadata: public · line 138

### AnalysisDatabase.add_type_constraint

No function or method docstring is declared in the v0.7.4 source.

```
def add_type_constraint(self, *, subject_entity: str, relation: str, object_value: str, provenance: str, evidence_id: str | None = None, confidence: float | None = None, status: str = 'proposed') -> int
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.add_type_constraint`

Metadata: public · line 159

### AnalysisDatabase.detect_constraint_conflicts

No function or method docstring is declared in the v0.7.4 source.

```
def detect_constraint_conflicts(self, subject_entity: str, relation: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.detect_constraint_conflicts`

Metadata: public · line 174

### AnalysisDatabase.accept_constraint

No function or method docstring is declared in the v0.7.4 source.

```
def accept_constraint(self, constraint_id: int) -> None
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.accept_constraint`

Metadata: public · line 186

### AnalysisDatabase.ingest_function_artifact

No function or method docstring is declared in the v0.7.4 source.

```
def ingest_function_artifact(self, artifact_dir: Path, *, image_base: int = 0) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.ingest_function_artifact`

Metadata: public · line 241

### AnalysisDatabase.query

No function or method docstring is declared in the v0.7.4 source.

```
def query(self, sql: str, parameters: Iterable[Any] = ()) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.analysis_db:AnalysisDatabase.query`
