# Documentation audit

## Scope and factual checks

All 122 baseline Markdown files and all Python docstrings were completely ingested. Local Markdown targets were resolved; zero broken local targets were found. JSON companions parsed successfully. Version references were checked against release 0.7.11. Installation, verification, architecture, adapter, local-model, supported-scope, evidence, recovery, test-bundle, and security guides were reviewed against implementation and tests.

## Strengths

- README states purpose, authorization boundary, install commands, first-project flow, local-model acceptance boundary, assembly behavior, and verification entry points.
- Architecture and supported-scope documents distinguish static facts, proposals, and validated claims.
- Local-model documentation explains loopback defaults, secret indirection, redirects, and byte-match acceptance.
- Security and evidence documents communicate important trust boundaries.
- All 405 live argparse nodes contain help text.
- Module/class/function docstring presence is complete under the shipped gate.

## Verified weaknesses

1. **DOC-001:** 364/1,853 documented symbols use generic low-information forms; the quality gate checks only two obsolete exact phrases plus repeated first words.
2. **DOC-002:** explicit long-form coverage reaches 23/166 root commands and 8/239 canonical routes; examples cover 23 root commands and 7 routes.
3. **REL-001:** verification documentation tells users to run a sequence that rewrites sealed reports and then fails hash verification.
4. The command-reference Markdown is a count summary rather than a complete command manual.
5. The executable has no version-reporting option, reducing provenance usability (UX-001).

## Command-documentation matrix

`COMMAND_INVENTORY.csv` contains one row for each of 405 parser nodes, including summary/help, description presence, full argument metadata, documentation mention, example match, and safety flags. `CANONICAL_ROUTE_INVENTORY.csv` contains all 239 canonical routes. These are the exhaustive matrices; aggregate coverage is summarized in `COMMAND_SYSTEM_AUDIT.md`.

## New-user assessment

A new user can install, discover commands, initialize a project, and understand the evidence model. Advanced workflows require significant `--help` exploration or source reading because per-command examples, expected outputs, errors, and realistic use cases are not comprehensive. Documentation is therefore **usable but incomplete for the full advertised surface**.
