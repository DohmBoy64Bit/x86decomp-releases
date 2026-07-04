---
title: x86decomp review
description: Exact v0.7.8 parser-derived reference for `x86decomp review`.
---


# `x86decomp review`

Canonical review commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp review [-h] [--project PROJECT] [--actor ACTOR]
                        {assign,create,decide,list,lock,show} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `assign` | `usage: x86decomp review assign [-h] review_id assignee` | `governance` |
| `create` | `usage: x86decomp review create [-h] [--priority PRIORITY] [--details-json DETAILS_JSON] kind subject_id summary` | `governance` |
| `decide` | `usage: x86decomp review decide [-h] --rationale RATIONALE [--lock] review_id decision` | `governance` |
| `list` | `usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]` | `governance` |
| `lock` | `usage: x86decomp review lock [-h] review_id` | `governance` |
| `show` | `usage: x86decomp review show [-h] review_id` | `governance` |

### `x86decomp review assign`

```text
usage: x86decomp review assign [-h] review_id assignee
```

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required · parser destination: `review_id`. No help text declared. |
| `assignee` | required · parser destination: `assignee`. No help text declared. |

### `x86decomp review create`

```text
usage: x86decomp review create [-h] [--priority PRIORITY]
                               [--details-json DETAILS_JSON]
                               kind subject_id summary
```

| Argument | Exact parser declaration |
| --- | --- |
| `kind` | required · parser destination: `kind`. No help text declared. |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `summary` | required · parser destination: `summary`. No help text declared. |
| `--priority` | type: `int` · default: `50` · parser destination: `priority`. No help text declared. |
| `--details-json` | parser destination: `details_json`. No help text declared. |

### `x86decomp review decide`

```text
usage: x86decomp review decide [-h] --rationale RATIONALE [--lock]
                               review_id decision
```

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required · parser destination: `review_id`. No help text declared. |
| `decision` | required · parser destination: `decision`. No help text declared. |
| `--rationale` | required · parser destination: `rationale`. No help text declared. |
| `--lock` | nargs: `0` · default: `False` · parser destination: `lock`. No help text declared. |

### `x86decomp review list`

```text
usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--status` | parser destination: `status`. No help text declared. |
| `--limit` | type: `int` · default: `100` · parser destination: `limit`. No help text declared. |

### `x86decomp review lock`

```text
usage: x86decomp review lock [-h] review_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required · parser destination: `review_id`. No help text declared. |

### `x86decomp review show`

```text
usage: x86decomp review show [-h] review_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `review_id` | required · parser destination: `review_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
