# x86decomp 0.7.4 Project Examples Suite docs patch

This drop-in static-site overlay replaces the earlier single hybrid page with a source-audited suite:

- 11 detailed workflow examples
- one Project Examples landing page
- one human-readable source-audit page
- responsive inline SVG workflow diagrams with text fallbacks
- exact v0.7.4 command forms, bounded claims, and implementation caveats

The suite distinguishes the two actual `DecompilationMode` values (`matching` and `functional`) from the `preferred_mode: both` composition commonly described as hybrid. It also documents important v0.7.4 boundaries such as candidate-length patching and the release-gate/public-workflow schema mismatch.

## Install

PowerShell:

```powershell
python .\apply_project_examples_suite.py "C:\path\to\x86decomp-docs-site-0.7.4"
```

PowerShell does not use a standalone backslash for line continuation. Put the command on one line, or use a backtick.

The installer creates a timestamped backup by default. Use `--no-backup` only when you intentionally do not want one.

## Verify the audited source

Run these from the extracted patch directory against the extracted v0.7.4 source tree:

```powershell
python .\verify_against_v074_source.py "C:\path\to\x86decomp-toolkit-0.7.4"
python .\verify_command_surface.py "C:\path\to\x86decomp-toolkit-0.7.4"
python .\verify_patch_content.py
```

The source verifier checks the detected release, 50 whole-file SHA-256 values, 95 exact source anchors, and every declared line range. The command verifier imports the real v0.7.4 parser and parses all 163 documented command lines. The content verifier checks all 11 pages, diagrams, bounded-claim sections, critical caveat disclosures, search entries, source rows, and placeholder policy.

## Installed content

- `project-examples.html` — suite landing page
- `project-examples/*.html` — eleven detailed examples plus source audit
- `assets/project-examples.css` — responsive diagrams, cards, steps, and tables
- `PROJECT_EXAMPLES_SOURCE_AUDIT.json` — exact source evidence copied into the site
- `PROJECT_EXAMPLES_VERIFICATION.json/.md` — generated after installation

The installer replaces prior Project Examples search entries and page payloads, keeps one sidebar entry, updates the home/workflows links, validates local links and fragments, and refreshes any detected site checksum manifest.

## Verification records included with the patch

- `SOURCE_VERIFICATION.json`
- `COMMAND_SURFACE_VERIFICATION.json`
- `CONTENT_VERIFICATION.json`
- `IMPLEMENTATION_PROBES.json`
- `TARGETED_TEST_VERIFICATION.json`
- `PATCH_VERIFICATION.json` and `PATCH_VERIFICATION.md`

These records verify the documentation patch and its source basis. They do not assert that a user target has a particular compiler, ABI, function size, safe execution environment, passing validator result, or successful release gate.
