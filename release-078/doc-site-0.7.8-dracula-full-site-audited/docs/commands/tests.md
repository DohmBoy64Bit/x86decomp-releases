---
title: x86decomp tests
description: Exact v0.7.8 parser-derived reference for `x86decomp tests`.
---


# `x86decomp tests`

Canonical tests commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp tests [-h] [--project PROJECT] [--actor ACTOR]
                       {add,explain,list,promote-counterexample,synthesize} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add` | `usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON --evidence-json EVIDENCE_JSON name scope_kind scope_id test_kind relative_path content_file` | `reconstruction` |
| `explain` | `usage: x86decomp tests explain [-h] test_id` | `reconstruction` |
| `list` | `usage: x86decomp tests list [-h]` | `reconstruction` |
| `promote-counterexample` | `usage: x86decomp tests promote-counterexample [-h] [--name NAME] counterexample_id` | `reconstruction` |
| `synthesize` | `usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id` | `reconstruction` |

### `x86decomp tests add`

```text
usage: x86decomp tests add [-h] --applicability-json APPLICABILITY_JSON
                           --evidence-json EVIDENCE_JSON
                           name scope_kind scope_id test_kind relative_path
                           content_file
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `scope_kind` | required · parser destination: `scope_kind`. No help text declared. |
| `scope_id` | required · parser destination: `scope_id`. No help text declared. |
| `test_kind` | required · parser destination: `test_kind`. No help text declared. |
| `relative_path` | required · parser destination: `relative_path`. No help text declared. |
| `content_file` | required · parser destination: `content_file`. No help text declared. |
| `--applicability-json` | required · parser destination: `applicability_json`. No help text declared. |
| `--evidence-json` | required · parser destination: `evidence_json`. No help text declared. |

### `x86decomp tests explain`

```text
usage: x86decomp tests explain [-h] test_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `test_id` | required · parser destination: `test_id`. No help text declared. |

### `x86decomp tests list`

```text
usage: x86decomp tests list [-h]
```

### `x86decomp tests promote-counterexample`

```text
usage: x86decomp tests promote-counterexample [-h] [--name NAME]
                                              counterexample_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `counterexample_id` | required · parser destination: `counterexample_id`. No help text declared. |
| `--name` | parser destination: `name`. No help text declared. |

### `x86decomp tests synthesize`

```text
usage: x86decomp tests synthesize [-h] [--name NAME] scope_kind scope_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `scope_kind` | required · parser destination: `scope_kind`. No help text declared. |
| `scope_id` | required · parser destination: `scope_id`. No help text declared. |
| `--name` | parser destination: `name`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
