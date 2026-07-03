---
title: x86decomp.governance.campaigns
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.governance.campaigns`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/governance/campaigns.py`  
**SHA-256:** `0c43e0289c80013abf35c01f68f0214d968d3be681395621632a24e5d09dfd2a`  
**Functions/methods:** 16

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-campaignengine-init"></a>

### `CampaignEngine.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.__init__(self, store: GovernanceStore)
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.__init__`  
**Visibility:** internal  
**Source line:** 16

<a id="function-campaignengine-create"></a>

### `CampaignEngine.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.create(self, goal: str, *, budget: dict[str, Any] | None=None, policy: dict[str, Any] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.create`  
**Visibility:** public  
**Source line:** 20

<a id="function-campaignengine-validate-budget"></a>

### `CampaignEngine._validate_budget`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine._validate_budget(value: dict[str, Any]) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine._validate_budget`  
**Visibility:** internal  
**Source line:** 41

<a id="function-campaignengine-transition"></a>

### `CampaignEngine.transition`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.transition(self, campaign_id: str, new_state: str, *, reason: str | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.transition`  
**Visibility:** public  
**Source line:** 52

<a id="function-campaignengine-start"></a>

### `CampaignEngine.start`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.start(self, campaign_id: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.start`  
**Visibility:** public  
**Source line:** 70

<a id="function-campaignengine-pause"></a>

### `CampaignEngine.pause`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.pause(self, campaign_id: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.pause`  
**Visibility:** public  
**Source line:** 73

<a id="function-campaignengine-resume"></a>

### `CampaignEngine.resume`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.resume(self, campaign_id: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.resume`  
**Visibility:** public  
**Source line:** 76

<a id="function-campaignengine-stop"></a>

### `CampaignEngine.stop`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.stop(self, campaign_id: str, *, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.stop`  
**Visibility:** public  
**Source line:** 79

<a id="function-campaignengine-consume-budget"></a>

### `CampaignEngine.consume_budget`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.consume_budget(self, campaign_id: str, dimension: str, amount: int, *, actor: str='system') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.consume_budget`  
**Visibility:** public  
**Source line:** 82

<a id="function-campaignengine-branch"></a>

### `CampaignEngine.branch`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.branch(self, campaign_id: str, name: str, *, parent_branch_id: str | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.branch`  
**Visibility:** public  
**Source line:** 106

<a id="function-campaignengine-get-branch"></a>

### `CampaignEngine.get_branch`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.get_branch(self, branch_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.get_branch`  
**Visibility:** public  
**Source line:** 123

<a id="function-campaignengine-snapshot"></a>

### `CampaignEngine.snapshot`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.snapshot(self, campaign_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.snapshot`  
**Visibility:** public  
**Source line:** 130

<a id="function-campaignengine-decision"></a>

### `CampaignEngine._decision`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine._decision(row: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine._decision`  
**Visibility:** internal  
**Source line:** 139

<a id="function-campaignengine-plan-next"></a>

### `CampaignEngine.plan_next`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.plan_next(self, campaign_id: str, *, actor: str='planner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.plan_next`  
**Visibility:** public  
**Source line:** 144

<a id="function-campaignengine-get"></a>

### `CampaignEngine.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.get(self, campaign_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.get`  
**Visibility:** public  
**Source line:** 176

<a id="function-campaignengine-list"></a>

### `CampaignEngine.list`

No function or method docstring is declared in the 0.7.5 source.

```python
def CampaignEngine.list(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.governance.campaigns:CampaignEngine.list`  
**Visibility:** public  
**Source line:** 186
