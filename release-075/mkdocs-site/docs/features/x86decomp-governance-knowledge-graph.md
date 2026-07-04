---
title: x86decomp.governance.knowledge_graph
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.knowledge_graph`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/knowledge_graph.py`  
**SHA-256:** `8ab4ed3fe2315a0a44f7ac646a7759127283a436807ed80bc01e865c6eb0cc33`  
**Functions/methods:** 5

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-knowledgegraph-init"></a>

### `KnowledgeGraph.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def KnowledgeGraph.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.__init__`  
**Visibility:** internal  
**Source line:** 12

<a id="function-knowledgegraph-upsert-node"></a>

### `KnowledgeGraph.upsert_node`

No function or method docstring is declared in the 0.7.5 source.

```python
def KnowledgeGraph.upsert_node(self, node_id: str, kind: str, label: str, *, attributes: dict[str, Any] | None=None, actor: str='system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.upsert_node`  
**Visibility:** public  
**Source line:** 16

<a id="function-knowledgegraph-add-edge"></a>

### `KnowledgeGraph.add_edge`

No function or method docstring is declared in the 0.7.5 source.

```python
def KnowledgeGraph.add_edge(self, source_id: str, target_id: str, relation: str, *, attributes: dict[str, Any] | None=None, actor: str='system') -> str
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.add_edge`  
**Visibility:** public  
**Source line:** 30

<a id="function-knowledgegraph-get-node"></a>

### `KnowledgeGraph.get_node`

No function or method docstring is declared in the 0.7.5 source.

```python
def KnowledgeGraph.get_node(self, node_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.get_node`  
**Visibility:** public  
**Source line:** 50

<a id="function-knowledgegraph-impact"></a>

### `KnowledgeGraph.impact`

No function or method docstring is declared in the 0.7.5 source.

```python
def KnowledgeGraph.impact(self, node_id: str, *, direction: str='outbound', max_depth: int=8, relations: set[str] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.knowledge_graph:KnowledgeGraph.impact`  
**Visibility:** public  
**Source line:** 59
