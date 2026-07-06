"""Dependency-free HTTP transports for supported local-model servers."""

from __future__ import annotations

import json
import os
import ssl
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

from x86decomp.contracts import ContractError

from .profiles import public_profile


@dataclass(frozen=True)
class ModelResponse:
    """Store validated model response fields used by toolkit reports and adapters."""
    content: str
    raw: dict[str, Any]
    structured_output_requested: bool
    structured_output_fallback: bool


class _SameOriginRedirectHandler(HTTPRedirectHandler):
    """Coordinate same origin redirect handler behavior for the current toolkit workflow."""
    def redirect_request(self, req: Request, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> Request | None:
        """Execute the redirect request operation for the current toolkit workflow."""
        old = urlsplit(req.full_url)
        new = urlsplit(newurl)
        old_port = old.port or (443 if old.scheme == "https" else 80)
        new_port = new.port or (443 if new.scheme == "https" else 80)
        if (old.scheme, old.hostname, old_port) != (new.scheme, new.hostname, new_port):
            raise ContractError("local-model redirect crossed origin and was rejected")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _endpoint(profile: dict[str, Any], path: str) -> str:
    """Support endpoint processing for internal toolkit callers."""
    return urljoin(profile["base_url"].rstrip("/") + "/", path.lstrip("/"))


def _opener(profile: dict[str, Any]) -> Any:
    """Support opener processing for internal toolkit callers."""
    context = ssl.create_default_context()
    if not profile.get("verify_tls", True):
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    return build_opener(_SameOriginRedirectHandler(), HTTPSHandler(context=context))


def _headers(profile: dict[str, Any]) -> dict[str, str]:
    """Support headers processing for internal toolkit callers."""
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    headers.update(profile.get("headers", {}))
    api_key_env = profile.get("api_key_env")
    if api_key_env:
        value = os.environ.get(api_key_env)
        if not value:
            raise ContractError(f"required API key environment variable is unset: {api_key_env}")
        headers["Authorization"] = f"Bearer {value}"
    return headers


def _read_json_response(profile: dict[str, Any], request: Request) -> dict[str, Any]:
    """Support read json response processing for internal toolkit callers."""
    maximum = int(profile["max_response_bytes"])
    try:
        with _opener(profile).open(request, timeout=int(profile["timeout_seconds"])) as response:
            length = response.headers.get("Content-Length")
            if length is not None and int(length) > maximum:
                raise ContractError("local-model response exceeded max_response_bytes")
            payload = response.read(maximum + 1)
    except HTTPError:
        raise
    except (URLError, TimeoutError, OSError) as exc:
        raise ContractError(f"local-model request failed: {exc}") from exc
    if len(payload) > maximum:
        raise ContractError("local-model response exceeded max_response_bytes")
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContractError("local-model response was not valid UTF-8 JSON") from exc
    if not isinstance(value, dict):
        raise ContractError("local-model response must be a JSON object")
    return value


def _request_json(
    profile: dict[str, Any],
    *,
    method: str,
    path: str,
    body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Support request json processing for internal toolkit callers."""
    encoded = None if body is None else json.dumps(body, separators=(",", ":")).encode("utf-8")
    request = Request(
        _endpoint(profile, path),
        data=encoded,
        method=method,
        headers=_headers(profile),
    )
    return _read_json_response(profile, request)


def _model_ids(profile: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    """Support model ids processing for internal toolkit callers."""
    if profile["protocol"] == "ollama-chat":
        models = payload.get("models", [])
        if not isinstance(models, list):
            raise ContractError("Ollama model-list response lacks models array")
        result = []
        for item in models:
            if isinstance(item, dict):
                value = item.get("name") or item.get("model")
                if isinstance(value, str):
                    result.append(value)
        return sorted(set(result))
    data = payload.get("data", [])
    if not isinstance(data, list):
        raise ContractError("OpenAI-compatible model-list response lacks data array")
    result = []
    for item in data:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            result.append(item["id"])
    return sorted(set(result))


def _ollama_model_matches(requested: str, available: str) -> bool:
    """Support ollama model matches processing for internal toolkit callers."""
    if requested == available:
        return True
    if ":" not in requested and available == f"{requested}:latest":
        return True
    return False


def probe_profile(profile: dict[str, Any]) -> dict[str, Any]:
    """Probe a provider's model-list endpoint without generating text."""
    payload = _request_json(profile, method="GET", path=profile["models_path"])
    model_ids = _model_ids(profile, payload)
    requested = profile["model"]
    if profile["protocol"] == "ollama-chat":
        model_available = any(_ollama_model_matches(requested, item) for item in model_ids)
    else:
        model_available = requested in model_ids
    return {
        "schema_version": 1,
        "profile": public_profile(profile),
        "reachable": True,
        "model_available": model_available,
        "models": model_ids,
    }


def _candidate_schema() -> dict[str, Any]:
    """Support candidate schema processing for internal toolkit callers."""
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "status": {"type": "string", "enum": ["proposed", "blocked"]},
            "c_source": {"type": "string"},
            "assumptions": {"type": "array", "items": {"type": "string"}},
            "rationale": {"type": "string"},
        },
        "required": ["status", "c_source", "assumptions", "rationale"],
    }


