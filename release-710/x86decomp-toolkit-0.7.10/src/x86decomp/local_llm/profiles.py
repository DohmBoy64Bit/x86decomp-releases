"""Provider profiles for bounded local-model inference.

Profiles deliberately contain only transport and inference settings. Secrets are
referenced by environment-variable name and are never persisted in generated
profiles or reports.
"""

from __future__ import annotations

import ipaddress
import socket
from copy import deepcopy
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from x86decomp.contracts import ContractError
from x86decomp.util import load_json, write_json

_PROVIDER_PRESETS: dict[str, dict[str, Any]] = {
    "lm-studio": {
        "protocol": "openai-chat",
        "base_url": "http://127.0.0.1:1234/v1",
        "models_path": "/models",
        "chat_path": "/chat/completions",
        "structured_output": "openai-json-schema",
    },
    "ollama": {
        "protocol": "ollama-chat",
        "base_url": "http://127.0.0.1:11434",
        "models_path": "/api/tags",
        "chat_path": "/api/chat",
        "structured_output": "ollama-json-schema",
    },
    "llama.cpp": {
        "protocol": "openai-chat",
        "base_url": "http://127.0.0.1:8080/v1",
        "models_path": "/models",
        "chat_path": "/chat/completions",
        "structured_output": "openai-json-schema",
    },
    "vllm": {
        "protocol": "openai-chat",
        "base_url": "http://127.0.0.1:8000/v1",
        "models_path": "/models",
        "chat_path": "/chat/completions",
        "structured_output": "openai-json-schema",
    },
    "localai": {
        "protocol": "openai-chat",
        "base_url": "http://127.0.0.1:8080/v1",
        "models_path": "/models",
        "chat_path": "/chat/completions",
        "structured_output": "openai-json-schema",
    },
    "openai-compatible": {
        "protocol": "openai-chat",
        "base_url": "http://127.0.0.1:8000/v1",
        "models_path": "/models",
        "chat_path": "/chat/completions",
        "structured_output": "openai-json-schema",
    },
}

_ALLOWED_PROTOCOLS = {"openai-chat", "ollama-chat"}
_ALLOWED_STRUCTURED_OUTPUT = {
    "openai-json-schema",
    "ollama-json-schema",
    "none",
}


def provider_catalog() -> dict[str, Any]:
    """Return the immutable built-in provider preset catalog."""
    return {
        "schema_version": 1,
        "providers": [
            {
                "id": provider_id,
                **deepcopy(values),
            }
            for provider_id, values in sorted(_PROVIDER_PRESETS.items())
        ],
        "security_default": "loopback_only",
        "secrets": "environment variables only",
    }


def _normalized_base_url(value: str) -> str:
    """Support normalized base url processing for internal toolkit callers."""
    if not isinstance(value, str) or not value.strip():
        raise ContractError("base_url must be a non-empty string")
    parsed = urlsplit(value.strip())
    if parsed.scheme not in {"http", "https"}:
        raise ContractError("base_url scheme must be http or https")
    if parsed.username is not None or parsed.password is not None:
        raise ContractError("base_url must not embed credentials")
    if not parsed.hostname:
        raise ContractError("base_url must include a hostname")
    if parsed.query or parsed.fragment:
        raise ContractError("base_url must not include a query or fragment")
    path = parsed.path.rstrip("/")
    return urlunsplit((parsed.scheme, parsed.netloc, path, "", ""))


def is_loopback_host(hostname: str) -> bool:
    """Return whether a hostname is an explicit local loopback identity."""
    normalized = hostname.strip().lower().rstrip(".")
    if normalized in {"localhost", "localhost.localdomain"}:
        return True
    try:
        return ipaddress.ip_address(normalized).is_loopback
    except ValueError:
        return False


def resolved_addresses_are_loopback(hostname: str) -> bool:
    """Resolve a host and require every result to be loopback.

    This is an additional diagnostic check. The default policy still requires an
    explicit loopback hostname, avoiding a DNS name whose answer may change
    between validation and request execution.
    """
    try:
        addresses = {
            record[4][0]
            for record in socket.getaddrinfo(hostname, None, type=socket.SOCK_STREAM)
        }
    except OSError:
        return False
    if not addresses:
        return False
    try:
        return all(ipaddress.ip_address(address).is_loopback for address in addresses)
    except ValueError:
        return False


