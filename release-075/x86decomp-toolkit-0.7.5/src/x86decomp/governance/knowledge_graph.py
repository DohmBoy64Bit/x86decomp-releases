from __future__ import annotations

import json
from collections import deque
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now, validate_id
from .store import GovernanceStore


class KnowledgeGraph:
    def __init__(self, store: GovernanceStore):
        self.store = store
        self.store.initialize()

    def upsert_node(self, node_id: str, kind: str, label: str, *, attributes: dict[str, Any] | None = None, actor: str = "system") -> dict[str, Any]:
        validate_id(node_id, field="node_id")
        if not kind or not label:
            raise ContractError("node kind and label are required")
        now = utc_now()
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_graph_nodes(node_id,kind,label,attributes_json,created_at,updated_at) VALUES(?,?,?,?,?,?) "
                "ON CONFLICT(node_id) DO UPDATE SET kind=excluded.kind,label=excluded.label,attributes_json=excluded.attributes_json,updated_at=excluded.updated_at",
                (node_id, kind, label, canonical_json(attributes or {}), now, now),
            )
            self.store.audit(actor, "graph.node.upsert", node_id, {"kind": kind, "label": label, "attributes": attributes or {}}, connection=connection)
        return self.get_node(node_id)

    def add_edge(self, source_id: str, target_id: str, relation: str, *, attributes: dict[str, Any] | None = None, actor: str = "system") -> str:
        if source_id == target_id and relation in {"depends_on", "contains"}:
            raise ContractError(f"self edge not allowed for relation {relation}")
        with self.store.connect() as connection:
            known = {row[0] for row in connection.execute("SELECT node_id FROM governance_graph_nodes WHERE node_id IN (?,?)", (source_id, target_id)).fetchall()}
        missing = {source_id, target_id} - known
        if missing:
            raise ContractError("unknown graph node(s): " + ", ".join(sorted(missing)))
        edge_id = random_id("edge")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_graph_edges(edge_id,source_id,target_id,relation,attributes_json,created_at) VALUES(?,?,?,?,?,?) "
                "ON CONFLICT(source_id,target_id,relation) DO UPDATE SET attributes_json=excluded.attributes_json",
                (edge_id, source_id, target_id, relation, canonical_json(attributes or {}), utc_now()),
            )
            row = connection.execute("SELECT edge_id FROM governance_graph_edges WHERE source_id=? AND target_id=? AND relation=?", (source_id, target_id, relation)).fetchone()
            actual_id = row[0]
            self.store.audit(actor, "graph.edge.upsert", actual_id, {"source_id": source_id, "target_id": target_id, "relation": relation, "attributes": attributes or {}}, connection=connection)
        return actual_id

    def get_node(self, node_id: str) -> dict[str, Any]:
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_graph_nodes WHERE node_id=?", (node_id,)).fetchone()
        if not row:
            raise KeyError(node_id)
        result = dict(row)
        result["attributes"] = json.loads(result.pop("attributes_json"))
        return result

    def impact(self, node_id: str, *, direction: str = "outbound", max_depth: int = 8, relations: set[str] | None = None) -> dict[str, Any]:
        if direction not in {"outbound", "inbound", "both"}:
            raise ContractError("direction must be outbound, inbound, or both")
        if not 0 <= max_depth <= 64:
            raise ContractError("max_depth must be in [0,64]")
        self.get_node(node_id)
        queue: deque[tuple[str, int]] = deque([(node_id, 0)])
        seen = {node_id}
        nodes: list[dict[str, Any]] = []
        edges: list[dict[str, Any]] = []
        with self.store.connect() as connection:
            while queue:
                current, depth = queue.popleft()
                nodes.append({"node": self.get_node(current), "depth": depth})
                if depth >= max_depth:
                    continue
                queries: list[tuple[str, tuple[Any, ...], str]] = []
                if direction in {"outbound", "both"}:
                    queries.append(("SELECT * FROM governance_graph_edges WHERE source_id=?", (current,), "target_id"))
                if direction in {"inbound", "both"}:
                    queries.append(("SELECT * FROM governance_graph_edges WHERE target_id=?", (current,), "source_id"))
                for query, args, next_field in queries:
                    for row in connection.execute(query, args).fetchall():
                        if relations and row["relation"] not in relations:
                            continue
                        edge = dict(row)
                        edge["attributes"] = json.loads(edge.pop("attributes_json"))
                        if not any(existing["edge_id"] == edge["edge_id"] for existing in edges):
                            edges.append(edge)
                        next_id = row[next_field]
                        if next_id not in seen:
                            seen.add(next_id)
                            queue.append((next_id, depth + 1))
        return {"root": node_id, "direction": direction, "max_depth": max_depth, "nodes": nodes, "edges": edges}
