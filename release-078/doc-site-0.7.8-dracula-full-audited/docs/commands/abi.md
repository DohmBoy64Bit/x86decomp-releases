---
title: x86decomp abi
---

# `x86decomp abi`

Canonical abi commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp abi [-h] [--project PROJECT] [--actor ACTOR]
                     {compare,export,recover,shim,show,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `compare` | `usage: x86decomp abi compare [-h] left_id right_id` |
| `export` | `usage: x86decomp abi export [-h] contract_id output` |
| `recover` | `usage: x86decomp abi recover [-h] --evidence-json EVIDENCE_JSON subject_kind subject_id architecture contract_json` |
| `shim` | `usage: x86decomp abi shim [-h] [--kind KIND] contract_id source_path` |
| `show` | `usage: x86decomp abi show [-h] contract_id` |
| `verify` | `usage: x86decomp abi verify [-h] contract_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp abi compare` | `reconstruction` |
| `x86decomp abi export` | `reconstruction` |
| `x86decomp abi recover` | `reconstruction` |
| `x86decomp abi shim` | `reconstruction` |
| `x86decomp abi show` | `reconstruction` |
| `x86decomp abi verify` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
