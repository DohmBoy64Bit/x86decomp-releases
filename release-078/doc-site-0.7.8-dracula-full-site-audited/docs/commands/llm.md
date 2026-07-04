---
title: x86decomp llm
description: Exact v0.7.8 parser-derived reference for `x86decomp llm`.
---


# `x86decomp llm`

Canonical llm commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp llm [-h] [--project PROJECT] [--actor ACTOR]
                     {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `batch-create` | `usage: x86decomp llm batch-create [-h] --architecture {x86,x86_64} [--image-base IMAGE_BASE] [--max-bytes MAX_BYTES] [--max-attempts MAX_ATTEMPTS] [--overwrite] project_root output_directory` | `reconstruction` |
| `batch-match` | `usage: x86decomp llm batch-match [-h] [--max-workers MAX_WORKERS] [--max-attempts MAX_ATTEMPTS] [--overwrite] profile compiler_profile jobs output_directory` | `reconstruction` |
| `cpp-generate` | `usage: x86decomp llm cpp-generate [-h] [--class-context CLASS_CONTEXT] [--report REPORT] [--overwrite] profile job output` | `reconstruction` |
| `generate` | `usage: x86decomp llm generate [-h] [--report REPORT] [--overwrite] profile job output` | `reconstruction` |
| `job-create` | `usage: x86decomp llm job-create [-h] --architecture {x86,x86_64} [--image-base IMAGE_BASE] [--function-name FUNCTION_NAME] [--symbol SYMBOL] [--max-attempts MAX_ATTEMPTS] [--inline] [--overwrite] function_packet output` | `reconstruction` |
| `job-from-range` | `usage: x86decomp llm job-from-range [-h] --rva RVA --size SIZE --architecture {x86,x86_64} --function-name FUNCTION_NAME [--symbol SYMBOL] [--image-base IMAGE_BASE] [--mnemonics MNEMONICS] [--max-attempts MAX_ATTEMPTS] [--overwrite] image output` | `reconstruction` |
| `match` | `usage: x86decomp llm match [-h] [--max-attempts MAX_ATTEMPTS] [--overwrite] profile compiler_profile job output_directory` | `reconstruction` |
| `probe` | `usage: x86decomp llm probe [-h] profile` | `reconstruction` |
| `profile-create` | `usage: x86decomp llm profile-create [-h] --model MODEL [--base-url BASE_URL] [--id ID] [--api-key-env API_KEY_ENV] [--allow-remote] {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm} output` | `reconstruction` |
| `profile-validate` | `usage: x86decomp llm profile-validate [-h] profile` | `reconstruction` |
| `prompt` | `usage: x86decomp llm prompt [-h] job output` | `reconstruction` |
| `providers` | `usage: x86decomp llm providers [-h]` | `reconstruction` |
| `verify` | `usage: x86decomp llm verify [-h] report` | `reconstruction` |

### `x86decomp llm batch-create`

```text
usage: x86decomp llm batch-create [-h] --architecture {x86,x86_64}
                                  [--image-base IMAGE_BASE]
                                  [--max-bytes MAX_BYTES]
                                  [--max-attempts MAX_ATTEMPTS] [--overwrite]
                                  project_root output_directory
```

| Argument | Exact parser declaration |
| --- | --- |
| `project_root` | required · parser destination: `project_root`. No help text declared. |
| `output_directory` | required · parser destination: `output_directory`. No help text declared. |
| `--architecture` | required · choices: `x86`, `x86_64` · parser destination: `architecture`. No help text declared. |
| `--image-base` | type: `<lambda>` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--max-bytes` | type: `int` · default: `256` · parser destination: `max_bytes`. No help text declared. |
| `--max-attempts` | type: `int` · default: `4` · parser destination: `max_attempts`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm batch-match`

```text
usage: x86decomp llm batch-match [-h] [--max-workers MAX_WORKERS]
                                 [--max-attempts MAX_ATTEMPTS] [--overwrite]
                                 profile compiler_profile jobs
                                 output_directory
```

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · parser destination: `profile`. No help text declared. |
| `compiler_profile` | required · parser destination: `compiler_profile`. No help text declared. |
| `jobs` | required · parser destination: `jobs`. No help text declared. |
| `output_directory` | required · parser destination: `output_directory`. No help text declared. |
| `--max-workers` | type: `int` · default: `1` · parser destination: `max_workers`. No help text declared. |
| `--max-attempts` | type: `int` · parser destination: `max_attempts`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm cpp-generate`

```text
usage: x86decomp llm cpp-generate [-h] [--class-context CLASS_CONTEXT]
                                  [--report REPORT] [--overwrite]
                                  profile job output
```

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · parser destination: `profile`. No help text declared. |
| `job` | required · parser destination: `job`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--class-context` | parser destination: `class_context`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm generate`

```text
usage: x86decomp llm generate [-h] [--report REPORT] [--overwrite]
                              profile job output
```

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · parser destination: `profile`. No help text declared. |
| `job` | required · parser destination: `job`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--report` | parser destination: `report`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm job-create`

```text
usage: x86decomp llm job-create [-h] --architecture {x86,x86_64}
                                [--image-base IMAGE_BASE]
                                [--function-name FUNCTION_NAME]
                                [--symbol SYMBOL]
                                [--max-attempts MAX_ATTEMPTS] [--inline]
                                [--overwrite]
                                function_packet output
```

| Argument | Exact parser declaration |
| --- | --- |
| `function_packet` | required · parser destination: `function_packet`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--architecture` | required · choices: `x86`, `x86_64` · parser destination: `architecture`. No help text declared. |
| `--image-base` | type: `<lambda>` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--function-name` | parser destination: `function_name`. No help text declared. |
| `--symbol` | parser destination: `symbol`. No help text declared. |
| `--max-attempts` | type: `int` · default: `4` · parser destination: `max_attempts`. No help text declared. |
| `--inline` | nargs: `0` · default: `False` · parser destination: `inline`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm job-from-range`

```text
usage: x86decomp llm job-from-range [-h] --rva RVA --size SIZE
                                    --architecture {x86,x86_64}
                                    --function-name FUNCTION_NAME
                                    [--symbol SYMBOL]
                                    [--image-base IMAGE_BASE]
                                    [--mnemonics MNEMONICS]
                                    [--max-attempts MAX_ATTEMPTS]
                                    [--overwrite]
                                    image output
```

| Argument | Exact parser declaration |
| --- | --- |
| `image` | required · parser destination: `image`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--rva` | required · type: `<lambda>` · parser destination: `rva`. No help text declared. |
| `--size` | required · type: `<lambda>` · parser destination: `size`. No help text declared. |
| `--architecture` | required · choices: `x86`, `x86_64` · parser destination: `architecture`. No help text declared. |
| `--function-name` | required · parser destination: `function_name`. No help text declared. |
| `--symbol` | parser destination: `symbol`. No help text declared. |
| `--image-base` | type: `<lambda>` · default: `0` · parser destination: `image_base`. No help text declared. |
| `--mnemonics` | parser destination: `mnemonics`. No help text declared. |
| `--max-attempts` | type: `int` · default: `4` · parser destination: `max_attempts`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm match`

```text
usage: x86decomp llm match [-h] [--max-attempts MAX_ATTEMPTS] [--overwrite]
                           profile compiler_profile job output_directory
```

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · parser destination: `profile`. No help text declared. |
| `compiler_profile` | required · parser destination: `compiler_profile`. No help text declared. |
| `job` | required · parser destination: `job`. No help text declared. |
| `output_directory` | required · parser destination: `output_directory`. No help text declared. |
| `--max-attempts` | type: `int` · parser destination: `max_attempts`. No help text declared. |
| `--overwrite` | nargs: `0` · default: `False` · parser destination: `overwrite`. No help text declared. |

### `x86decomp llm probe`

```text
usage: x86decomp llm probe [-h] profile
```

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · parser destination: `profile`. No help text declared. |

### `x86decomp llm profile-create`

```text
usage: x86decomp llm profile-create [-h] --model MODEL [--base-url BASE_URL]
                                    [--id ID] [--api-key-env API_KEY_ENV]
                                    [--allow-remote]
                                    {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm}
                                    output
```

| Argument | Exact parser declaration |
| --- | --- |
| `provider` | required · choices: `llama.cpp`, `lm-studio`, `localai`, `ollama`, `openai-compatible`, `vllm` · parser destination: `provider`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |
| `--model` | required · parser destination: `model`. No help text declared. |
| `--base-url` | parser destination: `base_url`. No help text declared. |
| `--id` | parser destination: `id`. No help text declared. |
| `--api-key-env` | parser destination: `api_key_env`. No help text declared. |
| `--allow-remote` | nargs: `0` · default: `False` · parser destination: `allow_remote`. No help text declared. |

### `x86decomp llm profile-validate`

```text
usage: x86decomp llm profile-validate [-h] profile
```

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required · parser destination: `profile`. No help text declared. |

### `x86decomp llm prompt`

```text
usage: x86decomp llm prompt [-h] job output
```

| Argument | Exact parser declaration |
| --- | --- |
| `job` | required · parser destination: `job`. No help text declared. |
| `output` | required · parser destination: `output`. No help text declared. |

### `x86decomp llm providers`

```text
usage: x86decomp llm providers [-h]
```

### `x86decomp llm verify`

```text
usage: x86decomp llm verify [-h] report
```

| Argument | Exact parser declaration |
| --- | --- |
| `report` | required · parser destination: `report`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| reconstruction cli | `src/x86decomp/reconstruction/cli.py` | `dd5a6c7c987b3c49a3f7c1c635d60b34542e21f9346bd85f869013532c844cc4` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
