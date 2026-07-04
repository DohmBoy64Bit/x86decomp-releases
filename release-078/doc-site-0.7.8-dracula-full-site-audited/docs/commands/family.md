---
title: x86decomp family
description: Exact v0.7.8 parser-derived reference for `x86decomp family`.
---


# `x86decomp family`

Canonical family commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp family [-h] [--project PROJECT] [--actor ACTOR]
                        {add,correlate,create,report} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add` | `usage: x86decomp family add [-h] [--metadata-json METADATA_JSON] family_id label path` | `governance` |
| `correlate` | `usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE] left_member_id right_member_id` | `governance` |
| `create` | `usage: x86decomp family create [-h] name` | `governance` |
| `report` | `usage: x86decomp family report [-h] family_id` | `governance` |

### `x86decomp family add`

```text
usage: x86decomp family add [-h] [--metadata-json METADATA_JSON]
                            family_id label path
```

| Argument | Exact parser declaration |
| --- | --- |
| `family_id` | required · parser destination: `family_id`. No help text declared. |
| `label` | required · parser destination: `label`. No help text declared. |
| `path` | required · parser destination: `path`. No help text declared. |
| `--metadata-json` | parser destination: `metadata_json`. No help text declared. |

### `x86decomp family correlate`

```text
usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE]
                                  left_member_id right_member_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `left_member_id` | required · parser destination: `left_member_id`. No help text declared. |
| `right_member_id` | required · parser destination: `right_member_id`. No help text declared. |
| `--block-size` | type: `int` · default: `64` · parser destination: `block_size`. No help text declared. |

### `x86decomp family create`

```text
usage: x86decomp family create [-h] name
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |

### `x86decomp family report`

```text
usage: x86decomp family report [-h] family_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `family_id` | required · parser destination: `family_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
