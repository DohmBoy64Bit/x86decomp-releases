---
title: x86decomp changeset
---

# `x86decomp changeset`

Canonical changeset commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp changeset [-h] [--project PROJECT] [--actor ACTOR]
                           {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add-operation` | `usage: x86decomp changeset add-operation [-h] changeset_id operation_json` |
| `apply` | `usage: x86decomp changeset apply [-h] path` |
| `conflicts` | `usage: x86decomp changeset conflicts [-h] changeset_id` |
| `create` | `usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH] name` |
| `export` | `usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output` |
| `inspect` | `usage: x86decomp changeset inspect [-h] path` |
| `merge` | `usage: x86decomp changeset merge [-h] left_id right_id name` |
| `rebase` | `usage: x86decomp changeset rebase [-h] changeset_id new_base_hash` |
| `show` | `usage: x86decomp changeset show [-h] changeset_id` |
| `verify` | `usage: x86decomp changeset verify [-h] changeset_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp changeset add-operation` | `reconstruction` |
| `x86decomp changeset apply` | `governance` |
| `x86decomp changeset conflicts` | `reconstruction` |
| `x86decomp changeset create` | `reconstruction` |
| `x86decomp changeset export` | `governance` |
| `x86decomp changeset inspect` | `governance` |
| `x86decomp changeset merge` | `reconstruction` |
| `x86decomp changeset rebase` | `reconstruction` |
| `x86decomp changeset show` | `reconstruction` |
| `x86decomp changeset verify` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
