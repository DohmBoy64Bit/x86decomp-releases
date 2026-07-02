---
title: Migration Report
description: Static HTML to MkDocs migration notes for x86decomp 0.7.4.
---

# Migration Report

This MkDocs project was generated from the original static `x86decomp-docs-site-0.7.4` bundle.

## Coverage

- Original HTML pages converted to Markdown: 354
- Original non-HTML files copied under `original-site-files/`: 16
- Original search-index entries observed: 2183

## Intentional Structural Changes

- The original custom header, sidebar, theme toggle, page footer, and search overlay were removed from converted pages because MkDocs and the Dracula theme provide site chrome.
- Original local `.html` links were rewritten to `.md` source links so MkDocs can resolve and validate them during build.
- Original card grids, stat strips, metadata tags, and callout blocks were converted into Markdown-friendly lists, tables, paragraphs, or blockquotes.
- The original static search JavaScript was not used as runtime UI. MkDocs' built-in search plugin is enabled instead, while the original JavaScript asset is retained under `original-site-files/assets/`.

## Content Policy

No discretionary end-user documentation content was removed. The changes above are format and platform changes required for MkDocs.
