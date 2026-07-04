"""MCP 2025-06-18 client and evidence-gated Ghidra mutation journal."""

from __future__ import annotations

from . import __version__

import hashlib
import json
import subprocess
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ContractError, ExternalToolError
from .memory import ProjectMemory
from .util import canonical_json_bytes, load_json, utc_now, write_json

PROTOCOL_VERSION = "2025-06-18"


@dataclass(frozen=True)
class MCPTool:
    name: str
    description: str | None
    input_schema: dict[str, Any]


class StdioMCPClient:
    def __init__(self, command: list[str], *, cwd: Path | None = None):
        if not command:
            raise ContractError("MCP stdio command may not be empty")
        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            bufsize=1,
            cwd=None if cwd is None else cwd.resolve(),
        )
        self.request_id = 0
        self.initialized = False

    def _send(self, message: dict[str, Any]) -> None:
        if self.process.stdin is None:
            raise ExternalToolError("MCP server stdin is unavailable")
        self.process.stdin.write(json.dumps(message, separators=(",", ":")) + "\n")
        self.process.stdin.flush()

    def _request(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        if self.process.poll() is not None:
            stderr = self.process.stderr.read() if self.process.stderr else ""
            raise ExternalToolError(f"MCP server exited with {self.process.returncode}: {stderr}")
        self.request_id += 1
        request_id = self.request_id
        self._send({"jsonrpc": "2.0", "id": request_id, "method": method, "params": params or {}})
        if self.process.stdout is None:
            raise ExternalToolError("MCP server stdout is unavailable")
        while True:
            line = self.process.stdout.readline()
            if line == "":
                stderr = self.process.stderr.read() if self.process.stderr else ""
                raise ExternalToolError(f"MCP server closed stdout: {stderr}")
            try:
                response = json.loads(line)
            except json.JSONDecodeError:
                continue
            if response.get("id") != request_id:
                continue
            if "error" in response:
                raise ExternalToolError(f"MCP {method} error: {response['error']}")
            result = response.get("result")
            if not isinstance(result, dict):
                raise ExternalToolError(f"MCP {method} returned a non-object result")
            return result

    def initialize(self) -> dict[str, Any]:
        result = self._request(
            "initialize",
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {"name": "x86decomp-toolkit", "version": __version__},
            },
        )
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
        self.initialized = True
        return result

    def _ensure_initialized(self) -> None:
        if not self.initialized:
            self.initialize()

    def list_tools(self) -> list[MCPTool]:
        self._ensure_initialized()
        cursor: str | None = None
        tools: list[MCPTool] = []
        while True:
            params = {} if cursor is None else {"cursor": cursor}
            result = self._request("tools/list", params)
            raw = result.get("tools", [])
            if not isinstance(raw, list):
                raise ExternalToolError("MCP tools/list returned invalid tools")
            for item in raw:
                if not isinstance(item, dict) or not isinstance(item.get("name"), str):
                    raise ExternalToolError("MCP tool record is invalid")
                tools.append(MCPTool(item["name"], item.get("description"), item.get("inputSchema", {})))
            cursor = result.get("nextCursor")
            if not isinstance(cursor, str) or not cursor:
                break
        return tools

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        self._ensure_initialized()
        return self._request("tools/call", {"name": name, "arguments": arguments})

    def close(self) -> None:
        if self.process.poll() is None:
            if self.process.stdin is not None:
                self.process.stdin.close()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    self.process.kill()

    def __enter__(self) -> "StdioMCPClient":
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        self.close()


