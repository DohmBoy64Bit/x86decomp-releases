---
title: x86decomp changeset
description: Exact parser-derived reference for x86decomp changeset in 0.7.5.
---

# `x86decomp changeset`

Canonical capability group with 10 routes. Shared group options are shown in every exact usage string.

## `x86decomp changeset add-operation`

usage: x86decomp changeset add-operation [-h] changeset_id operation_json

### Usage

```text
x86decomp changeset add-operation [-h] changeset_id operation_json
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required. No help text is declared; parser destination is `changeset_id`. |
| `operation_json` | required. No help text is declared; parser destination is `operation_json`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp changeset apply`

usage: x86decomp changeset apply [-h] path

### Usage

```text
x86decomp changeset apply [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp changeset conflicts`

usage: x86decomp changeset conflicts [-h] changeset_id

### Usage

```text
x86decomp changeset conflicts [-h] changeset_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required. No help text is declared; parser destination is `changeset_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp changeset create`

usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH]

### Usage

```text
x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH]
                                  name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required. No help text is declared; parser destination is `name`. |
| `--base-audit-hash` | declared. No help text is declared; parser destination is `base_audit_hash`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp changeset export`

usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output

### Usage

```text
x86decomp changeset export [-h] [--after-hash AFTER_HASH] output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--after-hash` | declared. No help text is declared; parser destination is `after_hash`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp changeset inspect`

usage: x86decomp changeset inspect [-h] path

### Usage

```text
x86decomp changeset inspect [-h] path
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `path` | required. No help text is declared; parser destination is `path`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `governance` | `src/x86decomp/governance/cli.py` · `faae2889a75675440df013530a18a15c8e3d06b74b119d88a9de4bbed4145f9b` |
## `x86decomp changeset merge`

usage: x86decomp changeset merge [-h] left_id right_id name

### Usage

```text
x86decomp changeset merge [-h] left_id right_id name
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `left_id` | required. No help text is declared; parser destination is `left_id`. |
| `right_id` | required. No help text is declared; parser destination is `right_id`. |
| `name` | required. No help text is declared; parser destination is `name`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp changeset rebase`

usage: x86decomp changeset rebase [-h] changeset_id new_base_hash

### Usage

```text
x86decomp changeset rebase [-h] changeset_id new_base_hash
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required. No help text is declared; parser destination is `changeset_id`. |
| `new_base_hash` | required. No help text is declared; parser destination is `new_base_hash`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp changeset show`

usage: x86decomp changeset show [-h] changeset_id

### Usage

```text
x86decomp changeset show [-h] changeset_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required. No help text is declared; parser destination is `changeset_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp changeset verify`

usage: x86decomp changeset verify [-h] changeset_id

### Usage

```text
x86decomp changeset verify [-h] changeset_id
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `changeset_id` | required. No help text is declared; parser destination is `changeset_id`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
