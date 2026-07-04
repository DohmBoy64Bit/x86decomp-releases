---
title: x86decomp security
description: Exact v0.7.8 parser-derived reference for `x86decomp security`.
---


# `x86decomp security`

Canonical security commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp security [-h] [--project PROJECT] [--actor ACTOR]
                          {finding,policy,report,scan} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `finding` | `usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON rule_id severity subject_id summary` | `reconstruction` |
| `policy` | `usage: x86decomp security policy [-h] name policy_json` | `reconstruction` |
| `report` | `usage: x86decomp security report [-h]` | `reconstruction` |
| `scan` | `usage: x86decomp security scan [-h] observations_json` | `reconstruction` |

### `x86decomp security finding`

```text
usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON
                                  rule_id severity subject_id summary
```

| Argument | Exact parser declaration |
| --- | --- |
| `rule_id` | required · parser destination: `rule_id`. No help text declared. |
| `severity` | required · parser destination: `severity`. No help text declared. |
| `subject_id` | required · parser destination: `subject_id`. No help text declared. |
| `summary` | required · parser destination: `summary`. No help text declared. |
| `--evidence-json` | required · parser destination: `evidence_json`. No help text declared. |

### `x86decomp security policy`

```text
usage: x86decomp security policy [-h] name policy_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `name` | required · parser destination: `name`. No help text declared. |
| `policy_json` | required · parser destination: `policy_json`. No help text declared. |

### `x86decomp security report`

```text
usage: x86decomp security report [-h]
```

### `x86decomp security scan`

```text
usage: x86decomp security scan [-h] observations_json
```

| Argument | Exact parser declaration |
| --- | --- |
| `observations_json` | required · parser destination: `observations_json`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
