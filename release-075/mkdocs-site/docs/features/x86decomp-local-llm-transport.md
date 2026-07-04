---
title: x86decomp.local_llm.transport
description: Dependency-free HTTP transports for supported local-model servers.
---

# `x86decomp.local_llm.transport`

Dependency-free HTTP transports for supported local-model servers.

**Area:** Toolkit  
**Source:** `src/x86decomp/local_llm/transport.py`  
**SHA-256:** `65526331d46e71ae5625569b23e3312d9126d860ef1bd244135f21a47af25a3f`  
**Functions/methods:** 14

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-sameoriginredirecthandler-redirect-request"></a>

### `_SameOriginRedirectHandler.redirect_request`

No function or method docstring is declared in the 0.7.5 source.

```python
def _SameOriginRedirectHandler.redirect_request(self, req: Request, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> Request | None
```

**Catalog symbol:** `x86decomp.local_llm.transport:_SameOriginRedirectHandler.redirect_request`  
**Visibility:** public  
**Source line:** 28

<a id="function-endpoint"></a>

### `_endpoint`

No function or method docstring is declared in the 0.7.5 source.

```python
def _endpoint(profile: dict[str, Any], path: str) -> str
```

**Catalog symbol:** `x86decomp.local_llm.transport:_endpoint`  
**Visibility:** internal  
**Source line:** 38

<a id="function-opener"></a>

### `_opener`

No function or method docstring is declared in the 0.7.5 source.

```python
def _opener(profile: dict[str, Any]) -> Any
```

**Catalog symbol:** `x86decomp.local_llm.transport:_opener`  
**Visibility:** internal  
**Source line:** 42

<a id="function-headers"></a>

### `_headers`

No function or method docstring is declared in the 0.7.5 source.

```python
def _headers(profile: dict[str, Any]) -> dict[str, str]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_headers`  
**Visibility:** internal  
**Source line:** 50

<a id="function-read-json-response"></a>

### `_read_json_response`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_json_response(profile: dict[str, Any], request: Request) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_read_json_response`  
**Visibility:** internal  
**Source line:** 62

<a id="function-request-json"></a>

### `_request_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def _request_json(profile: dict[str, Any], *, method: str, path: str, body: dict[str, Any] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_request_json`  
**Visibility:** internal  
**Source line:** 85

<a id="function-model-ids"></a>

### `_model_ids`

No function or method docstring is declared in the 0.7.5 source.

```python
def _model_ids(profile: dict[str, Any], payload: dict[str, Any]) -> list[str]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_model_ids`  
**Visibility:** internal  
**Source line:** 102

<a id="function-ollama-model-matches"></a>

### `_ollama_model_matches`

No function or method docstring is declared in the 0.7.5 source.

```python
def _ollama_model_matches(requested: str, available: str) -> bool
```

**Catalog symbol:** `x86decomp.local_llm.transport:_ollama_model_matches`  
**Visibility:** internal  
**Source line:** 124

<a id="function-probe-profile"></a>

### `probe_profile`

Probe a provider's model-list endpoint without generating text.

```python
def probe_profile(profile: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.transport:probe_profile`  
**Visibility:** public  
**Source line:** 132

<a id="function-candidate-schema"></a>

### `_candidate_schema`

No function or method docstring is declared in the 0.7.5 source.

```python
def _candidate_schema() -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_candidate_schema`  
**Visibility:** internal  
**Source line:** 150

<a id="function-openai-body"></a>

### `_openai_body`

No function or method docstring is declared in the 0.7.5 source.

```python
def _openai_body(profile: dict[str, Any], messages: list[dict[str, str]], structured: bool) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_openai_body`  
**Visibility:** internal  
**Source line:** 164

<a id="function-ollama-body"></a>

### `_ollama_body`

No function or method docstring is declared in the 0.7.5 source.

```python
def _ollama_body(profile: dict[str, Any], messages: list[dict[str, str]], structured: bool) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.transport:_ollama_body`  
**Visibility:** internal  
**Source line:** 184

<a id="function-extract-content"></a>

### `_extract_content`

No function or method docstring is declared in the 0.7.5 source.

```python
def _extract_content(profile: dict[str, Any], payload: dict[str, Any]) -> str
```

**Catalog symbol:** `x86decomp.local_llm.transport:_extract_content`  
**Visibility:** internal  
**Source line:** 199

<a id="function-chat"></a>

### `chat`

Generate one bounded response, retrying once without structured mode when unsupported.

```python
def chat(profile: dict[str, Any], messages: list[dict[str, str]]) -> ModelResponse
```

**Catalog symbol:** `x86decomp.local_llm.transport:chat`  
**Visibility:** public  
**Source line:** 215
