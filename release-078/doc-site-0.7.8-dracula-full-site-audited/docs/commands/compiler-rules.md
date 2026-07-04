---
title: x86decomp compiler-rules
description: Exact v0.7.8 parser-derived reference for `x86decomp compiler-rules`.
---


# `x86decomp compiler-rules`

Canonical compiler-rules commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp compiler-rules [-h] [--project PROJECT] [--actor ACTOR]
                                {compare-flags,learn-rule,rule-report} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `compare-flags` | `usage: x86decomp compiler-rules compare-flags [-h] [--output OUTPUT] reports [reports ...]` | `reconstruction` |
| `learn-rule` | `usage: x86decomp compiler-rules learn-rule [-h] rule_id observations output` | `reconstruction` |
| `rule-report` | `usage: x86decomp compiler-rules rule-report [-h] [--output OUTPUT] rules [rules ...]` | `reconstruction` |

### `x86decomp compiler-rules compare-flags`

```text
usage: x86decomp compiler-rules compare-flags [-h] [--output OUTPUT]
                                              reports [reports ...]
```

| Argument | Exact parser declaration |
| --- | --- |
| `reports` | required · nargs: `+` · parser destination: `reports`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

### `x86decomp compiler-rules learn-rule`

```text
usage: x86decomp compiler-rules learn-rule [-h] rule_id observations output
```

| Argument | Exact parser declaration |
| --- | --- |
| `rule_id` | required · parser destination: `rule_id`. No help text declared. |
| `observations` | required · parser destination: `observations`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp compiler-rules rule-report`

```text
usage: x86decomp compiler-rules rule-report [-h] [--output OUTPUT]
                                            rules [rules ...]
```

| Argument | Exact parser declaration |
| --- | --- |
| `rules` | required · nargs: `+` · parser destination: `rules`. No help text declared. |
| `--output` | parser destination: `output`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
