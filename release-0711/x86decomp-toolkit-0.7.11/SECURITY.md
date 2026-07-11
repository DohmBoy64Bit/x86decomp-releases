# Security policy — 0.7.11

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

Send vulnerability reports privately to [cyborgplague1@gmail.com](mailto:cyborgplague1@gmail.com) before opening a public issue. Use a subject beginning with `x86decomp security:`. Include the affected command or module, release version, artifact identity or hash, reproduction steps, impact, and a minimal safe test case. Do not attach proprietary or unauthorized binaries.

The maintainer will acknowledge receipt through the same private channel and coordinate disclosure after a fix or documented mitigation is available.
