---
title: x86decomp graph
description: Canonical graph commands implemented by the current capability subsystem.
original_path: commands/graph.html
---

<a id="command-graph-edge"></a>
<a id="command-graph-impact"></a>
<a id="command-graph-node"></a>

Section: Command reference

# `x86decomp graph`

Canonical graph commands implemented by the current capability subsystem.

Metadata: current · canonical group · 3 runnable paths

## Help

```
x86decomp graph --help
```

Metadata: current · governance

## `x86decomp graph edge`

edge command

### Usage

```
x86decomp graph edge [-h] [--attributes-json ATTRIBUTES_JSON]
                            source_id target_id relation
```

### Syntax example

```
x86decomp graph edge ./candidate.c ./target.exe example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `source_id` required | No argument help text is declared; parser destination is `source_id`. |
| `target_id` required | No argument help text is declared; parser destination is `target_id`. |
| `relation` required | No argument help text is declared; parser destination is `relation`. |
| `--attributes-json` | No argument help text is declared; parser destination is `attributes_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp graph impact`

impact command

### Usage

```
x86decomp graph impact [-h] [--direction DIRECTION]
                              [--max-depth MAX_DEPTH] [--relations RELATIONS]
                              node_id
```

### Syntax example

```
x86decomp graph impact example-001
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `node_id` required | No argument help text is declared; parser destination is `node_id`. |
| `--direction` default: 'outbound' | No argument help text is declared; parser destination is `direction`. |
| `--max-depth` default: 8 · type: int | No argument help text is declared; parser destination is `max_depth`. |
| `--relations` | No argument help text is declared; parser destination is `relations`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.

Metadata: current · governance

## `x86decomp graph node`

node command

### Usage

```
x86decomp graph node [-h] [--attributes-json ATTRIBUTES_JSON]
                            node_id kind label
```

### Syntax example

```
x86decomp graph node example-001 analysis example
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `node_id` required | No argument help text is declared; parser destination is `node_id`. |
| `kind` required | No argument help text is declared; parser destination is `kind`. |
| `label` required | No argument help text is declared; parser destination is `label`. |
| `--attributes-json` | No argument help text is declared; parser destination is `attributes_json`. |

> **Source basis.** Parser definition: `src/x86decomp/governance/cli.py`; SHA-256 `690a4e9b2db9efbe402f77a87c0e7d5eaedddd487aebc3efabed9e3df208f5eb`. Descriptions above use only parser-declared text or an explicit no-help notice.
