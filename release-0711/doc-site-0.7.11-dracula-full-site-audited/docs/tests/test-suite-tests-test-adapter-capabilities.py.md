---
title: test-suite/tests/test_adapter_capabilities.py
description: Test source page for test-suite/tests/test_adapter_capabilities.py.
---

# `test-suite/tests/test_adapter_capabilities.py`

- SHA-256: `47dde51aa511486350597ec6a786e4be9ed9bc229b02e9cd8d12baff0874f133`
- Size: `4413` bytes
- Test functions: `3`

```python
"""Provide test-suite.tests.test_adapter_capabilities functionality for the x86decomp-toolkit 0.7.11 release.

This module-level documentation was added during the complete 0.7.11 code audit.
"""
from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from x86decomp_testkit.adapters.catalog import adapter_catalog
from x86decomp_testkit.adapters.capabilities import capabilities_from_adapters, capability_map, endpoint_is_allowed, host_is_loopback
from x86decomp_testkit.adapters.detection import detect_adapter
from x86decomp_testkit.config import TestConfig
from x86decomp_testkit.models import ProbeResult


class _ModelsHandler(BaseHTTPRequestHandler):
    """Implement the _ModelsHandler class using its declared base class contract.
    
    Attributes, invariants, and helper methods are defined by the class body.
    """
    def do_GET(self) -> None:
        """Implement do g e t.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        if self.path != "/v1/models":
            self.send_response(404)
            self.end_headers()
            return
        payload = json.dumps({"object": "list", "data": [{"id": "local-model"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args: object) -> None:
        """Implement log message.
        
        Parameters and return values follow the signature and runtime validation in the body.
        """
        return


def _config(tmp_path: Path) -> TestConfig:
    """Implement config.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return TestConfig(toolkit_root=tmp_path, output_root=tmp_path / "out", interactive=False, strict=False)


def test_lm_studio_http_satisfies_openai_capability_without_product_aliasing(tmp_path: Path) -> None:
    """Verify lm studio http satisfies openai capability without product aliasing.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    server = HTTPServer(("127.0.0.1", 0), _ModelsHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        config = _config(tmp_path)
        catalog = adapter_catalog()
        config.adapter_paths["lm-studio-http"] = f"http://127.0.0.1:{server.server_port}/v1"
        result = detect_adapter(catalog["lm-studio-http"], config)
        assert result.installed
        assert "openai-compatible-chat" in result.capabilities
        assert "local-loopback-llm" in result.capabilities
        product_results = [
            ProbeResult("ollama", False),
            ProbeResult("llama-server", False),
            ProbeResult("localai", False),
            ProbeResult("vllm", False),
            result,
        ]
        caps = capability_map(capabilities_from_adapters(catalog, product_results))
        assert caps["openai-compatible-chat"].satisfied
        assert "lm-studio-http" in caps["openai-compatible-chat"].providers
        unresolved_products = {"ollama", "llama-server", "localai", "vllm"}
        by_id = {item.adapter_id: item for item in product_results}
        assert not any(by_id[item].installed for item in unresolved_products)
    finally:
        server.shutdown()
        thread.join(timeout=5)


def test_non_loopback_http_endpoint_requires_network_opt_in(tmp_path: Path) -> None:
    """Verify non loopback http endpoint requires network opt in.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    config = _config(tmp_path)
    assert not endpoint_is_allowed("http://198.51.100.7:1234/v1", config)
    config.allow_network = True
    assert endpoint_is_allowed("http://198.51.100.7:1234/v1", config)


def test_loopback_host_classifier_is_strict() -> None:
    """Verify loopback host classifier is strict.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    assert host_is_loopback("127.0.0.1")
    assert host_is_loopback("localhost")
    assert not host_is_loopback("192.0.2.1")
```
