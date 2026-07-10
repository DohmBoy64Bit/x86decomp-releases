---
title: x86decomp.evidence
description: Module reference for x86decomp.evidence.
---

# `x86decomp.evidence`

- Area: `toolkit`
- Source path: `src/x86decomp/evidence.py`
- SHA-256: `5e84e855cf3aa99a089ca44a049786ee37538761fa86b0a3ea988675230818eb`
- Size: `11142` bytes
- Lines: `264`

## Module docstring

Evidence store and strict three-independent-source claim verification.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_validate_id` | 17 | Support validate id processing for internal toolkit callers. |
| class | `EvidenceStore` | 25 | Filesystem-backed evidence and claims with deterministic validation rules. |
| function | `__init__` | 28 | Initialize the instance with validated constructor state. |
| function | `add_evidence` | 38 | Execute the add evidence operation for the current toolkit workflow. |
| function | `get_evidence` | 84 | Execute the get evidence operation for the current toolkit workflow. |
| function | `create_claim` | 106 | Create claim for the current toolkit workflow. |
| function | `get_claim` | 138 | Execute the get claim operation for the current toolkit workflow. |
| function | `save_claim` | 161 | Execute the save claim operation for the current toolkit workflow. |
| function | `attach_evidence` | 166 | Execute the attach evidence operation for the current toolkit workflow. |
| function | `add_contradiction` | 177 | Execute the add contradiction operation for the current toolkit workflow. |
| function | `audit_evidence_integrity` | 187 | Audit evidence integrity for the current toolkit workflow. |
| function | `verify_claim` | 210 | Apply the strict verification gate and persist the resulting state. |
| function | `require_verified` | 256 | Execute the require verified operation for the current toolkit workflow. |
