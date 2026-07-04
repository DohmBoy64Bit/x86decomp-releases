---
title: x86decomp llm
---

# `x86decomp llm`

Canonical llm commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp llm [-h] [--project PROJECT] [--actor ACTOR]
                     {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `batch-create` | `usage: x86decomp llm batch-create [-h] --architecture {x86,x86_64} [--image-base IMAGE_BASE] [--max-bytes MAX_BYTES] [--max-attempts MAX_ATTEMPTS] [--overwrite] project_root output_directory` |
| `batch-match` | `usage: x86decomp llm batch-match [-h] [--max-workers MAX_WORKERS] [--max-attempts MAX_ATTEMPTS] [--overwrite] profile compiler_profile jobs output_directory` |
| `cpp-generate` | `usage: x86decomp llm cpp-generate [-h] [--class-context CLASS_CONTEXT] [--report REPORT] [--overwrite] profile job output` |
| `generate` | `usage: x86decomp llm generate [-h] [--report REPORT] [--overwrite] profile job output` |
| `job-create` | `usage: x86decomp llm job-create [-h] --architecture {x86,x86_64} [--image-base IMAGE_BASE] [--function-name FUNCTION_NAME] [--symbol SYMBOL] [--max-attempts MAX_ATTEMPTS] [--inline] [--overwrite] function_packet output` |
| `job-from-range` | `usage: x86decomp llm job-from-range [-h] --rva RVA --size SIZE --architecture {x86,x86_64} --function-name FUNCTION_NAME [--symbol SYMBOL] [--image-base IMAGE_BASE] [--mnemonics MNEMONICS] [--max-attempts MAX_ATTEMPTS] [--overwrite] image output` |
| `match` | `usage: x86decomp llm match [-h] [--max-attempts MAX_ATTEMPTS] [--overwrite] profile compiler_profile job output_directory` |
| `probe` | `usage: x86decomp llm probe [-h] profile` |
| `profile-create` | `usage: x86decomp llm profile-create [-h] --model MODEL [--base-url BASE_URL] [--id ID] [--api-key-env API_KEY_ENV] [--allow-remote] {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm} output` |
| `profile-validate` | `usage: x86decomp llm profile-validate [-h] profile` |
| `prompt` | `usage: x86decomp llm prompt [-h] job output` |
| `providers` | `usage: x86decomp llm providers [-h]` |
| `verify` | `usage: x86decomp llm verify [-h] report` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp llm batch-create` | `reconstruction` |
| `x86decomp llm batch-match` | `reconstruction` |
| `x86decomp llm cpp-generate` | `reconstruction` |
| `x86decomp llm generate` | `reconstruction` |
| `x86decomp llm job-create` | `reconstruction` |
| `x86decomp llm job-from-range` | `reconstruction` |
| `x86decomp llm match` | `reconstruction` |
| `x86decomp llm probe` | `reconstruction` |
| `x86decomp llm profile-create` | `reconstruction` |
| `x86decomp llm profile-validate` | `reconstruction` |
| `x86decomp llm prompt` | `reconstruction` |
| `x86decomp llm providers` | `reconstruction` |
| `x86decomp llm verify` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
