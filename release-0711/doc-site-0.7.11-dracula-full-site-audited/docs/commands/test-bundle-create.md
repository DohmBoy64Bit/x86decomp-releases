---
title: x86decomp test-bundle-create
description: Parser-derived command reference page for `test-bundle-create`.
---

# `x86decomp test-bundle-create`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp test-bundle-create [-h] --artifact ARTIFACT
                                    --authorization AUTHORIZATION
                                    [--name NAME] [--description DESCRIPTION]
                                    [--expected-architecture {x86,x86_64}]
                                    output

positional arguments:
  output

options:
  -h, --help            show this help message and exit
  --artifact ARTIFACT   role=path
  --authorization AUTHORIZATION
  --name NAME
  --description DESCRIPTION
  --expected-architecture {x86,x86_64}
```
