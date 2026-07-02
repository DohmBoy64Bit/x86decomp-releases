---
title: x86decomp.governance.campaigns
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-governance-campaigns.html
---

<a id="function-campaignengine-init"></a>
<a id="function-campaignengine-create"></a>
<a id="function-campaignengine-validate-budget"></a>
<a id="function-campaignengine-transition"></a>
<a id="function-campaignengine-start"></a>
<a id="function-campaignengine-pause"></a>
<a id="function-campaignengine-resume"></a>
<a id="function-campaignengine-stop"></a>
<a id="function-campaignengine-consume-budget"></a>
<a id="function-campaignengine-branch"></a>
<a id="function-campaignengine-get-branch"></a>
<a id="function-campaignengine-snapshot"></a>
<a id="function-campaignengine-decision"></a>
<a id="function-campaignengine-plan-next"></a>
<a id="function-campaignengine-get"></a>
<a id="function-campaignengine-list"></a>

Section: Source-derived feature and function reference

# x86decomp.governance.campaigns

No module docstring is declared in the v0.7.4 source.

Metadata: governance · current · 16 functions/methods

**Source:** `src/x86decomp/governance/campaigns.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `0c43e0289c80013abf35c01f68f0214d968d3be681395621632a24e5d09dfd2a`.

## Functions and methods

Metadata: internal · line 16

### CampaignEngine.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.__init__`

Metadata: public · line 20

### CampaignEngine.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, goal: str, *, budget: dict[str, Any] | None = None, policy: dict[str, Any] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.create`

Metadata: internal · line 41

### CampaignEngine._validate_budget

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_budget(value: dict[str, Any]) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine._validate_budget`

Metadata: public · line 52

### CampaignEngine.transition

No function or method docstring is declared in the v0.7.4 source.

```
def transition(self, campaign_id: str, new_state: str, *, reason: str | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.transition`

Metadata: public · line 70

### CampaignEngine.start

No function or method docstring is declared in the v0.7.4 source.

```
def start(self, campaign_id: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.start`

Metadata: public · line 73

### CampaignEngine.pause

No function or method docstring is declared in the v0.7.4 source.

```
def pause(self, campaign_id: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.pause`

Metadata: public · line 76

### CampaignEngine.resume

No function or method docstring is declared in the v0.7.4 source.

```
def resume(self, campaign_id: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.resume`

Metadata: public · line 79

### CampaignEngine.stop

No function or method docstring is declared in the v0.7.4 source.

```
def stop(self, campaign_id: str, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.stop`

Metadata: public · line 82

### CampaignEngine.consume_budget

No function or method docstring is declared in the v0.7.4 source.

```
def consume_budget(self, campaign_id: str, dimension: str, amount: int, *, actor: str = 'system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.consume_budget`

Metadata: public · line 106

### CampaignEngine.branch

No function or method docstring is declared in the v0.7.4 source.

```
def branch(self, campaign_id: str, name: str, *, parent_branch_id: str | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.branch`

Metadata: public · line 123

### CampaignEngine.get_branch

No function or method docstring is declared in the v0.7.4 source.

```
def get_branch(self, branch_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.get_branch`

Metadata: public · line 130

### CampaignEngine.snapshot

No function or method docstring is declared in the v0.7.4 source.

```
def snapshot(self, campaign_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.snapshot`

Metadata: internal · line 139

### CampaignEngine._decision

No function or method docstring is declared in the v0.7.4 source.

```
def _decision(row: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine._decision`

Metadata: public · line 144

### CampaignEngine.plan_next

No function or method docstring is declared in the v0.7.4 source.

```
def plan_next(self, campaign_id: str, *, actor: str = 'planner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.plan_next`

Metadata: public · line 176

### CampaignEngine.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, campaign_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.get`

Metadata: public · line 186

### CampaignEngine.list

No function or method docstring is declared in the v0.7.4 source.

```
def list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.list`
