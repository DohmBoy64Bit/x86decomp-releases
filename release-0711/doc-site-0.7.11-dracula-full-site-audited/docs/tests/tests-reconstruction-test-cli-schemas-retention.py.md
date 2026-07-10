---
title: tests/reconstruction/test_cli_schemas_retention.py
description: Test source page for tests/reconstruction/test_cli_schemas_retention.py.
---

# `tests/reconstruction/test_cli_schemas_retention.py`

- SHA-256: `c38bb38a3af81453e5a70293bf7a913ddd32c93bbfa21199f96e4d8a29e27ce2`
- Size: `3926` bytes
- Test functions: `6`

```python
"""Verify the current toolkit behavior covered by `tests/reconstruction/test_cli_schemas_retention.py`."""
from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator

from x86decomp.cli import _build_parser, main
from x86decomp.reconstruction.cli import _json, build_parser, main as reconstruction_main

ROOT=Path(__file__).resolve().parents[2]

def _leaf_commands(parser):
    """Support leaf commands processing for internal toolkit callers."""
    result=[]
    def walk(p,prefix=()):
        """Execute the walk operation for the current toolkit workflow."""
        actions=[a for a in p._actions if a.__class__.__name__=='_SubParsersAction']
        if not actions:
            result.append(' '.join(prefix)); return
        for action in actions:
            for name,child in action.choices.items(): walk(child,prefix+(name,))
    walk(parser); return sorted(x for x in result if x)


def test_reconstruction_json_argument_validation() -> None:
    """Verify reconstruction json argument validation behavior."""
    assert _json(None,{'default':True})=={'default':True}
    assert _json('{"value":1}',{})=={'value':1}
    import pytest
    from x86decomp.contracts import ContractError
    with pytest.raises(ContractError): _json('{broken',{})

def test_reconstruction_cli_has_complete_project_scale_surface(tmp_path: Path,capsys) -> None:
    """Verify reconstruction cli has complete project scale surface behavior."""
    leaves=_leaf_commands(build_parser())
    for required in ('project init','module create','headers synthesize','build compare-modes','provenance source','source reconcile','abi shim','tests promote-counterexample','capsule reproduce','library externalize','security report','changeset merge'):
        assert required in leaves
    assert len(leaves)>=60
    assert reconstruction_main(['--project',str(tmp_path),'project','init'])==0
    payload=json.loads(capsys.readouterr().out); assert payload['reconstruction_schema_extension_version']==5 and payload['passed']



def test_every_reconstruction_leaf_command_parses_help(capsys) -> None:
    """Verify every reconstruction leaf command parses help behavior."""
    parser=build_parser()
    leaves=_leaf_commands(parser)
    assert len(leaves)==133
    for command in leaves:
        try:
            parser.parse_args(command.split()+['--help'])
        except SystemExit as exc:
            assert exc.code==0, command
    capsys.readouterr()

def test_main_cli_exposes_reconstruction_capabilities(capsys) -> None:
    """Verify main cli exposes reconstruction capabilities behavior."""
    parser = _build_parser()
    choices = set()
    for action in parser._actions:
        if action.__class__.__name__ == '_SubParsersAction':
            choices.update(action.choices)
    assert {'commands', 'module', 'source', 'build'} <= choices
    assert main(['commands', '--owner', 'reconstruction']) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload['release'] == '0.7.11'
    assert payload['selected_route_count'] > 0
    assert {route['owner'] for route in payload['routes']} == {'reconstruction'}


def test_all_reconstruction_schemas_are_meta_valid() -> None:
    """Verify all reconstruction schemas are meta valid behavior."""
    schemas=sorted((ROOT/'schemas/reconstruction').glob('*.schema.json')); assert len(schemas)==12
    for path in schemas: Draft202012Validator.check_schema(json.loads(path.read_text()))


def test_governance_capabilities_are_in_the_unified_catalog(capsys) -> None:
    """Verify governance capabilities are in the unified catalog behavior."""
    assert main(['commands', '--owner', 'governance']) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload['release'] == '0.7.11'
    assert payload['selected_route_count'] > 0
    assert {route['owner'] for route in payload['routes']} == {'governance'}
```
