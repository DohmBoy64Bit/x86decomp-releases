"""Unified canonical CLI surface that merges the governance, reconstruction, native,
and assembly command groups and routes each command to its owning subsystem."""
from __future__ import annotations

import argparse
import subprocess
from collections import defaultdict
from typing import Any

from x86decomp.cli_utils import run_cli
from x86decomp.governance.cli import build_parser as build_governance_parser
from x86decomp.governance.cli import dispatch as dispatch_governance
from x86decomp.contracts import ContractError
from x86decomp.reconstruction.cli import build_parser as build_reconstruction_parser
from x86decomp.reconstruction.cli import dispatch as dispatch_reconstruction
from x86decomp.native.cli import build_parser as build_native_parser
from x86decomp.native.cli import dispatch as dispatch_native
from x86decomp.assembly.cli import build_parser as build_assembly_parser
from x86decomp.assembly.cli import dispatch as dispatch_assembly

_OWNER_ORDER = ("governance", "reconstruction", "native", "assembly")
_BUILDERS = {
    "governance": build_governance_parser,
    "reconstruction": build_reconstruction_parser,
    "native": build_native_parser,
    "assembly": build_assembly_parser,
}
_DISPATCHERS = {
    "governance": dispatch_governance,
    "reconstruction": dispatch_reconstruction,
    "native": dispatch_native,
    "assembly": dispatch_assembly,
}
_LATEST_SHARED_OWNER = {
    ("project", "init"): "assembly",
    ("project", "check"): "assembly",
}
_MERGED_GROUPS = {
    "project": {
        "init": "assembly",
        "check": "assembly",
        "synthesize-layout": "reconstruction",
        "explain-boundaries": "reconstruction",
        "export": "reconstruction",
    },
    "changeset": {
        "export": "governance",
        "inspect": "governance",
        "apply": "governance",
        "create": "reconstruction",
        "add-operation": "reconstruction",
        "merge": "reconstruction",
        "conflicts": "reconstruction",
        "rebase": "reconstruction",
        "verify": "reconstruction",
        "show": "reconstruction",
    },
    "hybrid": {
        "compose": "native",
        "verify": "native",
        "generate": "assembly",
    },
}


def _subparsers(parser: argparse.ArgumentParser) -> argparse._SubParsersAction[argparse.ArgumentParser]:
    """Return the sub-parsers action of an argparse parser.

    Args:
        parser: The parser expected to have a subcommand action.

    Returns:
        The parser's ``_SubParsersAction``.

    Raises:
        ContractError: If the parser defines no subcommands.
    """
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            return action
    raise ContractError(f"parser {parser.prog!r} has no subcommands")


def _source_parsers() -> dict[str, argparse.ArgumentParser]:
    """Build the top-level parser for each capability owner.

    Returns:
        A mapping from owner name to its freshly built argparse parser.
    """
    return {
        owner: _BUILDERS[owner](prog=f"x86decomp {owner}")
        for owner in _OWNER_ORDER
    }


def _group_parsers() -> dict[tuple[str, str], argparse.ArgumentParser]:
    """Enumerate every ``(owner, group)`` command group across all owners.

    Returns:
        A mapping from ``(owner, group)`` to the group's argparse parser.
    """
    result: dict[tuple[str, str], argparse.ArgumentParser] = {}
    for owner, parser in _source_parsers().items():
        for group, group_parser in _subparsers(parser).choices.items():
            result[(owner, group)] = group_parser
    return result


def _leaf_parsers() -> dict[tuple[str, str, str], argparse.ArgumentParser]:
    """Enumerate every ``(owner, group, action)`` leaf command across all owners.

    Returns:
        A mapping from ``(owner, group, action)`` to the action's argparse parser.
    """
    result: dict[tuple[str, str, str], argparse.ArgumentParser] = {}
    for (owner, group), group_parser in _group_parsers().items():
        for action, action_parser in _subparsers(group_parser).choices.items():
            result[(owner, group, action)] = action_parser
    return result


def _route_owner(group: str, action: str, owners: tuple[str, ...]) -> str:
    """Resolve which owner implements a given canonical ``group``/``action``.

    Precedence is: an explicit ``_MERGED_GROUPS`` declaration, then a
    ``_LATEST_SHARED_OWNER`` override, then the sole available owner.

    Args:
        group: The command group name.
        action: The action name within the group.
        owners: The owners that expose this action, in canonical order.

    Returns:
        The name of the owning subsystem.

    Raises:
        ContractError: If a declared or latest owner is unavailable, or if multiple
            owners remain with no declared route.
    """
    declared = _MERGED_GROUPS.get(group, {}).get(action)
    if declared is not None:
        if declared not in owners:
            raise ContractError(
                f"declared canonical owner {declared} is unavailable for {group} {action}"
            )
        return declared
    shared = _LATEST_SHARED_OWNER.get((group, action))
    if shared is not None:
        if shared not in owners:
            raise ContractError(f"latest owner {shared} is unavailable for {group} {action}")
        return shared
    if len(owners) != 1:
        raise ContractError(
            f"canonical route {group} {action} has ambiguous owners: {', '.join(owners)}"
        )
    return owners[0]


