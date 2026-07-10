---
title: x86decomp.analysis_db
description: Module reference for x86decomp.analysis_db.
---

# `x86decomp.analysis_db`

- Area: `toolkit`
- Source path: `src/x86decomp/analysis_db.py`
- SHA-256: `583910cb27d192fa35e39b0e4165ffa71ac5a1fd77de1b78843245e525e414fe`
- Size: `11680` bytes
- Lines: `258`

## Module docstring

SQLite-backed global symbol, type, reference, and constraint database.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `AnalysisDatabase` | 70 | Coordinate analysis database behavior for the current toolkit workflow. |
| function | `__init__` | 72 | Initialize the instance with validated constructor state. |
| function | `close` | 80 | Execute the close operation for the current toolkit workflow. |
| function | `__enter__` | 84 | Enter the managed runtime context and return the active resource. |
| function | `__exit__` | 88 | Exit the managed runtime context and release owned resources. |
| function | `upsert_entity` | 96 | Execute the upsert entity operation for the current toolkit workflow. |
| function | `add_reference` | 126 | Execute the add reference operation for the current toolkit workflow. |
| function | `add_type_constraint` | 145 | Execute the add type constraint operation for the current toolkit workflow. |
| function | `detect_constraint_conflicts` | 167 | Execute the detect constraint conflicts operation for the current toolkit workflow. |
| function | `accept_constraint` | 183 | Execute the accept constraint operation for the current toolkit workflow. |
| function | `ingest_function_artifact` | 196 | Execute the ingest function artifact operation for the current toolkit workflow. |
| function | `query` | 252 | Execute the query operation for the current toolkit workflow. |
