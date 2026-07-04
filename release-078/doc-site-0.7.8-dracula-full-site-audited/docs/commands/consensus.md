---
title: x86decomp consensus
description: Exact v0.7.8 parser-derived reference for `x86decomp consensus`.
---


# `x86decomp consensus`

Canonical consensus commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp consensus [-h] [--project PROJECT] [--actor ACTOR]
                           {conflicts,explain,record,resolve,scan} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `conflicts` | `usage: x86decomp consensus conflicts [-h]` | `governance` |
| `explain` | `usage: x86decomp consensus explain [-h] subject_kind subject_id property_name` | `governance` |
| `record` | `usage: x86decomp consensus record [-h] --adapter ADAPTER --adapter-version ADAPTER_VERSION --evidence-id EVIDENCE_ID --group GROUP [--confidence CONFIDENCE] subject_kind subject_id property_name value_json` | `governance` |
| `resolve` | `usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE [--lock] subject_kind subject_id property_name selected_value_json` | `governance` |
| `scan` | `usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND] [--subject-id SUBJECT_ID]` | `governance` |

### `x86decomp consensus conflicts`

```text
usage: x86decomp consensus conflicts [-h]
```

### `x86decomp consensus explain`

```text
usage: x86decomp consensus explain [-h] subject_kind subject_id property_name
```

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required · parser destination: `subject_kind`. No help text declared. |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `property_name` | required · parser destination: `property_name`. No help text declared. |

### `x86decomp consensus record`

```text
usage: x86decomp consensus record [-h] --adapter ADAPTER
                                  --adapter-version ADAPTER_VERSION
                                  --evidence-id EVIDENCE_ID --group GROUP
                                  [--confidence CONFIDENCE]
                                  subject_kind subject_id property_name
                                  value_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required · parser destination: `subject_kind`. No help text declared. |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `property_name` | required · parser destination: `property_name`. No help text declared. |
| `value_json` | required · parser destination: `value_json`. No help text declared. |
| `--adapter` | required · parser destination: `adapter`. No help text declared. |
| `--adapter-version` | required · parser destination: `adapter_version`. No help text declared. |
| `--evidence-id` | required · parser destination: `evidence_id`. No help text declared. |
| `--group` | required · default: `'consensus'` · parser destination: `group`. No help text declared. |
| `--confidence` | type: `float` · default: `1.0` · parser destination: `confidence`. No help text declared. |

### `x86decomp consensus resolve`

```text
usage: x86decomp consensus resolve [-h] --method METHOD --rationale RATIONALE
                                   [--lock]
                                   subject_kind subject_id property_name
                                   selected_value_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `subject_kind` | required · parser destination: `subject_kind`. No help text declared. |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `property_name` | required · parser destination: `property_name`. No help text declared. |
| `selected_value_json` | required · parser destination: `selected_value_json`. No help text declared. |
| `--method` | required · parser destination: `method`. No help text declared. |
| `--rationale` | required · parser destination: `rationale`. No help text declared. |
| `--lock` | nargs: `0` · default: `False` · parser destination: `lock`. No help text declared. |

### `x86decomp consensus scan`

```text
usage: x86decomp consensus scan [-h] [--subject-kind SUBJECT_KIND]
                                [--subject-id SUBJECT_ID]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--subject-kind` | parser destination: `subject_kind`. No help text declared. |
| `--subject-id` | parser destination: `subject_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
