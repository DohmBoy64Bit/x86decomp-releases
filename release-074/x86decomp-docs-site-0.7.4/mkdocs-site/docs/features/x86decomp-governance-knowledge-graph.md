---
title: x86decomp.governance.knowledge_graph
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-knowledge-graph.html
---

<a id="function-knowledgegraph-init"></a>
<a id="function-knowledgegraph-upsert-node"></a>
<a id="function-knowledgegraph-add-edge"></a>
<a id="function-knowledgegraph-get-node"></a>
<a id="function-knowledgegraph-impact"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.knowledge_graph

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 5 functions/methods

**Source:** `src/x86decomp/governance/knowledge_graph.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `8ab4ed3fe2315a0a44f7ac646a7759127283a436807ed80bc01e865c6eb0cc33`.

## Functions and methods

Metadata: internal · line 12

### KnowledgeGraph.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.__init__`

Metadata: public · line 16

### KnowledgeGraph.upsert_node

No function or method docstring is declared in the v0.7.4 source.

```
def upsert_node(self, node_id: str, kind: str, label: str, *, attributes: dict[str, Any] | None = None, actor: str = 'system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.upsert_node`

Metadata: public · line 30

### KnowledgeGraph.add_edge

No function or method docstring is declared in the v0.7.4 source.

```
def add_edge(self, source_id: str, target_id: str, relation: str, *, attributes: dict[str, Any] | None = None, actor: str = 'system') -> str
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.add_edge`

Metadata: public · line 50

### KnowledgeGraph.get_node

No function or method docstring is declared in the v0.7.4 source.

```
def get_node(self, node_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.get_node`

Metadata: public · line 59

### KnowledgeGraph.impact

No function or method docstring is declared in the v0.7.4 source.

```
def impact(self, node_id: str, *, direction: str = 'outbound', max_depth: int = 8, relations: set[str] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.impact`
