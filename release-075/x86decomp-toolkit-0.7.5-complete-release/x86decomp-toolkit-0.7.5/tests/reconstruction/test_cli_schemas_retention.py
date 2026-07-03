from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator

from x86decomp.cli import _build_parser, main
from x86decomp.reconstruction.cli import _json, build_parser, main as reconstruction_main

ROOT=Path(__file__).resolve().parents[2]

def _leaf_commands(parser):
    result=[]
    def walk(p,prefix=()):
        actions=[a for a in p._actions if a.__class__.__name__=='_SubParsersAction']
        if not actions:
            result.append(' '.join(prefix)); return
        for action in actions:
            for name,child in action.choices.items(): walk(child,prefix+(name,))
    walk(parser); return sorted(x for x in result if x)


def test_reconstruction_json_argument_validation() -> None:
    assert _json(None,{'default':True})=={'default':True}
    assert _json('{"value":1}',{})=={'value':1}
    import pytest
    from x86decomp.contracts import ContractError
    with pytest.raises(ContractError): _json('{broken',{})

def test_reconstruction_cli_has_complete_project_scale_surface(tmp_path: Path,capsys) -> None:
    leaves=_leaf_commands(build_parser())
    for required in ('project init','module create','headers synthesize','build compare-modes','provenance source','source reconcile','abi shim','tests promote-counterexample','capsule reproduce','library externalize','security report','changeset merge'):
        assert required in leaves
    assert len(leaves)>=60
    assert reconstruction_main(['--project',str(tmp_path),'project','init'])==0
    payload=json.loads(capsys.readouterr().out); assert payload['reconstruction_schema_extension_version']==5 and payload['passed']



def test_every_reconstruction_leaf_command_parses_help(capsys) -> None:
    parser=build_parser()
    leaves=_leaf_commands(parser)
    assert len(leaves)==75
    for command in leaves:
        try:
            parser.parse_args(command.split()+['--help'])
        except SystemExit as exc:
            assert exc.code==0, command
    capsys.readouterr()

def test_main_cli_exposes_reconstruction_capabilities(capsys) -> None:
    parser = _build_parser()
    choices = set()
    for action in parser._actions:
        if action.__class__.__name__ == '_SubParsersAction':
            choices.update(action.choices)
    assert {'commands', 'module', 'source', 'build'} <= choices
    assert main(['commands', '--owner', 'reconstruction']) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload['release'] == '0.7.5'
    assert payload['selected_route_count'] > 0
    assert {route['owner'] for route in payload['routes']} == {'reconstruction'}


def test_all_reconstruction_schemas_are_meta_valid() -> None:
    schemas=sorted((ROOT/'schemas/reconstruction').glob('*.schema.json')); assert len(schemas)==12
    for path in schemas: Draft202012Validator.check_schema(json.loads(path.read_text()))


def test_governance_capabilities_are_in_the_unified_catalog(capsys) -> None:
    assert main(['commands', '--owner', 'governance']) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload['release'] == '0.7.5'
    assert payload['selected_route_count'] > 0
    assert {route['owner'] for route in payload['routes']} == {'governance'}
