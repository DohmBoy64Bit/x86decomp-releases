# LLM profile

`$id: https://x86decomp.local/schemas/local-llm/profile.schema.json` — schema version 1.

Validated against `schemas/local-llm/profile.schema.json`.

An LLM profile configures a local or OpenAI-compatible LLM provider for AI-assisted decompilation. Profiles define the connection protocol, model parameters, and TLS settings.

---

## Required fields

| Field | Type | Constraint |
|-------|------|------------|
| `schema_version` | `1` (const) | — |
| `id` | string | minLength 1, maxLength 256 |
| `provider` | enum | One of 6 presets |
| `protocol` | enum | `openai-chat` or `ollama-chat` |
| `base_url` | string (uri) | Pattern `^https?://` |
| `models_path` | string | Pattern `^/` — API path to list models |
| `chat_path` | string | Pattern `^/` — API path for chat completions |
| `structured_output` | enum | `openai-json-schema`, `ollama-json-schema`, or `none` |
| `model` | string | minLength 1 |
| `temperature` | number | 0.0 — 2.0 |
| `max_tokens` | integer | 1 — 1,000,000 |
| `timeout_seconds` | integer | 1 — 3,600 |
| `max_response_bytes` | integer | 1,024 — 67,108,864 |
| `verify_tls` | boolean | — |
| `allow_remote` | boolean | — |
| `api_key_env` | string or null | minLength 1 if set |
| `headers` | object (string→string) | — |

---

## `provider` presets (6 values)

| Value | Description |
|-------|-------------|
| `lm-studio` | LM Studio local server |
| `ollama` | Ollama local server |
| `llama.cpp` | llama.cpp server |
| `vllm` | vLLM inference server |
| `localai` | LocalAI server |
| `openai-compatible` | Generic OpenAI-compatible endpoint |

## `protocol`

| Value | Meaning |
|-------|---------|
| `openai-chat` | OpenAI chat completions API (`/v1/chat/completions`) |
| `ollama-chat` | Ollama chat API (`/api/chat`) |

## `structured_output`

| Value | Meaning |
|-------|---------|
| `openai-json-schema` | OpenAI JSON structured output mode |
| `ollama-json-schema` | Ollama JSON schema mode |
| `none` | No structured output enforcement |

---

## Provider-specific presets

### LM Studio

```json
{
  "schema_version": 1,
  "id": "lm-studio-qwen-coder",
  "provider": "lm-studio",
  "protocol": "openai-chat",
  "base_url": "http://127.0.0.1:1234/v1",
  "models_path": "/models",
  "chat_path": "/chat/completions",
  "structured_output": "openai-json-schema",
  "model": "qwen2.5-coder-7b-instruct",
  "temperature": 0.0,
  "max_tokens": 4096,
  "timeout_seconds": 180,
  "max_response_bytes": 2097152,
  "verify_tls": true,
  "allow_remote": false,
  "api_key_env": null,
  "headers": {}
}
```

### Ollama

```json
{
  "schema_version": 1,
  "id": "ollama-qwen-coder",
  "provider": "ollama",
  "protocol": "ollama-chat",
  "base_url": "http://127.0.0.1:11434",
  "models_path": "/api/tags",
  "chat_path": "/api/chat",
  "structured_output": "ollama-json-schema",
  "model": "qwen2.5-coder",
  "temperature": 0.0,
  "max_tokens": 4096,
  "timeout_seconds": 180,
  "max_response_bytes": 2097152,
  "verify_tls": true,
  "allow_remote": false,
  "api_key_env": null,
  "headers": {}
}
```

!!! tip
    Set `temperature` to `0.0` for deterministic source-code generation. Increase only when exploring multiple candidate approaches.

!!! warning
    `allow_remote` controls whether the profile accepts remote connections when the LLM adapter is running as a server. Set to `false` for local-only profiles. `verify_tls` should remain `true` in production; disable only for local development with self-signed certificates.

### OpenAI-compatible generic preset

For any provider with an OpenAI-compatible API:

```json
{
  "schema_version": 1,
  "id": "openai-gpt4",
  "provider": "openai-compatible",
  "protocol": "openai-chat",
  "base_url": "https://api.openai.com/v1",
  "models_path": "/models",
  "chat_path": "/chat/completions",
  "structured_output": "openai-json-schema",
  "model": "gpt-4",
  "temperature": 0.0,
  "max_tokens": 16384,
  "timeout_seconds": 300,
  "max_response_bytes": 4194304,
  "verify_tls": true,
  "allow_remote": true,
  "api_key_env": "OPENAI_API_KEY",
  "headers": {}
}
```
