---
title: x86decomp.local_llm.transport
description: Module reference for x86decomp.local_llm.transport.
---

# `x86decomp.local_llm.transport`

- Area: `toolkit`
- Source path: `src/x86decomp/local_llm/transport.py`
- SHA-256: `040da7a261eb8b5c012cf2e3f7b303231666d5054ab449c34df11b69f5275990`
- Size: `10328` bytes
- Lines: `264`

## Module docstring

Dependency-free HTTP transports for supported local-model servers.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `ModelResponse` | 20 | Store validated model response fields used by toolkit reports and adapters. |
| class | `_SameOriginRedirectHandler` | 28 | Coordinate same origin redirect handler behavior for the current toolkit workflow. |
| function | `redirect_request` | 30 | Execute the redirect request operation for the current toolkit workflow. |
| function | `_endpoint` | 41 | Support endpoint processing for internal toolkit callers. |
| function | `_opener` | 46 | Support opener processing for internal toolkit callers. |
| function | `_headers` | 55 | Support headers processing for internal toolkit callers. |
| function | `_read_json_response` | 68 | Support read json response processing for internal toolkit callers. |
| function | `_request_json` | 92 | Support request json processing for internal toolkit callers. |
| function | `_model_ids` | 110 | Support model ids processing for internal toolkit callers. |
| function | `_ollama_model_matches` | 133 | Support ollama model matches processing for internal toolkit callers. |
| function | `probe_profile` | 142 | Probe a provider's model-list endpoint without generating text. |
| function | `_candidate_schema` | 160 | Support candidate schema processing for internal toolkit callers. |
| function | `_openai_body` | 175 | Support openai body processing for internal toolkit callers. |
| function | `_ollama_body` | 196 | Support ollama body processing for internal toolkit callers. |
| function | `_extract_content` | 212 | Support extract content processing for internal toolkit callers. |
| function | `chat` | 229 | Generate one bounded response, retrying once without structured mode when unsupported. |
