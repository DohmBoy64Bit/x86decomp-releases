---
title: x86decomp counterexample
description: Exact parser-derived reference for x86decomp counterexample in 0.7.5.
---

# `x86decomp counterexample`

Canonical capability group with 4 routes. Shared group options are shown in every exact usage string.

## `x86decomp counterexample add`

usage: x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON

### Usage

```text
x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON
                                    [--provenance-json PROVENANCE_JSON]
                                    scope_kind scope_id payload
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `scope_kind` | required. No help text is declared; parser destination is `scope_kind`. |
| `scope_id` | required. No help text is declared; parser destination is `scope_id`. |
| `payload` | required. No help text is declared; parser destination is `payload`. |
| `--predicate-json` | required. No help text is declared; parser destination is `predicate_json`. |
| `--provenance-json` | declared. No help text is declared; parser destination is `provenance_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp counterexample list`

usage: x86decomp counterexample list [-h]

### Usage

```text
x86decomp counterexample list [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp counterexample promote`

usage: x86decomp counterexample promote [-h] counterexample_id destination

### Usage

```text
x86decomp counterexample promote [-h] counterexample_id destination
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `counterexample_id` | required. No help text is declared; parser destination is `counterexample_id`. |
| `destination` | required. No help text is declared; parser destination is `destination`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp counterexample show`

usage: x86decomp counterexample show [-h] counterexample_id

### Usage

```text
x86decomp counterexample show [-h] counterexample_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `counterexample_id` | required. No help text is declared; parser destination is `counterexample_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
