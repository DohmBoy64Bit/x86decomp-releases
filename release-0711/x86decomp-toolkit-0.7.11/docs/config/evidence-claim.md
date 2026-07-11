# Evidence and claim schemas

Two closely related schemas — `evidence.schema.json` (observation records) and `claim.schema.json` (assertions backed by evidence).

---

## Evidence record

`$id: urn:x86decomp:schema:evidence:1` — schema version 1.

Validated against `schemas/evidence.schema.json`.

An evidence record captures a single observation — a byte range, analysis result, trace, compiler output, debug symbol, document, or human review.

### Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `id` | string | Pattern `^[a-z0-9][a-z0-9._:-]{2,127}$` — 3–128 chars |
| `kind` | enum | One of 7 values (see below) |
| `source` | string | minLength 1 — tool or origin |
| `locator` | string | minLength 1 — file:offset, RVA, or URL |
| `assertion` | string | minLength 1 — what was observed |
| `independent_group` | string | minLength 1 — independence grouping for verification |
| `digest_sha256` | string or null | Pattern `^[0-9a-f]{64}$` (optional) |
| `observed_at` | string | date-time format |
| `metadata` | object | Free-form context (tool version, parameters, etc.) |

### `kind` values (7 total)

| Value | Meaning |
|-------|---------|
| `binary_bytes` | Immutable bytes or directly decoded values |
| `static_analysis` | Ghidra, Capstone, or non-executing analysis result |
| `dynamic_trace` | Observed execution in a controlled environment |
| `compiler_output` | Compiler object, listing, diagnostics, or match report |
| `debug_symbol` | PDB or other symbol tied to an identifiable build |
| `external_document` | Authoritative format/compiler/tool documentation |
| `human_review` | Signed analyst review (not independently machine-verifiable) |

### `independent_group`

Used in the verification gate: a claim reaching `verified` status requires evidence from at least **three** distinct `independent_group` values across at least **two** distinct `kind` values. This prevents one tool from self-corroborating through multiple views of the same internal state.

!!! tip
    Use `digest_sha256` when the evidence references a specific file. Set it to `null` for non-file evidence (e.g. observations from an interactive debugger session).

---

## Claim

`$id: urn:x86decomp:schema:claim:1` — schema version 1.

Validated against `schemas/claim.schema.json`.

A claim is a subject-predicate-object assertion backed by evidence. Claims progress through states as evidence accumulates and contradictions are resolved.

### Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `id` | string | Pattern `^[a-z0-9][a-z0-9._:-]{2,127}$` |
| `subject` | string | minLength 1 |
| `predicate` | string | minLength 1 |
| `object` | string | minLength 1 |
| `state` | enum | One of 4 values |
| `evidence_ids` | array of strings | uniqueItems — references to evidence `id`s |
| `contradiction_ids` | array of strings | uniqueItems — references to contradictory evidence |
| `notes` | array of strings | Analyst notes |
| `created_at` | string | date-time format |
| `updated_at` | string | date-time format |

### `state` values (4 total)

| Value | Meaning |
|-------|---------|
| `proposed` | Claim has been stated but lacks sufficient evidence |
| `corroborated` | At least two evidence records support the claim |
| `verified` | Three evidence records, three independent groups, two kinds, no contradictions |
| `rejected` | Claim has been contradicted by evidence |

---

## Verification gate

For a claim to reach `verified`, all five conditions must hold:

1. At least three evidence records in `evidence_ids`.
2. At least three distinct `independent_group` values across those records.
3. At least two distinct evidence `kind` values.
4. All file-backed evidence hashes still match at current paths.
5. `contradiction_ids` is empty (no unresolved contradictions).

---

## Examples

### Evidence record

```json
{
  "id": "ev.pe-header.0",
  "kind": "binary_bytes",
  "source": "x86decomp pe analyze",
  "locator": "original/game.exe:0x0000-0x01FF",
  "assertion": "PE signature at offset 0x80, machine type 0x014C (i386), 4 sections",
  "independent_group": "pe-header",
  "digest_sha256": null,
  "observed_at": "2026-07-01T12:00:00Z",
  "metadata": {
    "tool_version": "0.7.11",
    "architecture": "x86"
  }
}
```

### Claim

```json
{
  "id": "claim.abi.main",
  "subject": "function:pe-rva:00001000",
  "predicate": "has_calling_convention",
  "object": "__cdecl",
  "state": "corroborated",
  "evidence_ids": [
    "ev.byte-analyzer.1",
    "ev.ghidra-callsites.3"
  ],
  "contradiction_ids": [],
  "notes": [
    "Matches compiler output for msvc6 /Gd default",
    "Awaiting dynamic trace evidence for verification"
  ],
  "created_at": "2026-07-01T12:00:00Z",
  "updated_at": "2026-07-02T09:30:00Z"
}
```
