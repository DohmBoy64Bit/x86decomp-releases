---
title: x86decomp hypothesis
description: Exact v0.7.8 parser-derived reference for `x86decomp hypothesis`.
---


# `x86decomp hypothesis`

Canonical hypothesis commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp hypothesis [-h] [--project PROJECT] [--actor ACTOR]
                            {create,dependency,evidence,gate,list,show,transition} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `create` | `usage: x86decomp hypothesis create [-h] --origin ORIGIN statement scope_kind scope_id` | `governance` |
| `dependency` | `usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id` | `governance` |
| `evidence` | `usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT --kind KIND --group GROUP [--artifact-sha256 ARTIFACT_SHA256] [--details-json DETAILS_JSON] hypothesis_id evidence_id` | `governance` |
| `gate` | `usage: x86decomp hypothesis gate [-h] hypothesis_id` | `governance` |
| `list` | `usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]` | `governance` |
| `show` | `usage: x86decomp hypothesis show [-h] hypothesis_id` | `governance` |
| `transition` | `usage: x86decomp hypothesis transition [-h] --reason REASON [--lock] hypothesis_id state` | `governance` |

### `x86decomp hypothesis create`

```text
usage: x86decomp hypothesis create [-h] --origin ORIGIN
                                   statement scope_kind scope_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `statement` | required · parser destination: `statement`. No help text declared. |
| `scope_kind` | required · parser destination: `scope_kind`. No help text declared. |
| `scope_id` | required · parser destination: `scope_id`. No help text declared. |
| `--origin` | required · parser destination: `origin`. No help text declared. |

### `x86decomp hypothesis dependency`

```text
usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required · parser destination: `hypothesis_id`. No help text declared. |
| `depends_on_id` | required · parser destination: `depends_on_id`. No help text declared. |

### `x86decomp hypothesis evidence`

```text
usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT
                                     --kind KIND --group GROUP
                                     [--artifact-sha256 ARTIFACT_SHA256]
                                     [--details-json DETAILS_JSON]
                                     hypothesis_id evidence_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required · parser destination: `hypothesis_id`. No help text declared. |
| `evidence_id` | required · parser destination: `evidence_id`. No help text declared. |
| `--stance` | required · parser destination: `stance`. No help text declared. |
| `--weight` | required · type: `float` · parser destination: `weight`. No help text declared. |
| `--kind` | required · parser destination: `kind`. No help text declared. |
| `--group` | required · default: `'hypothesis'` · parser destination: `group`. No help text declared. |
| `--artifact-sha256` | parser destination: `artifact_sha256`. No help text declared. |
| `--details-json` | parser destination: `details_json`. No help text declared. |

### `x86decomp hypothesis gate`

```text
usage: x86decomp hypothesis gate [-h] hypothesis_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required · parser destination: `hypothesis_id`. No help text declared. |

### `x86decomp hypothesis list`

```text
usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--state` | parser destination: `state`. No help text declared. |
| `--scope-id` | parser destination: `scope_id`. No help text declared. |

### `x86decomp hypothesis show`

```text
usage: x86decomp hypothesis show [-h] hypothesis_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required · parser destination: `hypothesis_id`. No help text declared. |

### `x86decomp hypothesis transition`

```text
usage: x86decomp hypothesis transition [-h] --reason REASON [--lock]
                                       hypothesis_id state
```

| Argument | Exact parser declaration |
| --- | --- |
| `hypothesis_id` | required · parser destination: `hypothesis_id`. No help text declared. |
| `state` | required · parser destination: `state`. No help text declared. |
| `--reason` | required · parser destination: `reason`. No help text declared. |
| `--lock` | nargs: `0` · default: `False` · parser destination: `lock`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
