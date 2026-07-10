# Per-file audit — x86decomp-test.json

## A. Identity
- Path: `x86decomp-test.json`
- SHA-256: `0e8d5c302355cae3c618375f19cf815ddc4a894a686e1ccc7064df12b75b620c`
- Size: 4097 bytes | Type: text | Classification: configuration/data
- Batch: B01/B02 (root metadata & docs) | Reviewed: 2026-07-10 | Read completely: yes

## B. Function
Generated config for the `x86decomp-test` harness (schema_version 1): adapter paths, install_root, output_root, toolkit_root, python_executable — all absolute Windows paths on the owner's machine — plus policy flags (allow_host_execution false, allow_install true, allow_network true, strict false, coverage floors 70/50, timeout 900).

## C/H. Review
- This is a machine-local, machine-generated working file sitting in a release tree; its MANIFEST.sha256 entry FAILS (regenerated locally after packaging). Verified.
- `custom_environment.PATH` embeds the user's complete Windows PATH (~40 entries incl. local user directories and tool inventory). Not credentials, but environment/user-topology leakage if this tree is redistributed. Verified by direct read.
- allow_network: true + allow_install: true grant the harness install/network rights by default config — worth users' awareness; harness behavior audit in B09.

## L. Findings
- REPO-002 (Medium, Verified): machine-local generated config with full user PATH committed at release root; should be untracked (root path missing from .gitignore — REPO-004) and absent from release bundles.

## M. Verdict
Belongs in repo: NO (working byproduct). Priority: near-term. Final status: Audited — complete.