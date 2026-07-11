"""Campaign lifecycle control, budget accounting, branching, and next-action planning."""
from __future__ import annotations

import json
from typing import Any

from x86decomp.contracts import ContractError, canonical_json, random_id, utc_now
from .store import GovernanceStore

CAMPAIGN_STATES = {"created", "running", "paused", "blocked", "completed", "stopped"}
GOALS = {"recover_function", "recover_module", "behavioral_equivalence", "byte_identical", "types_and_symbols"}


class CampaignEngine:
    """Persistent, deterministic campaign control and next-action planning."""

    def __init__(self, store: GovernanceStore):
        """Initialize CampaignEngine with `store`."""
        self.store = store
        self.store.initialize()

    def create(self, goal: str, *, budget: dict[str, Any] | None = None, policy: dict[str, Any] | None = None, actor: str = "analyst") -> dict[str, Any]:
        """Create a campaign in the ``created`` state with a ``main`` branch and audit entry.

        Args:
            goal: Campaign goal; must be one of :data:`GOALS`.
            budget: Optional budget overrides merged onto the defaults; see :meth:`_validate_budget`.
            policy: Optional opaque policy dictionary stored with the campaign.
            actor: Identity recorded in the audit log for the creation.

        Returns:
            The newly created campaign record.

        Raises:
            ContractError: If ``goal`` is not a supported goal, or the budget is invalid.
        """
        if goal not in GOALS:
            raise ContractError(f"unsupported campaign goal: {goal}")
        campaign_id = random_id("camp")
        branch_id = random_id("branch")
        now = utc_now()
        budget = self._validate_budget(budget or {})
        policy = policy or {}
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_campaigns(campaign_id,goal,status,project_root,budget_json,used_json,policy_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                (campaign_id, goal, "created", str(self.store.project_root), canonical_json(budget), canonical_json({k: 0 for k in budget}), canonical_json(policy), now, now),
            )
            connection.execute(
                "INSERT INTO governance_campaign_branches(branch_id,campaign_id,name,status,created_at) VALUES(?,?,?,?,?)",
                (branch_id, campaign_id, "main", "active", now),
            )
            self.store.audit(actor, "campaign.create", campaign_id, {"goal": goal, "budget": budget, "policy": policy, "main_branch_id": branch_id}, connection=connection)
        return self.get(campaign_id)

    @staticmethod
    def _validate_budget(value: dict[str, Any]) -> dict[str, int]:
        """Validate and normalize a budget mapping against the known dimensions.

        Args:
            value: Caller-supplied budget overrides keyed by dimension name.

        Returns:
            A budget dictionary with defaults applied for any omitted dimension.

        Raises:
            ContractError: If a key is not a known budget dimension, or a value is not a
                non-negative integer.
        """
        defaults = {"actions": 1000, "compile_seconds": 3600, "dynamic_cases": 100000, "symbolic_seconds": 3600}
        result = dict(defaults)
        for key, raw in value.items():
            if key not in defaults:
                raise ContractError(f"unknown budget dimension: {key}")
            if not isinstance(raw, int) or raw < 0:
                raise ContractError(f"budget {key} must be a non-negative integer")
            result[key] = raw
        return result

    def transition(self, campaign_id: str, new_state: str, *, reason: str | None = None, actor: str = "analyst") -> dict[str, Any]:
        """Move a campaign to a new lifecycle state, enforcing legal transitions.

        Args:
            campaign_id: Identifier of the campaign to transition.
            new_state: Target state; must be one of :data:`CAMPAIGN_STATES`.
            reason: Optional reason, stored only when transitioning to ``blocked``.
            actor: Identity recorded in the audit log for the transition.

        Returns:
            The updated campaign record.

        Raises:
            ContractError: If ``new_state`` is invalid or the transition is not allowed
                from the current state.
            KeyError: If the campaign does not exist.
        """
        if new_state not in CAMPAIGN_STATES:
            raise ContractError(f"invalid campaign state: {new_state}")
        current = self.get(campaign_id)
        allowed = {
            "created": {"running", "stopped"}, "running": {"paused", "blocked", "completed", "stopped"},
            "paused": {"running", "stopped"}, "blocked": {"running", "stopped"}, "completed": set(), "stopped": set(),
        }
        if new_state != current["status"] and new_state not in allowed[current["status"]]:
            raise ContractError(f"invalid campaign transition {current['status']} -> {new_state}")
        with self.store.transaction() as connection:
            connection.execute(
                "UPDATE governance_campaigns SET status=?,blocked_reason=?,updated_at=? WHERE campaign_id=?",
                (new_state, reason if new_state == "blocked" else None, utc_now(), campaign_id),
            )
            self.store.audit(actor, "campaign.transition", campaign_id, {"old_state": current["status"], "new_state": new_state, "reason": reason}, connection=connection)
        return self.get(campaign_id)

    def start(self, campaign_id: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Transition the campaign to the ``running`` state.

        Args:
            campaign_id: Identifier of the campaign to start.
            actor: Identity recorded in the audit log.

        Returns:
            The updated campaign record.
        """
        return self.transition(campaign_id, "running", actor=actor)

    def pause(self, campaign_id: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Transition the campaign to the ``paused`` state.

        Args:
            campaign_id: Identifier of the campaign to pause.
            actor: Identity recorded in the audit log.

        Returns:
            The updated campaign record.
        """
        return self.transition(campaign_id, "paused", actor=actor)

    def resume(self, campaign_id: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Resume a paused campaign by transitioning it back to ``running``.

        Args:
            campaign_id: Identifier of the campaign to resume.
            actor: Identity recorded in the audit log.

        Returns:
            The updated campaign record.
        """
        return self.transition(campaign_id, "running", actor=actor)

    def stop(self, campaign_id: str, *, actor: str = "analyst") -> dict[str, Any]:
        """Transition the campaign to the terminal ``stopped`` state.

        Args:
            campaign_id: Identifier of the campaign to stop.
            actor: Identity recorded in the audit log.

        Returns:
            The updated campaign record.
        """
        return self.transition(campaign_id, "stopped", actor=actor)

    def consume_budget(self, campaign_id: str, dimension: str, amount: int, *, actor: str = "system") -> dict[str, Any]:
        """Charge a budget dimension, blocking the campaign when the limit is exceeded.

        Args:
            campaign_id: Identifier of the campaign whose budget is charged.
            dimension: Budget dimension to debit.
            amount: Non-negative amount to consume.
            actor: Identity recorded in the audit log.

        Returns:
            The updated campaign record.

        Raises:
            ContractError: If ``amount`` is negative, the dimension is unknown, or the
                charge would exceed the limit (in which case the campaign is blocked).
            KeyError: If the campaign does not exist.
        """
        if amount < 0:
            raise ContractError("budget consumption must be non-negative")
        exhausted = False
        with self.store.transaction() as connection:
            row = connection.execute("SELECT budget_json,used_json,status FROM governance_campaigns WHERE campaign_id=?", (campaign_id,)).fetchone()
            if not row:
                raise KeyError(campaign_id)
            budget, used = json.loads(row["budget_json"]), json.loads(row["used_json"])
            if dimension not in budget:
                raise ContractError(f"unknown budget dimension: {dimension}")
            proposed = int(used.get(dimension, 0)) + amount
            if proposed > int(budget[dimension]):
                exhausted = True
                connection.execute("UPDATE governance_campaigns SET status='blocked',blocked_reason=?,updated_at=? WHERE campaign_id=?", (f"budget exhausted: {dimension}", utc_now(), campaign_id))
                self.store.audit(actor, "campaign.budget.exhausted", campaign_id, {"dimension": dimension, "requested": amount, "used": used.get(dimension, 0), "limit": budget[dimension]}, connection=connection)
            else:
                used[dimension] = proposed
                connection.execute("UPDATE governance_campaigns SET used_json=?,updated_at=? WHERE campaign_id=?", (canonical_json(used), utc_now(), campaign_id))
                self.store.audit(actor, "campaign.budget.consume", campaign_id, {"dimension": dimension, "amount": amount, "used": proposed, "limit": budget[dimension]}, connection=connection)
        if exhausted:
            raise ContractError(f"campaign budget exhausted: {dimension}")
        return self.get(campaign_id)

    def branch(self, campaign_id: str, name: str, *, parent_branch_id: str | None = None, actor: str = "analyst") -> dict[str, Any]:
        """Create a named branch under a campaign, optionally rooted at a parent branch.

        Args:
            campaign_id: Identifier of the owning campaign.
            name: Non-empty, path-safe branch name.
            parent_branch_id: Optional parent branch, which must belong to the campaign.
            actor: Identity recorded in the audit log.

        Returns:
            The newly created branch record.

        Raises:
            ContractError: If the name is empty or not path-safe, or the parent branch
                does not belong to the campaign.
            KeyError: If the campaign does not exist.
        """
        if not name or any(ch in name for ch in "\\/\x00"):
            raise ContractError("branch name must be non-empty and path-safe")
        self.get(campaign_id)
        branch_id = random_id("branch")
        with self.store.transaction() as connection:
            if parent_branch_id:
                parent = connection.execute("SELECT campaign_id FROM governance_campaign_branches WHERE branch_id=?", (parent_branch_id,)).fetchone()
                if not parent or parent[0] != campaign_id:
                    raise ContractError("parent branch does not belong to campaign")
            connection.execute(
                "INSERT INTO governance_campaign_branches(branch_id,campaign_id,parent_branch_id,name,status,created_at) VALUES(?,?,?,?,?,?)",
                (branch_id, campaign_id, parent_branch_id, name, "active", utc_now()),
            )
            self.store.audit(actor, "campaign.branch.create", branch_id, {"campaign_id": campaign_id, "name": name, "parent_branch_id": parent_branch_id}, connection=connection)
        return self.get_branch(branch_id)

    def get_branch(self, branch_id: str) -> dict[str, Any]:
        """Return a campaign branch record by its identifier.

        Args:
            branch_id: Identifier of the branch to fetch.

        Returns:
            The branch record.

        Raises:
            KeyError: If no branch with the given identifier exists.
        """
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_campaign_branches WHERE branch_id=?", (branch_id,)).fetchone()
        if not row:
            raise KeyError(branch_id)
        return dict(row)

    def snapshot(self, campaign_id: str) -> dict[str, Any]:
        """Return a campaign record enriched with its branches, decisions, and audit tip.

        Args:
            campaign_id: Identifier of the campaign to snapshot.

        Returns:
            The campaign record with ``branches``, ``decisions``, and ``audit_tip`` keys added.

        Raises:
            KeyError: If the campaign does not exist.
        """
        campaign = self.get(campaign_id)
        with self.store.connect() as connection:
            campaign["branches"] = [dict(r) for r in connection.execute("SELECT * FROM governance_campaign_branches WHERE campaign_id=? ORDER BY created_at", (campaign_id,)).fetchall()]
            campaign["decisions"] = [self._decision(r) for r in connection.execute("SELECT * FROM governance_planner_decisions WHERE campaign_id=? ORDER BY created_at", (campaign_id,)).fetchall()]
        campaign["audit_tip"] = self.store.verify_audit_chain()["tip_hash"]
        return campaign

    @staticmethod
    def _decision(row: Any) -> dict[str, Any]:
        """Convert a planner decision row into a dictionary with a decoded rationale.

        Args:
            row: Raw planner decision row from the database.

        Returns:
            A dictionary with the JSON ``rationale`` field decoded in place.
        """
        result = dict(row)
        result["rationale"] = json.loads(result.pop("rationale_json"))
        return result

    def plan_next(self, campaign_id: str, *, actor: str = "planner") -> dict[str, Any]:
        """Select and record the next campaign action using a deterministic priority policy.

        The planner inspects open reviews, contradicted and scheduled hypotheses, recorded
        counterexamples, and active candidates, choosing the highest-priority actionable item
        and falling back to unknown inventory when nothing is queued. Selecting an action
        charges one unit of the ``actions`` budget.

        Args:
            campaign_id: Identifier of the running campaign to plan for.
            actor: Identity recorded in the audit log.

        Returns:
            A dictionary describing the chosen decision, its subject, and rationale.

        Raises:
            ContractError: If the campaign is not in the ``running`` state, or the
                ``actions`` budget is exhausted.
            KeyError: If the campaign does not exist.
        """
        campaign = self.get(campaign_id)
        if campaign["status"] != "running":
            raise ContractError("campaign must be running before planning")
        with self.store.connect() as connection:
            unresolved_reviews = connection.execute("SELECT review_id,subject_id,priority FROM governance_review_items WHERE status IN ('open','assigned','needs_evidence') ORDER BY priority DESC,created_at LIMIT 1").fetchone()
            contradictory = connection.execute("SELECT hypothesis_id FROM governance_hypotheses WHERE state='contradicted' ORDER BY updated_at LIMIT 1").fetchone()
            testing = connection.execute("SELECT hypothesis_id FROM governance_hypotheses WHERE state IN ('scheduled','testing') ORDER BY updated_at LIMIT 1").fetchone()
            counterexample = connection.execute("SELECT counterexample_id FROM governance_counterexamples WHERE state='recorded' ORDER BY size_bytes DESC,created_at LIMIT 1").fetchone()
            candidate = connection.execute("SELECT candidate_id FROM governance_candidates WHERE state='active' ORDER BY updated_at LIMIT 1").fetchone()
        if unresolved_reviews and int(unresolved_reviews["priority"]) >= 80:
            action, subject, rationale = "review", unresolved_reviews["review_id"], {"reason": "highest-priority analyst review", "priority": unresolved_reviews["priority"]}
        elif contradictory:
            action, subject, rationale = "investigate_contradiction", contradictory[0], {"reason": "contradiction blocks acceptance"}
        elif counterexample:
            action, subject, rationale = "minimize_counterexample", counterexample[0], {"reason": "small counterexamples localize semantic divergence"}
        elif testing:
            action, subject, rationale = "run_experiment", testing[0], {"reason": "scheduled hypothesis requires evidence"}
        elif candidate:
            action, subject, rationale = "evaluate_candidate", candidate[0], {"reason": "active candidate has no higher-priority blocker"}
        else:
            action, subject, rationale = "inventory_unknowns", None, {"reason": "no actionable queued evidence; discover next bounded unknown"}
        self.consume_budget(campaign_id, "actions", 1, actor=actor)
        decision_id = random_id("plan")
        with self.store.transaction() as connection:
            connection.execute(
                "INSERT INTO governance_planner_decisions(decision_id,campaign_id,action_kind,subject_id,rationale_json,created_at) VALUES(?,?,?,?,?,?)",
                (decision_id, campaign_id, action, subject, canonical_json(rationale), utc_now()),
            )
            self.store.audit(actor, "campaign.plan", decision_id, {"campaign_id": campaign_id, "action": action, "subject_id": subject, "rationale": rationale}, connection=connection)
        return {"decision_id": decision_id, "campaign_id": campaign_id, "action": action, "subject_id": subject, "rationale": rationale}

    def get(self, campaign_id: str) -> dict[str, Any]:
        """Return a campaign record with its JSON budget, usage, and policy decoded.

        Args:
            campaign_id: Identifier of the campaign to fetch.

        Returns:
            The campaign record with ``budget``, ``used``, and ``policy`` keys decoded.

        Raises:
            KeyError: If the campaign does not exist.
        """
        with self.store.connect() as connection:
            row = connection.execute("SELECT * FROM governance_campaigns WHERE campaign_id=?", (campaign_id,)).fetchone()
        if not row:
            raise KeyError(campaign_id)
        result = dict(row)
        for name in ("budget_json", "used_json", "policy_json"):
            result[name[:-5]] = json.loads(result.pop(name))
        return result

    def list(self) -> list[dict[str, Any]]:
        """Return all campaign records ordered by creation time.

        Returns:
            A list of campaign records, each as returned by :meth:`get`.
        """
        with self.store.connect() as connection:
            ids = [r[0] for r in connection.execute("SELECT campaign_id FROM governance_campaigns ORDER BY created_at").fetchall()]
        return [self.get(item) for item in ids]