def canonical_routes() -> tuple[dict[str, str], ...]:
    """Compute the resolved canonical routing table.

    Returns:
        A tuple of ``{"group", "action", "owner"}`` records, one per canonical command,
        sorted by group and action.
    """
    candidates: dict[tuple[str, str], list[str]] = defaultdict(list)
    for owner, group, action in _leaf_parsers():
        candidates[(group, action)].append(owner)
    routes = []
    for (group, action), candidates_for_route in sorted(candidates.items()):
        owners = tuple(owner for owner in _OWNER_ORDER if owner in candidates_for_route)
        routes.append({"group": group, "action": action, "owner": _route_owner(group, action, owners)})
    return tuple(routes)


def canonical_groups() -> tuple[str, ...]:
    """Return the sorted set of canonical group names.

    Returns:
        A tuple of distinct group names present in the routing table.
    """
    return tuple(sorted({route["group"] for route in canonical_routes()}))


def command_catalog(*, group: str | None = None, owner: str | None = None) -> dict[str, Any]:
    """Build a filterable catalog of canonical routes and their owners.

    Args:
        group: If given, restrict the catalog to this group.
        owner: If given, restrict the catalog to routes owned by this subsystem.

    Returns:
        A catalog dict with release metadata, group and route counts, the merged-group
        declarations, and the selected routes.

    Raises:
        ContractError: If ``group`` is not a known canonical group or ``owner`` is not a
            known capability owner.
    """
    routes = [
        route
        for route in canonical_routes()
        if (group is None or route["group"] == group)
        and (owner is None or route["owner"] == owner)
    ]
    if group is not None and group not in canonical_groups():
        raise ContractError(f"unknown canonical group: {group}")
    if owner is not None and owner not in _OWNER_ORDER:
        raise ContractError(f"unknown capability owner: {owner}")
    return {
        "schema_version": 1,
        "release": "0.7.11",
        "interface": "canonical x86decomp capability groups",
        "group_count": len(canonical_groups()),
        "route_count": len(canonical_routes()),
        "selected_route_count": len(routes),
        "merged_groups": _MERGED_GROUPS,
        "routes": routes,
    }


def register_canonical_commands(subparsers: Any) -> None:
    """Register the ``commands`` catalog and all canonical groups on a sub-parsers action.

    Adds a ``commands`` listing subcommand and, for each canonical group, a group parser
    that reuses each action's source parser and tags it with its resolved owner for
    dispatch.

    Args:
        subparsers: The argparse sub-parsers action to populate.
    """
    catalog = subparsers.add_parser(
        "commands",
        help="list canonical capability routes and implementation owners",
    )
    catalog.add_argument("--group", choices=canonical_groups())
    catalog.add_argument("--owner", choices=_OWNER_ORDER)
    catalog.set_defaults(_canonical_catalog=True)

    leaves = _leaf_parsers()
    for group in canonical_groups():
        group_parser = subparsers.add_parser(
            group,
            help=f"canonical {group} capability commands",
            description=(
                f"Canonical {group} commands implemented by the current capability subsystem."
            ),
        )
        group_parser.add_argument(
            "--project",
            default=".",
            help="project root used by the capability implementation (default: current directory)",
        )
        group_parser.add_argument("--actor", default="analyst")
        actions = group_parser.add_subparsers(dest="action", required=True)
        for route in (item for item in canonical_routes() if item["group"] == group):
            owner = route["owner"]
            source = leaves[(owner, group, route["action"])]
            parser = actions.add_parser(
                route["action"],
                parents=[source],
                add_help=False,
                help=source.description or f"{route['action']} command",
                description=source.description,
            )
            parser.set_defaults(
                group=group,
                _canonical_owner=owner,
                _canonical_group=group,
                _canonical_action=route["action"],
            )


def dispatch(args: argparse.Namespace) -> Any:
    """Dispatch parsed command arguments to the matching implementation."""
    if getattr(args, "_canonical_catalog", False):
        return command_catalog(group=args.group, owner=args.owner)
    owner = getattr(args, "_canonical_owner", None)
    if owner not in _DISPATCHERS:
        raise ContractError("unhandled canonical command")
    return _DISPATCHERS[owner](args)


def build_parser(*, prog: str = "x86decomp") -> argparse.ArgumentParser:
    """Build the argparse parser for this command surface."""
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Unified x86decomp capability CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    register_canonical_commands(subparsers)
    return parser

def main(argv: list[str] | None = None) -> int:
    """Run the canonical command-line entry point and return its exit status.

    The canonical CLI presents the governance, reconstruction, native, and
    assembly command groups under a single parser. It delegates to
    :func:`x86decomp.cli_utils.run_cli`, which parses ``argv``, dispatches the
    selected command, emits the JSON result, and reports expected user-facing
    errors (including subprocess failures from the native and assembly groups)
    as a structured diagnostic with exit code ``2``.

    Args:
        argv: Argument vector to parse, or ``None`` to use ``sys.argv[1:]``.

    Returns:
        ``0`` on success, or ``2`` when an expected error is reported.
    """
    return run_cli(
        build_parser, dispatch, argv, extra_exceptions=(subprocess.SubprocessError,)
    )


if __name__ == "__main__":
    raise SystemExit(main())

