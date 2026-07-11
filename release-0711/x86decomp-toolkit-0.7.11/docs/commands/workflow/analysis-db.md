# Analysis Database Commands

Ingest analysis artifacts, run bounded read-only SQL queries, and manage provenance-bearing type constraints.

## `db-ingest`

Ingest an analysis artifact into the project database.

```bash
x86decomp db-ingest DATABASE ARTIFACT --image-base 0
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database file |
| `ARTIFACT` | yes | Path to the analysis artifact file to ingest |
| `--image-base` | no | Image base address for relocation (default: `0`) |

Ingested artifacts populate function metadata tables for subsequent query and constraint operations.

### Example

```bash
x86decomp db-ingest ./db/analysis.db ./artifacts/ghidra-export/pe-rva_00401000.json --image-base 0x400000
```

---

## `db-query`

Run a bounded read-only SQL query against the analysis database.

```bash
x86decomp db-query DATABASE SQL --parameters-json "[]"
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database file |
| `SQL` | yes | SQL query string (read-only operations only) |
| `--parameters-json` | no | JSON array of query parameters (default: `"[]"`) |

!!! warning "Read-only only"
    The database connection is opened in read-only mode. Mutating queries (INSERT, UPDATE, DELETE, DROP) are rejected.

### Examples

```bash
# List all ingested functions
x86decomp db-query ./db/analysis.db "SELECT function_id, name, start_rva, end_rva FROM functions"

# Parameterized query
x86decomp db-query ./db/analysis.db \
  "SELECT * FROM functions WHERE start_rva >= ?" \
  --parameters-json "[4198400]"
```

---

## `db-constraint-add`

Add a provenance-bearing analysis constraint.

```bash
x86decomp db-constraint-add DATABASE SUBJECT RELATION OBJECT_VALUE PROVENANCE \
  --evidence-id ID --confidence FLOAT
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database file |
| `SUBJECT` | yes | Subject entity (e.g. function ID, variable name) |
| `RELATION` | yes | Relation type (e.g. `has_type`, `is_parameter`) |
| `OBJECT_VALUE` | yes | Object value (e.g. type string, parameter index) |
| `PROVENANCE` | yes | Provenance source (tool, analyst, document) |
| `--evidence-id` | no | Linked evidence record ID |
| `--confidence` | no | Confidence score as a float |

### Example

```bash
x86decomp db-constraint-add ./db/analysis.db \
  "pe-rva:00401000:arg_0" has_type "int*" \
  "ghidra-parameter-analysis" \
  --evidence-id ghidra-401000-params \
  --confidence 0.85

x86decomp db-constraint-add ./db/analysis.db \
  "pe-rva:00401000" has_calling_convention "__cdecl" \
  "compiler-experiment" \
  --evidence-id compiler-401000-cdecl \
  --confidence 0.95
```

---

## `db-constraint-conflicts`

List conflicting constraints for a subject and relation.

```bash
x86decomp db-constraint-conflicts DATABASE SUBJECT RELATION
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database file |
| `SUBJECT` | yes | Subject entity to check |
| `RELATION` | yes | Relation type to check for conflicts |

Returns conflicting constraint pairs where the same subject has multiple, differing values for the same relation.

### Example

```bash
x86decomp db-constraint-conflicts ./db/analysis.db "pe-rva:00401000" has_type

x86decomp db-constraint-conflicts ./db/analysis.db "pe-rva:00401000:arg_0" is_parameter
```

---

## `db-constraint-accept`

Accept a selected analysis constraint (resolving conflicts).

```bash
x86decomp db-constraint-accept DATABASE CONSTRAINT_ID
```

| Argument | Required | Description |
|---|---|---|
| `DATABASE` | yes | Path to the analysis database file |
| `CONSTRAINT_ID` | yes | Integer constraint identifier to accept |

!!! note
    Accepting a constraint resolves conflicts by marking other conflicting constraints as rejected. Use `db-constraint-conflicts` first to review all conflicting values.

### Example

```bash
# First, list conflicts
x86decomp db-constraint-conflicts ./db/analysis.db "pe-rva:00401000:arg_0" has_type

# Then accept the correct constraint
x86decomp db-constraint-accept ./db/analysis.db 15
```
