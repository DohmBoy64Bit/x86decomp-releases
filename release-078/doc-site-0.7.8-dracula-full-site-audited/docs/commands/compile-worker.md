---
title: x86decomp compile-worker
description: Command reference for `x86decomp compile-worker`.
---


# `x86decomp compile-worker`

## Usage

```text
usage: x86decomp compile-worker [-h] [--isolation {local_bounded,container}]
                                [--container-image CONTAINER_IMAGE]
                                [--cache CACHE] [--report REPORT]
                                profile source output
```

## Arguments

| Argument | Details |
| --- | --- |
| `profile` | required · type: `path`. |
| `source` | required · type: `path`. |
| `output` | required · type: `path`. |
| `--isolation` | choices: `local_bounded`, `container` · default: `'local_bounded'`. |
| `--container-image` | — |
| `--cache` | type: `path`. |
| `--report` | type: `path`. |


