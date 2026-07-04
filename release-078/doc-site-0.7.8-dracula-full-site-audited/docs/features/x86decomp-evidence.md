---
title: x86decomp.evidence
description: Source module reference for x86decomp.evidence.
---

# `x86decomp.evidence`

**Source path:** `src/x86decomp/evidence.py`  
**Documented symbols:** 13

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `_validate_id` | function | 17 | 21 | — |
| `EvidenceStore` | class | 24 | 252 | Filesystem-backed evidence and claims with deterministic validation rules. |
| `__init__` | function | 27 | 34 | — |
| `add_evidence` | function | 36 | 79 | — |
| `get_evidence` | function | 81 | 100 | — |
| `create_claim` | function | 102 | 131 | — |
| `get_claim` | function | 133 | 153 | — |
| `save_claim` | function | 155 | 157 | — |
| `attach_evidence` | function | 159 | 167 | — |
| `add_contradiction` | function | 169 | 176 | — |
| `audit_evidence_integrity` | function | 178 | 198 | — |
| `verify_claim` | function | 200 | 244 | Apply the strict verification gate and persist the resulting state. |
| `require_verified` | function | 246 | 252 | — |
