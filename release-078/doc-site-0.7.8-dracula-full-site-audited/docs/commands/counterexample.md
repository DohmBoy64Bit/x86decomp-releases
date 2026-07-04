---
title: x86decomp counterexample
description: Exact v0.7.8 parser-derived reference for `x86decomp counterexample`.
---


# `x86decomp counterexample`

Canonical counterexample commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp counterexample [-h] [--project PROJECT] [--actor ACTOR]
                                {add,list,promote,show} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `scope_kind` | required · parser destination: `scope_kind`. No help text declared. |
| `scope_id` | required · parser destination: `scope_id`. No help text declared. |
| `payload` | required · parser destination: `payload`. No help text declared. |
| `--predicate-json` | required · parser destination: `predicate_json`. No help text declared. |
| `--provenance-json` | parser destination: `provenance_json`. No help text declared. |

### `x86decomp counterexample list`

```text
usage: x86decomp counterexample list [-h]
```

### `x86decomp counterexample promote`

```text
usage: x86decomp counterexample promote [-h] counterexample_id destination
```

| Argument | Exact parser declaration |
| --- | --- |
| `counterexample_id` | required · parser destination: `counterexample_id`. No help text declared. |
| `destination` | required · parser destination: `destination`. No help text declared. |

### `x86decomp counterexample show`

```text
usage: x86decomp counterexample show [-h] counterexample_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `counterexample_id` | required · parser destination: `counterexample_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
