"""Verify the current toolkit behavior covered by `tests/test_mcp.py`."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from x86decomp.mcp import GhidraMCPGateway, StdioMCPClient


def _server(path: Path) -> None:
    """Support server processing for internal toolkit callers."""
    path.write_text(
        """import json, sys
for line in sys.stdin:
    request = json.loads(line)
    if 'id' not in request:
        continue
    method = request.get('method')
    if method == 'initialize':
        result = {'protocolVersion':'2025-06-18','capabilities':{'tools':{}},'serverInfo':{'name':'mock','version':'1'}}
    elif method == 'tools/list':
        result = {'tools':[{'name':'read_function','description':'read','inputSchema':{'type':'object'}},{'name':'rename_function','description':'write','inputSchema':{'type':'object'}}]}
    elif method == 'tools/call':
        params = request['params']
        result = {'content':[{'type':'text','text':json.dumps({'tool':params['name'],'arguments':params['arguments']})}]}
    else:
        result = {}
    sys.stdout.write(json.dumps({'jsonrpc':'2.0','id':request['id'],'result':result})+'\\n')
    sys.stdout.flush()
""",
        encoding="utf-8",
    )


def test_stdio_mcp_and_mutation_journal(tmp_path: Path) -> None:
    """Verify stdio mcp and mutation journal behavior."""
    server = tmp_path / "server.py"
    _server(server)
    project = tmp_path / "project"
    client = StdioMCPClient([sys.executable, str(server)])
    try:
        tools = client.list_tools()
        assert {tool.name for tool in tools} == {"read_function", "rename_function"}
        gateway = GhidraMCPGateway(project, client, mutation_allowlist={"rename_function"})
        read = gateway.read("read_function", {"address": "00401000"})
        assert "content" in read
        proposal = gateway.propose_mutation(
            tool="rename_function",
            arguments={"address": "00401000", "name": "CandidateName"},
            rationale="Evidence-backed candidate name",
            evidence_ids=["ev-1", "ev-2", "ev-3"],
        )
        committed = gateway.commit_mutation(proposal["approval_hash"])
        assert committed["status"] == "committed"
        assert (project / "analysis" / "mcp-transactions" / f"{proposal['approval_hash']}.json").is_file()
    finally:
        client.close()
