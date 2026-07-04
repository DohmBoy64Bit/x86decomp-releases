---
title: x86decomp counterexample
description: Command reference for `x86decomp counterexample`.
---


# `x86decomp counterexample`

Canonical counterexample commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp counterexample [-h] [--project PROJECT] [--actor ACTOR]
                                {add,list,promote,show} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add` | `usage: x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON [--provenance-json PROVENANCE_JSON] scope_kind scope_id payload` | `governance` |
| `list` | `usage: x86decomp counterexample list [-h]` | `governance` |
| `promote` | `usage: x86decomp counterexample promote [-h] counterexample_id destination` | `governance` |
| `show` | `usage: x86decomp counterexample show [-h] counterexample_id` | `governance` |

### `x86decomp counterexample add`

```text
usage: x86decomp counterexample add [-h] --predicate-json PREDICATE_JSON
                                    [--provenance-json PROVENANCE_JSON]
                                    scope_kind scope_id payload
```

| Argument | Details |
| --- | --- |
| `scope_kind` | required. |
| `scope_id` | required. |
| `payload` | required. |
| `--predicate-json` | required. |
| `--provenance-json` | — |

### `x86decomp counterexample list`

```text
usage: x86decomp counterexample list [-h]
```

### `x86decomp counterexample promote`

```text
usage: x86decomp counterexample promote [-h] counterexample_id destination
```

| Argument | Details |
| --- | --- |
| `counterexample_id` | required. |
| `destination` | required. |

### `x86decomp counterexample show`

```text
usage: x86decomp counterexample show [-h] counterexample_id
```

| Argument | Details |
| --- | --- |
| `counterexample_id` | required. |


