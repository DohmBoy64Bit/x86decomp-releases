# Per-file audit — src/x86decomp/mcp.py

## A. Identity
- Path: `src/x86decomp/mcp.py`
- SHA-256: `4a2239c91b1dec43b6b8f9424f5341b7d56985e07519024549546f06f98c2bdb`
- Size: 19730 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 462 lines)
MCP 2025-06-18 client (stdio + Streamable HTTP/SSE) and GhidraMCPGateway: read() passes through read tools; propose_mutation/commit_mutation implement a hash-approved, allowlisted mutation journal (mutations require an approval hash + explicit --allow-tool).

## C/H. Security
- StreamableHTTPMCPClient validates URL scheme is http/https. Mutations are gated: a tool must be in mutation_allowlist AND go through propose→approval-hash→commit, matching the evidence-governance/consent posture. is_probable_mutation heuristic separates read vs mutate.
- stdio client spawns a user-declared command array (no shell). Server exit/closed-stream handled with ExternalToolError.
- Residual: approval hash is an integrity/consent mechanism, not authN of the server itself; user-supplied URL can be any origin (intended). Informational.

## M. Verdict
Well-structured trust boundary. Final status: Audited — complete.