def _openai_body(profile: dict[str, Any], messages: list[dict[str, str]], structured: bool) -> dict[str, Any]:
    """Support openai body processing for internal toolkit callers."""
    body: dict[str, Any] = {
        "model": profile["model"],
        "messages": messages,
        "temperature": profile["temperature"],
        "max_tokens": profile["max_tokens"],
        "stream": False,
    }
    if structured:
        body["response_format"] = {
            "type": "json_schema",
            "json_schema": {
                "name": "x86decomp_c_candidate",
                "strict": True,
                "schema": _candidate_schema(),
            },
        }
    return body


def _ollama_body(profile: dict[str, Any], messages: list[dict[str, str]], structured: bool) -> dict[str, Any]:
    """Support ollama body processing for internal toolkit callers."""
    body: dict[str, Any] = {
        "model": profile["model"],
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": profile["temperature"],
            "num_predict": profile["max_tokens"],
        },
    }
    if structured:
        body["format"] = _candidate_schema()
    return body


def _extract_content(profile: dict[str, Any], payload: dict[str, Any]) -> str:
    """Support extract content processing for internal toolkit callers."""
    if profile["protocol"] == "ollama-chat":
        message = payload.get("message")
        if not isinstance(message, dict) or not isinstance(message.get("content"), str):
            raise ContractError("Ollama chat response lacks message.content")
        return message["content"]
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        raise ContractError("OpenAI-compatible chat response lacks choices")
    first = choices[0]
    message = first.get("message") if isinstance(first, dict) else None
    if not isinstance(message, dict) or not isinstance(message.get("content"), str):
        raise ContractError("OpenAI-compatible chat response lacks choices[0].message.content")
    return message["content"]


def chat(profile: dict[str, Any], messages: list[dict[str, str]]) -> ModelResponse:
    """Generate one bounded response, retrying once without structured mode when unsupported."""
    structured = profile.get("structured_output") != "none"
    if profile["protocol"] == "ollama-chat":
        body_factory = _ollama_body
    else:
        body_factory = _openai_body
    fallback = False
    try:
        payload = _request_json(
            profile,
            method="POST",
            path=profile["chat_path"],
            body=body_factory(profile, messages, structured),
        )
    except HTTPError as exc:
        if not structured or exc.code not in {400, 404, 415, 422}:
            try:
                detail = exc.read(4096).decode("utf-8", errors="replace")
            except Exception:
                detail = ""
            raise ContractError(f"local-model server returned HTTP {exc.code}: {detail}") from exc
        fallback = True
        payload = _request_json(
            profile,
            method="POST",
            path=profile["chat_path"],
            body=body_factory(profile, messages, False),
        )
    return ModelResponse(
        content=_extract_content(profile, payload),
        raw=payload,
        structured_output_requested=structured,
        structured_output_fallback=fallback,
    )
