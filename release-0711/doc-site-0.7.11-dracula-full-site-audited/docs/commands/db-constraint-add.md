---
title: x86decomp db-constraint-add
description: Parser-derived command reference page for `db-constraint-add`.
---

# `x86decomp db-constraint-add`

Source: `0.7.11` parser surface.

This root command is a direct parser entry point, compatibility command, or non-canonical helper command. It is counted in the root command surface and intentionally not double-counted as a canonical route when it aliases another command family.

## Parser help

```text
usage: x86decomp db-constraint-add [-h] [--evidence-id EVIDENCE_ID]
                                   [--confidence CONFIDENCE]
                                   database subject relation object_value
                                   provenance

positional arguments:
  database
  subject
  relation
  object_value
  provenance

options:
  -h, --help            show this help message and exit
  --evidence-id EVIDENCE_ID
  --confidence CONFIDENCE
```
