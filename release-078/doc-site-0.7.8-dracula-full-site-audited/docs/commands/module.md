---
title: x86decomp module
description: Exact v0.7.8 parser-derived reference for `x86decomp module`.
---


# `x86decomp module`

Canonical module commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp module [-h] [--project PROJECT] [--actor ACTOR]
                        {add-member,add-unit-member,assign,create,create-unit,list,show,show-unit,suggest} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-member` | `usage: x86decomp module add-member [-h] [--ordinal ORDINAL] [--evidence-json EVIDENCE_JSON] module_id member_kind member_id` | `reconstruction` |
| `add-unit-member` | `usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE] [--ordinal ORDINAL] unit_id member_kind member_id` | `reconstruction` |
| `assign` | `usage: x86decomp module assign [-h] --module MODULE [--class-name CLASS_NAME] [--header HEADER] [--source SOURCE] [--report REPORT] function_id` | `reconstruction` |
| `create` | `usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] name` | `reconstruction` |
| `create-unit` | `usage: x86decomp module create-unit [-h] [--module-id MODULE_ID] [--language LANGUAGE] [--confidence CONFIDENCE] [--evidence-json EVIDENCE_JSON] source_path` | `reconstruction` |
| `list` | `usage: x86decomp module list [-h]` | `reconstruction` |
| `show` | `usage: x86decomp module show [-h] module_id` | `reconstruction` |
| `show-unit` | `usage: x86decomp module show-unit [-h] unit_id` | `reconstruction` |
| `suggest` | `usage: x86decomp module suggest [-h] [--output OUTPUT]` | `reconstruction` |

### `x86decomp module add-member`

```text
usage: x86decomp module add-member [-h] [--ordinal ORDINAL]
                                   [--evidence-json EVIDENCE_JSON]
                                   module_id member_kind member_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `module_id` | required · parser destination: `module_id`. No help text declared. |
| `member_kind` | required · parser destination: `member_kind`. No help text declared. |
| `member_id` | required · parser destination: `member_id`. No help text declared. |
| `--ordinal` | type: `int` · default: `0` · parser destination: `ordinal`. No help text declared. |
| `--evidence-json` | parser destination: `evidence_json`. No help text declared. |

### `x86decomp module add-unit-member`

```text
usage: x86decomp module add-unit-member [-h] [--linkage LINKAGE]
                                        [--ordinal ORDINAL]
                                        unit_id member_kind member_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `unit_id` | required · parser destination: `unit_id`. No help text declared. |
| `member_kind` | required · parser destination: `member_kind`. No help text declared. |
| `member_id` | required · parser destination: `member_id`. No help text declared. |
| `--linkage` | default: `'external'` · parser destination: `linkage`. No help text declared. |
| `--ordinal` | type: `int` · default: `0` · parser destination: `ordinal`. No help text declared. |

### `x86decomp module assign`

```text
usage: x86decomp module assign [-h] --module MODULE [--class-name CLASS_NAME]
                               [--header HEADER] [--source SOURCE]
                               [--report REPORT]
                               function_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required · parser destination: `function_id`. No help text declared. |
| `--module` | required · parser destination: `module`. No help text declared. |
| `--class-name` | parser destination: `class_name`. No help text declared. |
| `--header` | parser destination: `header`. No help text declared. |
| `--source` | parser destination: `source`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |

### `x86decomp module create`

```text
usage: x86decomp module create [-h] [--kind KIND] [--source-path SOURCE_PATH]
                               [--confidence CONFIDENCE]
                               [--evidence-json EVIDENCE_JSON]
                               name
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `--kind` | default: `'static-library'` · parser destination: `kind`. No help text declared. |
| `--source-path` | parser destination: `source_path`. No help text declared. |
| `--confidence` | type: `float` · default: `1.0` · parser destination: `confidence`. No help text declared. |
| `--evidence-json` | parser destination: `evidence_json`. No help text declared. |

### `x86decomp module create-unit`

```text
usage: x86decomp module create-unit [-h] [--module-id MODULE_ID]
                                    [--language LANGUAGE]
                                    [--confidence CONFIDENCE]
                                    [--evidence-json EVIDENCE_JSON]
                                    source_path
```

| Argument | Exact parser declaration |
| --- | --- |
| `source_path` | required · parser destination: `source_path`. No help text declared. |
| `--module-id` | parser destination: `module_id`. No help text declared. |
| `--language` | default: `'cpp'` · parser destination: `language`. No help text declared. |
| `--confidence` | type: `float` · default: `1.0` · parser destination: `confidence`. No help text declared. |
| `--evidence-json` | parser destination: `evidence_json`. No help text declared. |

### `x86decomp module list`

```text
usage: x86decomp module list [-h]
```

### `x86decomp module show`

```text
usage: x86decomp module show [-h] module_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `module_id` | required · parser destination: `module_id`. No help text declared. |

### `x86decomp module show-unit`

```text
usage: x86decomp module show-unit [-h] unit_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `unit_id` | required · parser destination: `unit_id`. No help text declared. |

### `x86decomp module suggest`

```text
usage: x86decomp module suggest [-h] [--output OUTPUT]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
