# Per-file audit — src/x86decomp/local_llm/transport.py

## A. Identity
- Path: `src/x86decomp/local_llm/transport.py`
- SHA-256: `ec489443f7fec07b465af050c6877c5d3f199c00e505460f341cbb6000fdd2ec`
- Size: 14631 bytes | Type: text | Classification: first-party source
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function (read fully via targeted reads, 421-region)
Dependency-free HTTP transport for local model servers. _SameOriginRedirectHandler rejects cross-origin redirects (scheme/host/effective-port compared); build_opener with TLS; API key strictly from os.environ[api_key_env] (ContractError if unset); urljoin base_url+path.

## C/H. Security — strong (matches README/SECURITY claims)
- SSRF hardening: same-origin redirect enforcement prevents redirect-based pivot; secrets via env var only (never stored/logged); loopback-oriented by profile. This precisely implements the README's 'endpoints loopback-only by default, secrets via env vars, redirects cannot cross origins' claim — Verified in code.
- Residual: base_url itself is user-supplied; nothing pins it to loopback (a user CAN point at a remote origin) — by design (README says 'by default'). SEC-Informational only.

## M. Verdict
Security posture excellent. Final status: Audited — complete.