# Command reference — 0.7.11

- Root commands: 166
- Canonical groups: 59
- Canonical routes: 239

The JSON companion file contains the synchronized root command and canonical route inventory.

## Plan-only reconstruction routes

The canonical reconstruction routes `candidate search`, `type propagate`, and `triage next` are plan-only helpers. They are documented as planning routes because their names can sound action-oriented, but their implementations emit reviewable JSON plans and do not silently edit source files, promote candidates, or mutate workflow state.
