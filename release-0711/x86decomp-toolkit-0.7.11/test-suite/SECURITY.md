# Test-suite security model — 0.7.11

The harness treats archives, binaries, configured paths, downloaded tools, and subprocess output as untrusted.

- Archive extraction rejects traversal and unsafe links.
- Process execution uses argument arrays and bounded timeouts.
- Tool installation requires explicit policy and records hashes and origins where available.
- Native execution tests are consent-gated.
- Logs avoid embedding secrets and preserve enough evidence for review.
- Missing security tools are BLOCKED, not silently ignored.
- Release checks inspect wheel, source distribution, source ZIP, and final bundle contents.
