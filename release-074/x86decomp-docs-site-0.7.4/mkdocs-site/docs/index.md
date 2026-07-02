---
title: x86decomp 0.7.4 Documentation
description: End-user documentation for installing, running, and verifying x86decomp-toolkit
  0.7.4.
---

# x86decomp 0.7.4 Documentation

Use this site to install the toolkit, create projects, run workflows, and verify release evidence. The reference pages remain source-derived, but the main path through the docs is organized around what an end user is trying to do.

<div class="doc-hero-metrics">
<div><strong>145</strong><span>command choices</span></div>
<div><strong>285</strong><span>runnable paths</span></div>
<div><strong>137</strong><span>Python modules</span></div>
<div><strong>93</strong><span>JSON schemas</span></div>
</div>

## Start Here

<div class="doc-card-grid">
<a class="doc-card" href="getting-started/">
<strong>Install and verify</strong>
<span>Set up the 0.7.4 toolkit, initialize a project, and run the verifier.</span>
<small>Start here</small>
</a>
<a class="doc-card" href="workflows/">
<strong>Choose a workflow</strong>
<span>Follow task-oriented paths for analysis, reconstruction, evidence, assembly, and release checks.</span>
<small>Guides</small>
</a>
<a class="doc-card" href="project-examples/">
<strong>Use project examples</strong>
<span>Walk through matching, functional, hybrid, and support workflows with bounded claims.</span>
<small>Examples</small>
</a>
<a class="doc-card" href="commands/">
<strong>Find a command</strong>
<span>Browse exact command syntax, arguments, examples, and source basis.</span>
<small>Reference</small>
</a>
<a class="doc-card" href="schemas/">
<strong>Check schemas</strong>
<span>Inspect every JSON schema contract shipped with the release.</span>
<small>Reference</small>
</a>
<a class="doc-card" href="verification/">
<strong>Review release evidence</strong>
<span>See the sealed verification result, source coverage, and current release boundary.</span>
<small>Evidence</small>
</a>
</div>

## Scope

x86decomp-toolkit is an evidence-governed x86 and x86-64 decompilation toolkit. The release exposes the `x86decomp` toolkit executable and the `x86decomp-test` verification executable.

> Analyze only binaries and systems you are authorized to inspect. Native execution and integration scenarios require appropriate isolation and explicit consent.
