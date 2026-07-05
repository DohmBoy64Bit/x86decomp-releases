"""Provide test-suite.x86decomp_testkit.adapters.capabilities functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import json
import socket
from dataclasses import asdict, dataclass
from ipaddress import ip_address
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

from ..config import TestConfig
from ..models import AdapterSpec, ProbeResult


LOOPBACK_HOSTS = {"localhost", "127.0.0.1", "::1"}


@dataclass(frozen=True)
class CapabilityResult:
    """Store the validated fields for capability result records.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    capability_id: str
    satisfied: bool
    providers: tuple[str, ...] = ()
    diagnostics: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        """Convert dict.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return asdict(self)


def host_is_loopback(host: str | None) -> bool:
    """Implement host is loopback.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not host:
        return False
    lowered = host.strip("[]").lower()
    if lowered in LOOPBACK_HOSTS:
        return True
    try:
        return ip_address(lowered).is_loopback
    except ValueError:
        try:
            return any(ip_address(item[4][0]).is_loopback for item in socket.getaddrinfo(lowered, None))
        except OSError:
            return False


def endpoint_is_allowed(url: str, config: TestConfig) -> bool:
    """Implement endpoint is allowed.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False
    return config.allow_network or host_is_loopback(parsed.hostname)


def normalize_endpoint(value: str) -> str:
    """Normalize endpoint.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    url = value.strip().rstrip("/")
    if not url:
        raise ValueError("empty endpoint URL")
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "http://" + url
    return url.rstrip("/")


def probe_openai_compatible_endpoint(base_url: str, config: TestConfig, timeout: int = 5) -> tuple[bool, str | None, list[str]]:
    """Implement probe openai compatible endpoint.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    diagnostics: list[str] = []
    try:
        endpoint = normalize_endpoint(base_url)
    except ValueError as exc:
        return False, None, [str(exc)]
    if not endpoint_is_allowed(endpoint, config):
        return False, endpoint, ["endpoint is not loopback and allow_network is false"]
    url = endpoint + "/models" if endpoint.endswith("/v1") else endpoint + "/v1/models"
    try:
        request = Request(url, method="GET", headers={"Accept": "application/json"})
        with urlopen(request, timeout=timeout) as response:  # noqa: S310 - loopback-guarded above
            status = getattr(response, "status", 200)
            payload = response.read(min(65536, int(response.headers.get("Content-Length", "65536") or 65536)))
        if 200 <= int(status) < 300:
            try:
                json.loads(payload.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                diagnostics.append("/v1/models returned non-JSON payload")
            return True, endpoint, diagnostics
        return False, endpoint, [f"/v1/models returned HTTP {status}"]
    except HTTPError as exc:
        return False, endpoint, [f"/v1/models returned HTTP {exc.code}"]
    except (OSError, URLError, TimeoutError) as exc:
        return False, endpoint, [f"OpenAI-compatible endpoint probe failed: {exc}"]


def capabilities_from_adapters(catalog: dict[str, AdapterSpec], probe_results: list[ProbeResult]) -> list[CapabilityResult]:
    """Implement capabilities from adapters.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    by_capability: dict[str, list[str]] = {}
    diagnostics: dict[str, list[str]] = {}
    installed = {result.adapter_id: result for result in probe_results if result.installed}
    for adapter_id, result in installed.items():
        spec = catalog.get(adapter_id)
        declared = set(getattr(spec, "capabilities", ()) if spec else ()) | set(result.capabilities)
        for capability in declared:
            by_capability.setdefault(capability, []).append(adapter_id)
    for spec in catalog.values():
        for capability in getattr(spec, "capabilities", ()):
            diagnostics.setdefault(capability, [])
    for result in probe_results:
        spec = catalog.get(result.adapter_id)
        if not spec:
            continue
        for capability in getattr(spec, "capabilities", ()):
            if result.installed:
                continue
            diagnostics.setdefault(capability, []).append(f"{result.adapter_id}: unresolved")
    return [
        CapabilityResult(
            capability_id=capability,
            satisfied=bool(sorted(set(providers))),
            providers=tuple(sorted(set(providers))),
            diagnostics=tuple(sorted(set(diagnostics.get(capability, [])))) if not providers else (),
        )
        for capability, providers in sorted({**{k: [] for k in diagnostics}, **by_capability}.items())
    ]


def capability_map(results: list[CapabilityResult]) -> dict[str, CapabilityResult]:
    """Implement capability map.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return {result.capability_id: result for result in results}


def write_capability_report(results: list[CapabilityResult], path: Path) -> None:
    """Write capability report.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"schema_version": 1, "capabilities": [item.to_dict() for item in results]}
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
