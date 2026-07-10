---
title: x86decomp compile-worker
description: Parser-derived command reference page for `compile-worker`.
---

# `x86decomp compile-worker`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp compile-worker [-h] [--isolation {local_bounded,container}]
                                [--container-image CONTAINER_IMAGE]
                                [--cache CACHE] [--report REPORT]
                                profile source output

positional arguments:
  profile
  source
  output

options:
  -h, --help            show this help message and exit
  --isolation {local_bounded,container}
  --container-image CONTAINER_IMAGE
  --cache CACHE
  --report REPORT
```
