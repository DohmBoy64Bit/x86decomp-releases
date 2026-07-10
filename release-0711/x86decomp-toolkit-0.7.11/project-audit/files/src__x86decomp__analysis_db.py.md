# Per-file audit — src/x86decomp/analysis_db.py

## A. Identity
- Path: `src/x86decomp/analysis_db.py`
- SHA-256: `583910cb27d192fa35e39b0e4165ffa71ac5a1fd77de1b78843245e525e414fe`
- Size: 11680 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 258 lines)
SQLite analysis DB: schema via executescript(_SCHEMA); ingest_function_artifact; add/detect/accept type constraints; query(sql, params). Context-manager lifecycle.

## C/H. Security — SQL
- ALL data-manipulation statements use `?` placeholders with param tuples (verified lines 114–213). No value interpolation.
- query() is the one raw-SQL entry (db-query command, by-design scriptability): guarded to SELECT-only via `normalized.lstrip().lower().startswith('select')`. SQLite execute() runs a single statement, so stacked `SELECT;DROP` is rejected by the driver; SELECT cannot mutate data in stdlib SQLite (no load_extension enabled). Residual: a pathological SELECT can be a CPU/memory DoS, and the connection is not opened read-only — acceptable for a local analyst DB, but note SEC-002 (Low/Informational).

## M. Verdict
Quality high; parameterization disciplined. Final status: Audited — complete.