class StreamableHTTPMCPClient:
    def __init__(self, url: str, *, timeout: int = 60):
        if not url.startswith(("http://", "https://")):
            raise ContractError("MCP URL must use http or https")
        self.url = url
        self.timeout = timeout
        self.request_id = 0
        self.session_id: str | None = None
        self.initialized = False

    def _request(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        self.request_id += 1
        payload = json.dumps({"jsonrpc": "2.0", "id": self.request_id, "method": method, "params": params or {}}).encode("utf-8")
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": PROTOCOL_VERSION,
        }
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        request = urllib.request.Request(self.url, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                session = response.headers.get("Mcp-Session-Id")
                if session:
                    self.session_id = session
                body = response.read().decode("utf-8")
                content_type = response.headers.get_content_type()
        except Exception as exc:
            raise ExternalToolError(f"MCP HTTP request failed: {exc}") from exc
        if content_type == "text/event-stream":
            data_lines = [line[5:].strip() for line in body.splitlines() if line.startswith("data:")]
            if not data_lines:
                raise ExternalToolError("MCP SSE response contained no data event")
            value = json.loads(data_lines[-1])
        else:
            value = json.loads(body)
        if "error" in value:
            raise ExternalToolError(f"MCP {method} error: {value['error']}")
        result = value.get("result")
        if not isinstance(result, dict):
            raise ExternalToolError(f"MCP {method} returned a non-object result")
        return result

    def _notify(self, method: str) -> None:
        payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": {}}).encode("utf-8")
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream", "MCP-Protocol-Version": PROTOCOL_VERSION}
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        request = urllib.request.Request(self.url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(request, timeout=self.timeout):
            pass

    def initialize(self) -> dict[str, Any]:
        result = self._request("initialize", {"protocolVersion": PROTOCOL_VERSION, "capabilities": {}, "clientInfo": {"name": "x86decomp-toolkit", "version": __version__}})
        self._notify("notifications/initialized")
        self.initialized = True
        return result

    def _ensure_initialized(self) -> None:
        if not self.initialized:
            self.initialize()

    def list_tools(self) -> list[MCPTool]:
        self._ensure_initialized()
        result = self._request("tools/list")
        return [MCPTool(item["name"], item.get("description"), item.get("inputSchema", {})) for item in result.get("tools", [])]

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        self._ensure_initialized()
        return self._request("tools/call", {"name": name, "arguments": arguments})

    def close(self) -> None:
        """Streamable HTTP has no persistent local process to close."""
        return None


_DEFAULT_MUTATION_MARKERS = (
    "rename", "create", "delete", "set_", "update", "apply", "write", "save", "comment", "type", "structure", "enum", "function_signature", "prototype",
)


def is_probable_mutation(tool_name: str) -> bool:
    lowered = tool_name.lower()
    return any(marker in lowered for marker in _DEFAULT_MUTATION_MARKERS)


class GhidraMCPGateway:
    """Separates read calls from hash-approved mutation transactions."""

    def __init__(self, project_root: Path, client: StdioMCPClient | StreamableHTTPMCPClient, *, mutation_allowlist: set[str] | None = None):
        self.project_root = project_root.resolve()
        self.client = client
        self.mutation_allowlist = mutation_allowlist or set()
        self.transaction_root = self.project_root / "analysis" / "mcp-transactions"
        self.transaction_root.mkdir(parents=True, exist_ok=True)

    def read(self, tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if is_probable_mutation(tool):
            raise ContractError(f"probable mutation tool must use propose/commit: {tool}")
        result = self.client.call_tool(tool, arguments)
        ProjectMemory(self.project_root).append(actor="ghidra-mcp", category="mcp-read", summary=f"Called read-only MCP tool {tool}.", details={"tool": tool, "arguments": arguments})
        return result

    def propose_mutation(
        self,
        *,
        tool: str,
        arguments: dict[str, Any],
        rationale: str,
        evidence_ids: list[str],
    ) -> dict[str, Any]:
        if tool not in self.mutation_allowlist:
            raise ContractError(f"mutation tool is not allowlisted: {tool}")
        if not rationale.strip() or not evidence_ids:
            raise ContractError("mutation proposal requires rationale and evidence_ids")
        proposal = {
            "schema_version": 1,
            "created_at": utc_now(),
            "tool": tool,
            "arguments": arguments,
            "rationale": rationale,
            "evidence_ids": evidence_ids,
            "status": "proposed",
        }
        digest = hashlib.sha256(canonical_json_bytes(proposal)).hexdigest()
        proposal["approval_hash"] = digest
        write_json(self.transaction_root / f"{digest}.json", proposal)
        return proposal

    def commit_mutation(self, approval_hash: str) -> dict[str, Any]:
        path = self.transaction_root / f"{approval_hash}.json"
        if not path.is_file():
            raise ContractError("mutation proposal does not exist")
        proposal = load_json(path)
        unsigned = {key: value for key, value in proposal.items() if key not in ("approval_hash", "status", "committed_at", "result")}
        # status was part of the original signed proposal.
        unsigned["status"] = "proposed"
        actual = hashlib.sha256(canonical_json_bytes(unsigned)).hexdigest()
        if actual != approval_hash or proposal.get("approval_hash") != approval_hash:
            raise ContractError("mutation proposal hash does not verify")
        if proposal.get("status") != "proposed":
            raise ContractError("mutation proposal was already committed")
        result = self.client.call_tool(proposal["tool"], proposal["arguments"])
        proposal["status"] = "committed"
        proposal["committed_at"] = utc_now()
        proposal["result"] = result
        write_json(path, proposal)
        ProjectMemory(self.project_root).append(actor="ghidra-mcp", category="mcp-mutation", summary=f"Committed MCP mutation {proposal['tool']}.", details={"approval_hash": approval_hash, "tool": proposal["tool"], "evidence_ids": proposal["evidence_ids"]})
        return proposal
