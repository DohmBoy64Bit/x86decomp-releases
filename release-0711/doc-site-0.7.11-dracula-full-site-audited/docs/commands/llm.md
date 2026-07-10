---
title: x86decomp llm
description: Parser-derived command reference page for `llm`.
---

# `x86decomp llm`

Source: `0.7.11` parser surface.

## Canonical routes

| Action | Owner |
| --- | --- |
| `batch-create` | `reconstruction` |
| `batch-match` | `reconstruction` |
| `cpp-generate` | `reconstruction` |
| `generate` | `reconstruction` |
| `job-create` | `reconstruction` |
| `job-from-range` | `reconstruction` |
| `match` | `reconstruction` |
| `probe` | `reconstruction` |
| `profile-create` | `reconstruction` |
| `profile-validate` | `reconstruction` |
| `prompt` | `reconstruction` |
| `providers` | `reconstruction` |
| `verify` | `reconstruction` |
## Parser help

```text
usage: x86decomp llm [-h] [--project PROJECT] [--actor ACTOR]
                     {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify} ...

Canonical llm commands implemented by the current capability subsystem.

positional arguments:
  {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify}
    batch-create        create local-LLM jobs for eligible project function
                        packets
    batch-match         run bounded match loops for a deterministic job queue
    cpp-generate        generate one bounded C++ proposal using a local-model
                        profile
    generate            generate one uncompiled C proposal
    job-create          create a local-LLM job from a function packet
    job-from-range      create a local-LLM job from an explicit byte range
    match               run bounded generation, compilation, relocation
                        resolution, and exact byte matching
    probe               probe the provider model-list endpoint
    profile-create      create a validated local-model provider profile
    profile-validate    validate a local-model provider profile
    prompt              materialize the deterministic prompt without
                        contacting a model
    providers           list built-in local-model provider presets
    verify              verify a local-model byte-match report and accepted
                        artifact hashes

options:
  -h, --help            show this help message and exit
  --project PROJECT     project root used by the capability implementation
                        (default: current directory)
  --actor ACTOR
```
