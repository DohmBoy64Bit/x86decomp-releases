---
title: x86decomp llm
description: Exact parser-derived reference for x86decomp llm in 0.7.5.
---

# `x86decomp llm`

Canonical capability group with 8 routes. Shared group options are shown in every exact usage string.

## `x86decomp llm generate`

generate one uncompiled C proposal

### Usage

```text
x86decomp llm generate [-h] [--report REPORT] [--overwrite]
                              profile job output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required. No help text is declared; parser destination is `profile`. |
| `job` | required. No help text is declared; parser destination is `job`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--report` | declared. No help text is declared; parser destination is `report`. |
| `--overwrite` | default: `False` · nargs: `0`. No help text is declared; parser destination is `overwrite`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm match`

run bounded generation, compilation, relocation resolution, and exact byte matching

### Usage

```text
x86decomp llm match [-h] [--max-attempts MAX_ATTEMPTS] [--overwrite]
                           profile compiler_profile job output_directory
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required. No help text is declared; parser destination is `profile`. |
| `compiler_profile` | required. No help text is declared; parser destination is `compiler_profile`. |
| `job` | required. No help text is declared; parser destination is `job`. |
| `output_directory` | required. No help text is declared; parser destination is `output_directory`. |
| `--max-attempts` | type: `int`. No help text is declared; parser destination is `max_attempts`. |
| `--overwrite` | default: `False` · nargs: `0`. No help text is declared; parser destination is `overwrite`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm probe`

probe the provider model-list endpoint

### Usage

```text
x86decomp llm probe [-h] profile
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required. No help text is declared; parser destination is `profile`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm profile-create`

create a validated local-model provider profile

### Usage

```text
x86decomp llm profile-create [-h] --model MODEL [--base-url BASE_URL]
                                    [--id ID] [--api-key-env API_KEY_ENV]
                                    [--allow-remote]
                                    {llama.cpp,lm-studio,localai,ollama,openai-compatible,vllm}
                                    output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `provider` | required · choices: `llama.cpp`, `lm-studio`, `localai`, `ollama`, `openai-compatible`, `vllm`. No help text is declared; parser destination is `provider`. |
| `output` | required. No help text is declared; parser destination is `output`. |
| `--model` | required. No help text is declared; parser destination is `model`. |
| `--base-url` | declared. No help text is declared; parser destination is `base_url`. |
| `--id` | declared. No help text is declared; parser destination is `id`. |
| `--api-key-env` | declared. No help text is declared; parser destination is `api_key_env`. |
| `--allow-remote` | default: `False` · nargs: `0`. No help text is declared; parser destination is `allow_remote`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm profile-validate`

validate a local-model provider profile

### Usage

```text
x86decomp llm profile-validate [-h] profile
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `profile` | required. No help text is declared; parser destination is `profile`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm prompt`

materialize the deterministic prompt without contacting a model

### Usage

```text
x86decomp llm prompt [-h] job output
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `job` | required. No help text is declared; parser destination is `job`. |
| `output` | required. No help text is declared; parser destination is `output`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm providers`

list built-in local-model provider presets

### Usage

```text
x86decomp llm providers [-h]
```

No route-specific arguments are declared.

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
## `x86decomp llm verify`

verify a local-model byte-match report and accepted artifact hashes

### Usage

```text
x86decomp llm verify [-h] report
```

### Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `report` | required. No help text is declared; parser destination is `report`. |

### Source basis

| Parser owner | Source file and SHA-256 |
| --- | --- |
| `reconstruction` | `src/x86decomp/reconstruction/cli.py` · `b9d051f746f52cb85e01dd963c5acf455645fae0ba61bb6a5f1a9577e0db9ac7` |
