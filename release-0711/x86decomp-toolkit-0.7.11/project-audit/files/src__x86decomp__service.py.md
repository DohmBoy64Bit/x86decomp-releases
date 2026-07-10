# Per-file audit — src/x86decomp/service.py

## A. Identity
- Path: `src/x86decomp/service.py`
- SHA-256: `e27471e52dc3b5eca0e3b46369cacfde424fb42bcd446cb475c7989b0dcfa8ae`
- Size: 10304 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully, 251 lines)
Optional read-only FastAPI service: service_snapshot (opens orchestrator sqlite with mode=ro URI), GET /api endpoints for project/pipelines/reports/functions/workflow, DOM-safe HTML index, run_service (uvicorn, host default 127.0.0.1).

## C/H. Security
- Explicitly read-only: docstring + read-only sqlite URI + no write endpoints. CR-0710 fix present: index() builds DOM via createElement/textContent + JSON.stringify into <pre>.textContent — no innerHTML project-data injection (test_audit_fixes green, R-013). CSP header set (object-src none, base-uri none; script-src 'unsafe-inline' required for the inline script).
- /api/functions/{function_id:path}/workflow: function_id normalized then load_function_workflow(root, normalized) — path-safety depends on workflow.py using ensure_relative_path (cross-check B07). Flagged SEC-003 to verify traversal containment on that path.
- run_service default loopback; but `serve --host` allows 0.0.0.0 with NO authentication → read-only project data exposed on the network if a user widens the bind. SEC-004 (Low): document/warn, or refuse non-loopback without an explicit flag.

## L. Findings
- SEC-003 (verify workflow path containment, B07). SEC-004 (Low): unauthenticated bind widening via --host.

## M. Verdict
Quality high; read-only intent well enforced. Final status: Audited — complete.