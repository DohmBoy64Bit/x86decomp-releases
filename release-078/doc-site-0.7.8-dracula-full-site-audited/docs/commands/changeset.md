---
title: x86decomp changeset
description: Exact v0.7.8 parser-derived reference for `x86decomp changeset`.
---


# `x86decomp changeset`

Canonical changeset commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp changeset [-h] [--project PROJECT] [--actor ACTOR]
                           {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-operation` | `usage: x86decomp changeset add-operation [-h] changeset_id operation_json` | `reconstruction` |
| `apply` | `usage: x86decomp changeset apply [-h] path` | `governance` |
| `conflicts` | `usage: x86decomp changeset conflicts [-h] changeset_id` | `reconstruction` |
| `create` | `usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH] name` | `reconstruction` |
| `export` | `usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output` | `governance` |
| `inspect` | `usage: x86decomp changeset inspect [-h] path` | `governance` |
| `merge` | `usage: x86decomp changeset merge [-h] left_id right_id name` | `reconstruction` |
| `rebase` | `usage: x86decomp changeset rebase [-h] changeset_id new_base_hash` | `reconstruction` |
| `show` | `usage: x86decomp changeset show [-h] changeset_id` | `reconstruction` |
| `verify` | `usage: x86decomp changeset verify [-h] changeset_id` | `reconstruction` |

### `x86decomp changeset add-operation`

```text
usage: x86decomp changeset add-operation [-h] changeset_id operation_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required · parser destination: `changeset_id`. No help text declared. |
| `operation_json` | required · parser destination: `operation_json`. No help text declared. |

### `x86decomp changeset apply`

```text
usage: x86decomp changeset apply [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

### `x86decomp changeset conflicts`

```text
usage: x86decomp changeset conflicts [-h] changeset_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required · parser destination: `changeset_id`. No help text declared. |

### `x86decomp changeset create`

```text
usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH]
                                  name
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `--base-audit-hash` | parser destination: `base_audit_hash`. No help text declared. |

### `x86decomp changeset export`

```text
usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output
```

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required · parser destination: `output`. No help text declared. |
| `--after-hash` | parser destination: `after_hash`. No help text declared. |

### `x86decomp changeset inspect`

```text
usage: x86decomp changeset inspect [-h] path
```

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required · parser destination: `path`. No help text declared. |

### `x86decomp changeset merge`

```text
usage: x86decomp changeset merge [-h] left_id right_id name
```

| Argument | Exact parser declaration |
| --- | --- |
| `left_id` | required · parser destination: `left_id`. No help text declared. |
| `right_id` | required · parser destination: `right_id`. No help text declared. |
| `name` | required · parser destination: `name`. No help text declared. |

### `x86decomp changeset rebase`

```text
usage: x86decomp changeset rebase [-h] changeset_id new_base_hash
```

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required · parser destination: `changeset_id`. No help text declared. |
| `new_base_hash` | required · parser destination: `new_base_hash`. No help text declared. |

### `x86decomp changeset show`

```text
usage: x86decomp changeset show [-h] changeset_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required · parser destination: `changeset_id`. No help text declared. |

### `x86decomp changeset verify`

```text
usage: x86decomp changeset verify [-h] changeset_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required · parser destination: `changeset_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
