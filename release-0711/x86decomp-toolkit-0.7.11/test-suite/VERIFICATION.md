# Verification record contract — 0.7.11

A final record must report exact counts for collected, passed, failed, errored, skipped, and blocked checks. It must include recursive catalog reconciliation, command and route audits, function-body coverage, line and branch coverage, adapter status, package results, archive results, exact root and sidecar source-manifest results, and checksums.

The release is rejected for any failure, error, skip, catalog drift, historical release reference, extra executable, upgrade artifact, placeholder, missing documentation mapping, or checksum mismatch.


## 0.7.11 adapter-capability note

The test harness now records protocol capabilities separately from product adapter identities. `lm-studio-http` can satisfy OpenAI-compatible local-LLM coverage through a loopback `/v1/models` probe without marking `ollama`, `llama-server`, `localai`, or `vllm` as installed.
