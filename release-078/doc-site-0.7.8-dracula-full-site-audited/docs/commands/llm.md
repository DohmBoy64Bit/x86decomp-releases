---
title: x86decomp llm
description: Command reference for `x86decomp llm`.
---


# `x86decomp llm`

Canonical llm commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp llm [-h] [--project PROJECT] [--actor ACTOR]
                     {batch-create,batch-match,cpp-generate,generate,job-create,job-from-range,match,probe,profile-create,profile-validate,prompt,providers,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

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

| Argument | Details |
| --- | --- |
| `project_root` | required. |
| `output_directory` | required. |
| `--architecture` | required · choices: `x86`, `x86_64`. |
| `--image-base` | type: `custom` · default: `0`. |
| `--max-bytes` | type: `int` · default: `256`. |
| `--max-attempts` | type: `int` · default: `4`. |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp llm batch-match`

```text
usage: x86decomp llm batch-match [-h] [--max-workers MAX_WORKERS]
                                 [--max-attempts MAX_ATTEMPTS] [--overwrite]
                                 profile compiler_profile jobs
                                 output_directory
```

| Argument | Details |
| --- | --- |
| `profile` | required. |
| `compiler_profile` | required. |
| `jobs` | required. |
| `output_directory` | required. |
| `--max-workers` | type: `int` · default: `1`. |
| `--max-attempts` | type: `int`. |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp llm cpp-generate`

```text
usage: x86decomp llm cpp-generate [-h] [--class-context CLASS_CONTEXT]
                                  [--report REPORT] [--overwrite]
                                  profile job output
```

| Argument | Details |
| --- | --- |
| `profile` | required. |
| `job` | required. |
| `output` | required. |
| `--class-context` | — |
| `--report` | — |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp llm generate`

```text
usage: x86decomp llm generate [-h] [--report REPORT] [--overwrite]
                              profile job output
```

| Argument | Details |
| --- | --- |
| `profile` | required. |
| `job` | required. |
| `output` | required. |
| `--report` | — |
| `--overwrite` | nargs: `0` · default: `False`. |

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

| Argument | Details |
| --- | --- |
| `function_packet` | required. |
| `output` | required. |
| `--architecture` | required · choices: `x86`, `x86_64`. |
| `--image-base` | type: `custom` · default: `0`. |
| `--function-name` | — |
| `--symbol` | — |
| `--max-attempts` | type: `int` · default: `4`. |
| `--inline` | nargs: `0` · default: `False`. |
| `--overwrite` | nargs: `0` · default: `False`. |

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

| Argument | Details |
| --- | --- |
| `image` | required. |
| `output` | required. |
| `--rva` | required · type: `custom`. |
| `--size` | required · type: `custom`. |
| `--architecture` | required · choices: `x86`, `x86_64`. |
| `--function-name` | required. |
| `--symbol` | — |
| `--image-base` | type: `custom` · default: `0`. |
| `--mnemonics` | — |
| `--max-attempts` | type: `int` · default: `4`. |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp llm match`

```text
usage: x86decomp llm match [-h] [--max-attempts MAX_ATTEMPTS] [--overwrite]
                           profile compiler_profile job output_directory
```

| Argument | Details |
| --- | --- |
| `profile` | required. |
| `compiler_profile` | required. |
| `job` | required. |
| `output_directory` | required. |
| `--max-attempts` | type: `int`. |
| `--overwrite` | nargs: `0` · default: `False`. |

### `x86decomp llm probe`

```text
usage: x86decomp llm probe [-h] profile
```

| Argument | Details |
| --- | --- |
| `profile` | required. |

### `x86decomp llm profile-create`

```text
usage: x86decomp llm profile-create [-h] --model MODEL [--base-url BASE_URL]
                                    [--id ID] [--api-key-env API_KEY_ENV]
                                    [--allow-remote]
                                    {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm}
                                    output
```

| Argument | Details |
| --- | --- |
| `provider` | required · choices: `llama.cpp`, `lm-studio`, `localai`, `ollama`, `openai-compatible`, `vllm`. |
| `output` | required. |
| `--model` | required. |
| `--base-url` | — |
| `--id` | — |
| `--api-key-env` | — |
| `--allow-remote` | nargs: `0` · default: `False`. |

### `x86decomp llm profile-validate`

```text
usage: x86decomp llm profile-validate [-h] profile
```

| Argument | Details |
| --- | --- |
| `profile` | required. |

### `x86decomp llm prompt`

```text
usage: x86decomp llm prompt [-h] job output
```

| Argument | Details |
| --- | --- |
| `job` | required. |
| `output` | required. |

### `x86decomp llm providers`

```text
usage: x86decomp llm providers [-h]
```

### `x86decomp llm verify`

```text
usage: x86decomp llm verify [-h] report
```

| Argument | Details |
| --- | --- |
| `report` | required. |


