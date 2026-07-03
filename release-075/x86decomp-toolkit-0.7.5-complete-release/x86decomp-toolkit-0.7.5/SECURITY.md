# Security policy — 0.7.5

x86decomp processes untrusted binary artifacts. Static analysis is the default. Dynamic or native execution is permitted only after explicit authorization and must use an appropriate bounded environment.

## Controls

- Validate paths before extraction or materialization.
- Reject archive traversal, unsafe links, and output paths outside declared roots.
- Use argument arrays rather than shell interpolation.
- Bound subprocess time, output, memory, and instruction counts where supported.
- Hash important inputs and outputs and preserve provenance.
- Never treat downloaded tools or artifacts as trusted solely because installation succeeded.
- Keep adapter detection and installation explicit in logs.
- Report unavailable security integrations as BLOCKED.
- Do not store secrets in project manifests, reports, examples, or release bundles.

## Reporting

Security findings should include the affected command or module, artifact identity, reproduction steps, impact, and a minimal safe test case. Do not attach proprietary or unauthorized binaries.
