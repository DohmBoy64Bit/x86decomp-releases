---
title: x86decomp content-put
description: Parser-derived command reference page for `content-put`.
---

# `x86decomp content-put`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp content-put [-h] [--media-type MEDIA_TYPE]
                             [--reference REFERENCE] [--kind KIND]
                             [--owner OWNER]
                             store file

positional arguments:
  store
  file

options:
  -h, --help            show this help message and exit
  --media-type MEDIA_TYPE
  --reference REFERENCE
  --kind KIND
  --owner OWNER
```
