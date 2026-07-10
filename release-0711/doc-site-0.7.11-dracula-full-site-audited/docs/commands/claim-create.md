---
title: x86decomp claim-create
description: Parser-derived command reference page for `claim-create`.
---

# `x86decomp claim-create`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp claim-create [-h] --subject SUBJECT --predicate PREDICATE
                              --object OBJECT_VALUE [--evidence EVIDENCE]
                              [--id ID]
                              project

positional arguments:
  project

options:
  -h, --help            show this help message and exit
  --subject SUBJECT
  --predicate PREDICATE
  --object OBJECT_VALUE
  --evidence EVIDENCE
  --id ID
```
