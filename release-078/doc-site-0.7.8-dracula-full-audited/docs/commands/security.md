---
title: x86decomp security
---

# `x86decomp security`

Canonical security commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp security [-h] [--project PROJECT] [--actor ACTOR]
                          {finding,policy,report,scan} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `finding` | `usage: x86decomp security finding [-h] --evidence-json EVIDENCE_JSON rule_id severity subject_id summary` |
| `policy` | `usage: x86decomp security policy [-h] name policy_json` |
| `report` | `usage: x86decomp security report [-h]` |
| `scan` | `usage: x86decomp security scan [-h] observations_json` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp security finding` | `reconstruction` |
| `x86decomp security policy` | `reconstruction` |
| `x86decomp security report` | `reconstruction` |
| `x86decomp security scan` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