def create_profile(
    provider: str,
    output: Path,
    *,
    model: str,
    base_url: str | None = None,
    profile_id: str | None = None,
    api_key_env: str | None = None,
    allow_remote: bool = False,
) -> dict[str, Any]:
    """Create and persist a validated provider profile."""
    if provider not in _PROVIDER_PRESETS:
        raise ContractError(f"unknown local-model provider: {provider}")
    if not isinstance(model, str) or not model.strip():
        raise ContractError("model must be a non-empty string")
    preset = deepcopy(_PROVIDER_PRESETS[provider])
    profile: dict[str, Any] = {
        "schema_version": 1,
        "id": profile_id or f"{provider}-{model.strip().replace('/', '-')}",
        "provider": provider,
        "protocol": preset["protocol"],
        "base_url": base_url or preset["base_url"],
        "models_path": preset["models_path"],
        "chat_path": preset["chat_path"],
        "structured_output": preset["structured_output"],
        "model": model.strip(),
        "temperature": 0.0,
        "max_tokens": 4096,
        "timeout_seconds": 180,
        "max_response_bytes": 2 * 1024 * 1024,
        "verify_tls": True,
        "allow_remote": bool(allow_remote),
        "api_key_env": api_key_env,
        "headers": {},
    }
    validated = validate_profile(profile)
    write_json(output, validated)
    return validated


def load_profile(path: Path) -> dict[str, Any]:
    """Load profile for the current toolkit workflow."""
    value = load_json(path)
    if not isinstance(value, dict):
        raise ContractError("local-model profile must be a JSON object")
    return validate_profile(value)


def validate_profile(raw: dict[str, Any]) -> dict[str, Any]:
    """Validate and normalize a local-model profile."""
    profile = deepcopy(raw)
    if profile.get("schema_version") != 1:
        raise ContractError("local-model profile schema_version must be 1")
    for key in ("id", "provider", "protocol", "base_url", "models_path", "chat_path", "model"):
        if not isinstance(profile.get(key), str) or not str(profile[key]).strip():
            raise ContractError(f"local-model profile {key} must be a non-empty string")
    if profile["provider"] not in _PROVIDER_PRESETS:
        raise ContractError(f"unsupported local-model provider: {profile['provider']}")
    if profile["protocol"] not in _ALLOWED_PROTOCOLS:
        raise ContractError(f"unsupported local-model protocol: {profile['protocol']}")
    profile["base_url"] = _normalized_base_url(profile["base_url"])
    parsed = urlsplit(profile["base_url"])
    allow_remote = profile.get("allow_remote", False)
    if not isinstance(allow_remote, bool):
        raise ContractError("allow_remote must be a boolean")
    if not allow_remote and not is_loopback_host(parsed.hostname or ""):
        raise ContractError(
            "remote local-model endpoint rejected; use an explicit loopback host or set allow_remote=true"
        )
    for key in ("models_path", "chat_path"):
        if not profile[key].startswith("/") or "?" in profile[key] or "#" in profile[key]:
            raise ContractError(f"{key} must be an absolute URL path without query or fragment")
    structured = profile.get("structured_output", "none")
    if structured not in _ALLOWED_STRUCTURED_OUTPUT:
        raise ContractError(f"unsupported structured_output mode: {structured}")
    profile["structured_output"] = structured
    temperature = profile.get("temperature", 0.0)
    if isinstance(temperature, bool) or not isinstance(temperature, (int, float)):
        raise ContractError("temperature must be numeric")
    if not 0.0 <= float(temperature) <= 2.0:
        raise ContractError("temperature must be between 0 and 2")
    profile["temperature"] = float(temperature)
    for key, minimum, maximum in (
        ("max_tokens", 1, 1_000_000),
        ("timeout_seconds", 1, 3600),
        ("max_response_bytes", 1024, 64 * 1024 * 1024),
    ):
        value = profile.get(key)
        if isinstance(value, bool) or not isinstance(value, int) or not minimum <= value <= maximum:
            raise ContractError(f"{key} must be an integer between {minimum} and {maximum}")
    if not isinstance(profile.get("verify_tls", True), bool):
        raise ContractError("verify_tls must be a boolean")
    api_key_env = profile.get("api_key_env")
    if api_key_env is not None and (not isinstance(api_key_env, str) or not api_key_env.strip()):
        raise ContractError("api_key_env must be null or a non-empty environment-variable name")
    headers = profile.get("headers", {})
    if not isinstance(headers, dict) or not all(
        isinstance(key, str) and isinstance(value, str) for key, value in headers.items()
    ):
        raise ContractError("headers must be a string-to-string object")
    forbidden = {key for key in headers if key.lower() in {"authorization", "proxy-authorization", "cookie"}}
    if forbidden:
        raise ContractError(
            "secret-bearing headers are not permitted in profiles; use api_key_env instead"
        )
    profile["headers"] = dict(headers)
    return profile


def public_profile(profile: dict[str, Any]) -> dict[str, Any]:
    """Return report-safe profile metadata without secret values."""
    return {
        key: deepcopy(value)
        for key, value in profile.items()
        if key not in {"headers"}
    } | {
        "headers": sorted(profile.get("headers", {}).keys()),
        "api_key_present": bool(profile.get("api_key_env")),
    }
