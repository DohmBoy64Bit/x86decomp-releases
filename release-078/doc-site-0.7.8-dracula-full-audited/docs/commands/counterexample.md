---
title: x86decomp counterexample
---

# `x86decomp counterexample`

Canonical counterexample commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp counterexample [-h] [--project PROJECT] [--actor ACTOR]
                                {add,list,promote,show} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add` | `usage: x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON [--provenance-json PROVENANCE_JSON] scope_kind scope_id payload` |
| `list` | `usage: x86decomp counterexample list [-h]` |
| `promote` | `usage: x86decomp counterexample promote [-h] counterexample_id destination` |
| `show` | `usage: x86decomp counterexample show [-h] counterexample_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp counterexample add` | `governance` |
| `x86decomp counterexample list` | `governance` |
| `x86decomp counterexample promote` | `governance` |
| `x86decomp counterexample show` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
