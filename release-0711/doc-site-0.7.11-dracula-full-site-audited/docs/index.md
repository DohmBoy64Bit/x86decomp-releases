---
title: x86decomp 0.7.11 Documentation
description: Evidence-governed x86/x86-64 decompilation toolkit documentation.
---

# x86decomp 0.7.11 Documentation

This site is synchronized to the uploaded 0.7.11 second-audit fix release bundle. Source-derived pages were regenerated from the parser, schemas, manifests, Python AST, tests, and release evidence.

<div class="doc-stat-grid">
<div><strong>166</strong><span>toolkit root commands</span></div>
<div><strong>59</strong><span>canonical groups</span></div>
<div><strong>239</strong><span>canonical routes</span></div>
<div><strong>148</strong><span>Python source/test-suite modules</span></div>
<div><strong>97</strong><span>JSON schemas</span></div>
<div><strong>269</strong><span>test functions indexed</span></div>
</div>

## Start here

- [Getting started](getting-started.md)
- [Workflows](workflows.md)
- [Local LLM C generation](local-llm.md)
- [Complete command reference](commands/index.md)
- [Release verification](verification.md)
- [Source coverage](source-coverage.md)

## 0.7.11 release boundary

The active release is the 0.7.11 second-audit fix release. It fixes all nine confirmed second-audit findings and adds command-level regressions, pyflakes validation, shared binary-reader logic, and synchronized architecture/reference documentation.

The monolithic all-at-once pytest run is not claimed because it timed out in the sandbox; the published evidence records segmented/file-level tests and other completed gates.
