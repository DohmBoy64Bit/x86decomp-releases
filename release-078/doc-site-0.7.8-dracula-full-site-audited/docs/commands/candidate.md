---
title: x86decomp candidate
description: Exact v0.7.8 parser-derived reference for `x86decomp candidate`.
---


# `x86decomp candidate`

Canonical candidate commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp candidate [-h] [--project PROJECT] [--actor ACTOR]
                           {add-file,compare,create,evaluate,list,promote,search,show,transition} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-file` | `usage: x86decomp candidate add-file [-h] candidate_id source relative_path` | `governance` |
| `compare` | `usage: x86decomp candidate compare [-h] left_id right_id` | `governance` |
| `create` | `usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID] [--parent PARENT] [--objective-json OBJECTIVE_JSON] branch_name` | `governance` |
| `evaluate` | `usage: x86decomp candidate evaluate [-h] [--value VALUE] [--details-json DETAILS_JSON] candidate_id metric status` | `governance` |
| `list` | `usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]` | `governance` |
| `promote` | `usage: x86decomp candidate promote [-h] --candidate CANDIDATE --report REPORT [--stage STAGE] [--update-workflow] [--update-build] [--overwrite] function_id` | `reconstruction` |
| `search` | `usage: x86decomp candidate search [-h] [--phase PHASE] [--output OUTPUT]` | `reconstruction` |
| `show` | `usage: x86decomp candidate show [-h] candidate_id` | `governance` |
| `transition` | `usage: x86decomp candidate transition [-h] --reason REASON candidate_id state` | `governance` |

### `x86decomp candidate add-file`

```text
usage: x86decomp candidate add-file [-h] candidate_id source relative_path
```

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required · parser destination: `candidate_id`. No help text declared. |
| `source` | required · parser destination: `source`. No help text declared. |
| `relative_path` | required · parser destination: `relative_path`. No help text declared. |

### `x86decomp candidate compare`

```text
usage: x86decomp candidate compare [-h] left_id right_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `left_id` | required · parser destination: `left_id`. No help text declared. |
| `right_id` | required · parser destination: `right_id`. No help text declared. |

### `x86decomp candidate create`

```text
usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID]
                                  [--parent PARENT]
                                  [--objective-json OBJECTIVE_JSON]
                                  branch_name
```

| Argument | Exact parser declaration |
| --- | --- |
| `branch_name` | required · parser destination: `branch_name`. No help text declared. |
| `--campaign-id` | parser destination: `campaign_id`. No help text declared. |
| `--parent` | parser destination: `parent`. No help text declared. |
| `--objective-json` | parser destination: `objective_json`. No help text declared. |

### `x86decomp candidate evaluate`

```text
usage: x86decomp candidate evaluate [-h] [--value VALUE]
                                    [--details-json DETAILS_JSON]
                                    candidate_id metric status
```

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required · parser destination: `candidate_id`. No help text declared. |
| `metric` | required · parser destination: `metric`. No help text declared. |
| `status` | required · parser destination: `status`. No help text declared. |
| `--value` | type: `float` · parser destination: `value`. No help text declared. |
| `--details-json` | parser destination: `details_json`. No help text declared. |

### `x86decomp candidate list`

```text
usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--campaign-id` | parser destination: `campaign_id`. No help text declared. |

### `x86decomp candidate promote`

```text
usage: x86decomp candidate promote [-h] --candidate CANDIDATE --report REPORT
                                   [--stage STAGE] [--update-workflow]
                                   [--update-build] [--overwrite]
                                   function_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `function_id` | required · parser destination: `function_id`. No help text declared. |
| `--candidate` | required · parser destination: `candidate`. No help text declared. |
| `--report` | required · parser destination: `report`. No help text declared. |
| `--stage` | default: `'matched'` · parser destination: `stage`. No help text declared. |
| `--update-workflow` | nargs: `0` · default: `False` · parser destination: `update_workflow`. No help text declared. |
| `--update-build` | nargs: `0` · default: `False` · parser destination: `update_build`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp candidate search`

```text
usage: x86decomp candidate search [-h] [--phase PHASE] [--output OUTPUT]
```

| Argument | Exact parser declaration |
| --- | --- |
| `--phase` | parser destination: `phase`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp candidate show`

```text
usage: x86decomp candidate show [-h] candidate_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required · parser destination: `candidate_id`. No help text declared. |

### `x86decomp candidate transition`

```text
usage: x86decomp candidate transition [-h] --reason REASON candidate_id state
```

| Argument | Exact parser declaration |
| --- | --- |
| `candidate_id` | required · parser destination: `candidate_id`. No help text declared. |
| `state` | required · parser destination: `state`. No help text declared. |
| `--reason` | required · parser destination: `reason`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
