---
title: Release Evidence
description: Current 0.7.5 tests, harness, source coverage, and documentation evidence.
---

# Release Evidence

These pages describe the final x86decomp-toolkit 0.7.5 package and its synchronized Material documentation site.

<div class="doc-card-grid">
<a class="doc-card" href="../verification/">
<strong>Verification</strong>
<span>223/223 distinct release tests and 191 PASS / 11 BLOCKED comprehensive-harness results.</span>
<small>Release gates</small>
</a>
<a class="doc-card" href="../source-coverage/">
<strong>Source coverage</strong>
<span>Manifest-backed coverage for 427 toolkit-root entries and 60 standalone test-suite entries.</span>
<small>487 verified entries</small>
</a>
<a class="doc-card" href="../local-llm/">
<strong>Local LLM workflow</strong>
<span>Local-model C proposals with compiler, COFF, relocation, and exact-byte acceptance gates.</span>
<small>Bounded trust</small>
</a>
<a class="doc-card" href="../changelog/">
<strong>Changelog</strong>
<span>Source-backed release notes for x86decomp-toolkit 0.7.5.</span>
<small>0.7.5</small>
</a>
</div>

## Evidence boundaries

- `PASS` means the declared harness check completed successfully.
- `BLOCKED` means an external runtime was unavailable; it is never silently converted into a pass or skip.
- Exact byte identity is limited to the declared compiler profile, symbol, relocation inputs, and contiguous target range.
- Test and documentation completeness do not prove target-specific decompilation success.
