---
title: x86decomp pipeline-recover
description: reset jobs with stale durable runner heartbeats
original_path: commands/pipeline-recover.html
---

<a id="command-pipeline-recover"></a>

Section: Command reference

# `x86decomp pipeline-recover`

reset jobs with stale durable runner heartbeats

Metadata: current · root command · 1 runnable path

## Help

```
x86decomp pipeline-recover --help
```

Metadata: current · core

## `x86decomp pipeline-recover`

reset jobs with stale durable runner heartbeats

### Usage

```
x86decomp pipeline-recover [-h] [--pipeline-id PIPELINE_ID]
                                  [--stale-seconds STALE_SECONDS]
                                  project
```

### Syntax example

```
x86decomp pipeline-recover ./work
```

### Arguments

| Argument | Source-declared parser metadata |
| --- | --- |
| `project` required · type: _path | No argument help text is declared; parser destination is `project`. |
| `--pipeline-id` | No argument help text is declared; parser destination is `pipeline_id`. |
| `--stale-seconds` default: 600 · type: int | No argument help text is declared; parser destination is `stale_seconds`. |

> **Source basis.** Parser definition: `src/x86decomp/cli.py`; SHA-256 `21e0654ced2f5dd0588adcbedec328613fba524ff1e0a91ef07d63cbbf88288c`. Descriptions above use only parser-declared text or an explicit no-help notice.
