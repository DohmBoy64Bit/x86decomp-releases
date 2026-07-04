---
title: x86decomp library
---

# `x86decomp library`

Canonical library commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp library [-h] [--project PROJECT] [--actor ACTOR]
                         {accept,candidates,externalize,identify,reconstruct,reject} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `accept` | `usage: x86decomp library accept [-h] match_id` |
| `candidates` | `usage: x86decomp library candidates [-h] subject_id` |
| `externalize` | `usage: x86decomp library externalize [-h] match_id` |
| `identify` | `usage: x86decomp library identify [-h] [--version-range VERSION_RANGE] --confidence CONFIDENCE --evidence-json EVIDENCE_JSON subject_id library_name` |
| `reconstruct` | `usage: x86decomp library reconstruct [-h] match_id` |
| `reject` | `usage: x86decomp library reject [-h] match_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp library accept` | `reconstruction` |
| `x86decomp library candidates` | `reconstruction` |
| `x86decomp library externalize` | `reconstruction` |
| `x86decomp library identify` | `reconstruction` |
| `x86decomp library reconstruct` | `reconstruction` |
| `x86decomp library reject` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
