# Test-suite integration — 0.7.10

The harness runs as a sidecar to a toolkit source tree. Set `toolkit_root` to the extracted toolkit root. The verifier loads its packaged current feature catalog, inventories the target tree recursively, and rejects any difference.

External adapters are resolved from installed commands, configured paths, environment roots, or explicit consent-gated installation. Unavailable adapters are recorded as BLOCKED.

The comprehensive run executes built-in tests, exact command probes, schema checks, Java syntax checks, function-body coverage, package builds, clean installation, and report generation.
