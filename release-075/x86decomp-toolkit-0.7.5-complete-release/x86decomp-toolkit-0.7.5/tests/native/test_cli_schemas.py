import json
from pathlib import Path

from jsonschema import Draft202012Validator

from x86decomp.cli import _build_parser, main as toolkit_main
from x86decomp.native.cli import build_parser, main
from x86decomp.native.store import NativeStore

ROOT=Path(__file__).resolve().parents[2]


def _leaf_commands(parser):
    output=[]
    def walk(current,prefix=()):
        children=[]
        for action in current._actions:
            if action.__class__.__name__=='_SubParsersAction': children.extend(action.choices.items())
        if not children:
            if prefix: output.append(' '.join(prefix))
            return
        for name,child in children: walk(child,prefix+(name,))
    walk(parser); return output


def test_native_project_init_and_all_leaf_help(tmp_path:Path,capsys)->None:
    assert main(['--project',str(tmp_path),'project','init'])==0
    assert json.loads(capsys.readouterr().out)['native_schema_extension_version']==6
    parser=build_parser(); commands=_leaf_commands(parser); assert len(commands)==33
    for command in commands:
        try: parser.parse_args(command.split()+['--help'])
        except SystemExit as exc: assert exc.code==0
        capsys.readouterr()


def test_main_cli_exposes_native_capabilities(capsys)->None:
    choices=set(next(a for a in _build_parser()._actions if a.__class__.__name__=='_SubParsersAction').choices)
    assert {'commands', 'boundary', 'match', 'windows'} <= choices
    assert toolkit_main(['commands', '--owner', 'native'])==0
    payload = json.loads(capsys.readouterr().out)
    assert payload['release']=='0.7.5'
    assert payload['selected_route_count'] > 0
    assert {route['owner'] for route in payload['routes']} == {'native'}


def test_native_schemas_meta_validate()->None:
    schemas=sorted((ROOT/'schemas/native').glob('*.schema.json')); assert len(schemas)==12
    for path in schemas: Draft202012Validator.check_schema(json.loads(path.read_text()))


def test_native_store_keeps_all_prior_schema_layers(tmp_path:Path)->None:
    check=NativeStore(tmp_path).check()
    assert check['passed'] and check['schema_extension_version']==4 and check['reconstruction_schema_extension_version']==5 and check['native_schema_extension_version']==6
