---
title: x86decomp pipeline-cancel
description: Parser-derived command reference page for `pipeline-cancel`.
---

# `x86decomp pipeline-cancel`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp pipeline-cancel [-h] [--stage-id STAGE_ID]
                                 project pipeline_id

positional arguments:
  project
  pipeline_id

options:
  -h, --help           show this help message and exit
  --stage-id STAGE_ID
```
