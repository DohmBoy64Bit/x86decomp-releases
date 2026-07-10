---
title: x86decomp campaign
description: Parser-derived command reference page for `campaign`.
---

# `x86decomp campaign`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `branch` | `governance` |
| `create` | `governance` |
| `list` | `governance` |
| `pause` | `governance` |
| `plan` | `governance` |
| `resume` | `governance` |
| `snapshot` | `governance` |
| `start` | `governance` |
| `status` | `governance` |
| `stop` | `governance` |
## Parser help

```text
usage: x86decomp campaign [-h] [--project PROJECT] [--actor ACTOR]
                          {branch,create,list,pause,plan,resume,snapshot,start,status,stop} ...

Canonical campaign commands implemented by the current capability subsystem.

positional arguments:
  {branch,create,list,pause,plan,resume,snapshot,start,status,stop}
    branch              branch command
    create              create command
    list                list command
    pause               pause command
    plan                plan command
    resume              resume command
    snapshot            snapshot command
    start               start command
    status              status command
    stop                stop command

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
