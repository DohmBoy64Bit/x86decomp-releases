# x86decomp Project Examples docs patch

This overlay adds a complete **Project examples** page to the static x86decomp-toolkit 0.7.4 documentation site.

## Included

- `payload/project-examples.html` — the complete end-to-end hybrid project page.
- `payload/assets/project-examples.css` — responsive diagram and page styling.
- `apply_project_examples.py` — applies the page and site-wide integration edits.
- `source/project-examples.md` — editorial source note.
- `PATCH_MANIFEST.sha256` — hashes for every file in this patch bundle.

The new page contains:

- the complete target-pack-to-release workflow;
- a continuously buildable assembly fallback model;
- source maturation and candidate compilation;
- ABI validation;
- independent matching and functional lanes;
- `diff-function`, `dynamic-validate`, `symbolic-validate`, `integration-run`, `relink`, and `image-match` examples;
- matching and functional state records;
- a complete example final-state YAML record;
- two responsive inline SVG workflow diagrams;
- accessible text/ASCII diagram fallbacks;
- explicit bounded-claim and native-execution safety language.

## Apply it

Extract the existing `x86decomp-docs-site-0.7.4.zip`, then run:

```bash
python apply_project_examples.py /path/to/extracted/docs-site
```

The script:

1. creates a timestamped backup inside the site root;
2. installs the new page and stylesheet;
3. adds **Project examples** after **Workflows** in every HTML sidebar, including nested command, feature, and test pages;
4. adds a home-page card and a workflows-page cross-link;
5. appends a search entry when the generated search index has the expected JSON-compatible array format;
6. validates local links and fragments across the complete site;
7. writes `PROJECT_EXAMPLES_VERIFICATION.json` and `.md`;
8. refreshes `SHA256SUMS.txt`, `MANIFEST.sha256`, or `SITE_MANIFEST.sha256` when present.

## Idempotency

Running the script again does not duplicate the navigation entry, home card, workflow callout, or search entry. A fresh timestamped backup is still created unless `--no-backup` is supplied.

## Verification boundary

The overlay verifier checks documentation files, navigation, local links, fragments, visible placeholder markers, and discovered checksum manifests. It does not re-run the toolkit parser, release test suite, or external adapter probes. The sealed 0.7.4 release evidence remains a separate verification record.
