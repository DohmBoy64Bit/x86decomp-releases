"""Provide test-suite.x86decomp_testkit.adapters.installation functionality for the x86decomp-toolkit 0.7.9 release.

This module-level documentation was added during the complete 0.7.9 code audit.
"""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

from ..config import TestConfig, save_config
from ..logging_utils import JsonlEventLogger
from ..models import AdapterKind, AdapterSpec, ProbeResult
from .detection import detect_adapter
from .download import (
    download_file,
    github_latest_release,
    platform_key,
    safe_extract_archive,
    select_release_asset,
)


Prompt = Callable[[str], str]


PACKAGE_MANAGER_PACKAGES: dict[str, dict[str, str]] = {
    "apt": {
        "java": "openjdk-21-jdk",
        "clang": "clang",
        "clangxx": "clang",
        "lld-link": "lld",
        "llvm-lib": "llvm",
        "llvm-readobj": "llvm",
        "llvm-objdump": "llvm",
        "gcc": "gcc",
        "gxx": "g++",
        "cmake": "cmake",
        "ninja": "ninja-build",
    },
    "dnf": {
        "java": "java-21-openjdk-devel",
        "clang": "clang",
        "clangxx": "clang",
        "lld-link": "lld",
        "llvm-lib": "llvm",
        "llvm-readobj": "llvm",
        "llvm-objdump": "llvm",
        "gcc": "gcc",
        "gxx": "gcc-c++",
        "cmake": "cmake",
        "ninja": "ninja-build",
    },
    "brew": {
        "java": "openjdk@21",
        "clang": "llvm",
        "clangxx": "llvm",
        "lld-link": "llvm",
        "llvm-lib": "llvm",
        "llvm-readobj": "llvm",
        "llvm-objdump": "llvm",
        "gcc": "gcc",
        "gxx": "gcc",
        "cmake": "cmake",
        "ninja": "ninja",
    },
    "winget": {
        "java": "Microsoft.OpenJDK.21",
        "clang": "LLVM.LLVM",
        "clangxx": "LLVM.LLVM",
        "lld-link": "LLVM.LLVM",
        "llvm-lib": "LLVM.LLVM",
        "llvm-readobj": "LLVM.LLVM",
        "llvm-objdump": "LLVM.LLVM",
        "cmake": "Kitware.CMake",
        "ninja": "Ninja-build.Ninja",
    },
}


def _yes(value: str) -> bool:
    """Implement yes.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    return value.strip().lower() in {"y", "yes"}


def _find_package_manager() -> str | None:
    """Find package manager.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    for manager in ("apt-get", "dnf", "brew", "winget"):
        if shutil.which(manager):
            return "apt" if manager == "apt-get" else manager
    return None


def _run_checked(command: list[str], event_logger: JsonlEventLogger | None = None) -> None:
    """Run checked.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if event_logger:
        event_logger.emit("adapter.install.command", command=command)
    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        raise RuntimeError(f"installation command failed with exit code {completed.returncode}: {command}")


def install_python_adapter(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None = None) -> None:
    """Install python adapter.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not spec.pip_requirement:
        raise RuntimeError(f"{spec.adapter_id} has no pip installation contract")
    command = [config.python_executable, "-m", "pip", "install", spec.pip_requirement]
    _run_checked(command, event_logger)


def install_github_release(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None = None) -> Path:
    """Install github release.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if not spec.github_repository:
        raise RuntimeError(f"{spec.adapter_id} has no GitHub release source")
    if not config.allow_network:
        raise RuntimeError("network installation is disabled; enable allow_network")
    install_root = config.install_root or (Path.home() / ".x86decomp-test-tools")
    destination = install_root / spec.adapter_id
    destination.mkdir(parents=True, exist_ok=True)

    release = github_latest_release(spec.github_repository)
    key = platform_key()
    tokens = spec.release_asset_patterns.get(key) or spec.release_asset_patterns.get("all")
    if not tokens:
        raise RuntimeError(f"no release asset pattern for {spec.adapter_id} on {key}")
    asset = select_release_asset(release, tokens)
    asset_name = str(asset["name"])
    url = str(asset["browser_download_url"])
    archive = destination / asset_name
    if event_logger:
        event_logger.emit(
            "adapter.install.download.begin",
            adapter_id=spec.adapter_id,
            repository=spec.github_repository,
            release=release.get("tag_name"),
            asset=asset_name,
            url=url,
        )
    sha256 = download_file(url, archive)
    extract_directory = destination / "current"
    temporary = destination / "extracting"
    if temporary.exists():
        shutil.rmtree(temporary)
    temporary.mkdir(parents=True)
    safe_extract_archive(archive, temporary)
    if extract_directory.exists():
        shutil.rmtree(extract_directory)
    temporary.rename(extract_directory)
    if spec.kind == AdapterKind.EXECUTABLE and spec.commands:
        exe_files = [p for p in extract_directory.iterdir() if p.suffix.lower() == ".exe"]
        command_name = spec.commands[0]
        if exe_files and not (extract_directory / command_name).exists() and not (extract_directory / f"{command_name}.exe").exists():
            exe_files[0].rename(extract_directory / f"{command_name}.exe")
    if event_logger:
        event_logger.emit(
            "adapter.install.download.complete",
            adapter_id=spec.adapter_id,
            archive=str(archive),
            sha256=sha256,
            extracted_to=str(extract_directory),
        )
    config.adapter_paths[spec.adapter_id] = str(extract_directory)
    return extract_directory


def install_package_manager_adapter(spec: AdapterSpec, event_logger: JsonlEventLogger | None = None) -> None:
    """Install package manager adapter.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    manager = _find_package_manager()
    if manager is None:
        raise RuntimeError("no supported package manager detected")
    package = PACKAGE_MANAGER_PACKAGES.get(manager, {}).get(spec.adapter_id)
    if not package:
        raise RuntimeError(f"no {manager} installation contract for {spec.adapter_id}")
    elevation: list[str] = []
    if manager in {"apt", "dnf"} and hasattr(os, "geteuid") and os.geteuid() != 0:
        if shutil.which("sudo") is None:
            raise RuntimeError(f"{manager} installation requires root privileges and sudo was not found")
        elevation = ["sudo"]
    if manager == "apt":
        command = [*elevation, "apt-get", "install", "-y", package]
    elif manager == "dnf":
        command = [*elevation, "dnf", "install", "-y", package]
    elif manager == "brew":
        command = ["brew", "install", package]
    elif manager == "winget":
        command = ["winget", "install", "--id", package, "--exact", "--accept-package-agreements", "--accept-source-agreements"]
    else:
        raise RuntimeError(f"unsupported package manager {manager}")
    _run_checked(command, event_logger)


def _validate_custom_path(spec: AdapterSpec, value: str, config: TestConfig) -> ProbeResult:
    """Validate custom path.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if spec.kind == AdapterKind.HTTP_ENDPOINT:
        previous = config.adapter_paths.get(spec.adapter_id)
        config.adapter_paths[spec.adapter_id] = value.strip()
        result = detect_adapter(spec, config)
        if not result.installed:
            if previous is None:
                config.adapter_paths.pop(spec.adapter_id, None)
            else:
                config.adapter_paths[spec.adapter_id] = previous
        return result
    candidate = Path(value).expanduser().absolute()
    if spec.kind == AdapterKind.PYTHON:
        if candidate.is_dir():
            options = (candidate / "bin" / "python", candidate / "Scripts" / "python.exe", candidate / "python", candidate / "python.exe")
            candidate = next((item for item in options if item.is_file()), candidate)
        previous_python = config.python_executable
        config.python_executable = str(candidate)
        result = detect_adapter(spec, config)
        if not result.installed:
            config.python_executable = previous_python
        return result
    previous = config.adapter_paths.get(spec.adapter_id)
    config.adapter_paths[spec.adapter_id] = str(candidate)
    result = detect_adapter(spec, config)
    if not result.installed:
        if previous is None:
            config.adapter_paths.pop(spec.adapter_id, None)
        else:
            config.adapter_paths[spec.adapter_id] = previous
    return result


def _automatic_install_available(spec: AdapterSpec) -> bool:
    """Implement automatic install available.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if spec.kind == AdapterKind.PYTHON and spec.pip_requirement:
        return True
    if spec.github_repository:
        return True
    manager = _find_package_manager()
    return bool(manager and spec.adapter_id in PACKAGE_MANAGER_PACKAGES.get(manager, {}))


def install_adapter(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None = None) -> None:
    """Install adapter.
    
    Parameters and return values follow the signature and runtime validation in the body.
    """
    if spec.kind == AdapterKind.HTTP_ENDPOINT:
        raise RuntimeError(f"{spec.adapter_id} is a live HTTP endpoint and cannot be installed automatically")
    if spec.kind == AdapterKind.PYTHON:
        install_python_adapter(spec, config, event_logger)
    elif spec.github_repository:
        install_github_release(spec, config, event_logger)
    else:
        install_package_manager_adapter(spec, event_logger)


def resolve_missing_adapters(
    catalog: dict[str, AdapterSpec],
    config: TestConfig,
    config_path: Path | None = None,
    adapter_ids: list[str] | None = None,
    prompt: Prompt = input,
    assume_yes: bool = False,
    event_logger: JsonlEventLogger | None = None,
) -> list[ProbeResult]:
    """Detect first, then prompt only for missing adapters.

    No installed adapter produces an interactive question. A missing adapter is never
    silently skipped: it ends installed or remains an explicit unresolved ProbeResult.
    """
    selected = adapter_ids or sorted(catalog)
    results: list[ProbeResult] = []
    for adapter_id in selected:
        spec = catalog[adapter_id]
        initial = detect_adapter(spec, config)
        if event_logger:
            event_logger.emit("adapter.detected", result=initial.to_dict())
        if initial.installed:
            results.append(initial)
            continue

        if event_logger:
            event_logger.emit("adapter.missing", adapter_id=adapter_id, display_name=spec.display_name, required_for=list(spec.required_for), diagnostics=initial.diagnostics)

        if not config.interactive:
            if config.allow_install and _automatic_install_available(spec):
                try:
                    install_adapter(spec, config, event_logger)
                except Exception as exc:
                    unresolved = ProbeResult(adapter_id, False, diagnostics=[*initial.diagnostics, f"automatic installation failed: {exc}"])
                    results.append(unresolved)
                    continue
                results.append(detect_adapter(spec, config))
            else:
                results.append(initial)
            continue

        print(f"\nMissing adapter: {spec.display_name} ({adapter_id})")
        print("Required for: " + ", ".join(spec.required_for))
        if spec.manual_install_note:
            print(spec.manual_install_note)

        has_custom = assume_yes or _yes(prompt("Is it already installed at a custom path? [y/N]: "))
        if event_logger:
            event_logger.emit("adapter.prompt.custom_path", adapter_id=adapter_id, accepted=has_custom)
        if has_custom:
            while True:
                value = prompt("Enter the executable or installation directory (blank to cancel): ").strip()
                if not value:
                    break
                if event_logger:
                    event_logger.emit("adapter.custom_path.attempt", adapter_id=adapter_id, path=str(Path(value).expanduser().absolute()))
                custom_result = _validate_custom_path(spec, value, config)
                if custom_result.installed:
                    print(f"Detected {spec.display_name}: {custom_result.path}")
                    results.append(custom_result)
                    if event_logger:
                        event_logger.emit("adapter.custom_path.accepted", adapter_id=adapter_id, result=custom_result.to_dict())
                    if config_path:
                        save_config(config, config_path)
                    break
                if event_logger:
                    event_logger.emit("adapter.custom_path.rejected", adapter_id=adapter_id, result=custom_result.to_dict())
                print("That path did not satisfy the adapter detection contract.")
                for diagnostic in custom_result.diagnostics:
                    print(f"  - {diagnostic}")
            if results and results[-1].adapter_id == adapter_id and results[-1].installed:
                continue

        can_install = _automatic_install_available(spec)
        should_install = False
        if can_install:
            if config.allow_install and assume_yes:
                should_install = True
            else:
                should_install = _yes(prompt(f"Install {spec.display_name} automatically now? [y/N]: "))
        if event_logger and can_install:
            event_logger.emit("adapter.prompt.install", adapter_id=adapter_id, accepted=should_install, allow_install=config.allow_install, allow_network=config.allow_network)
        if should_install:
            if not config.allow_install:
                print("Automatic installation is disabled. Re-run with --allow-install.")
            else:
                try:
                    install_adapter(spec, config, event_logger)
                    installed = detect_adapter(spec, config)
                    results.append(installed)
                    if config_path:
                        save_config(config, config_path)
                    continue
                except Exception as exc:
                    print(f"Installation failed: {exc}")
                    if event_logger:
                        event_logger.emit("adapter.install.failed", adapter_id=adapter_id, error=str(exc))

        unresolved = detect_adapter(spec, config)
        results.append(unresolved)
        if event_logger:
            event_logger.emit("adapter.unresolved", adapter_id=adapter_id, result=unresolved.to_dict())
        print(f"{spec.display_name} remains unresolved and dependent tests will be BLOCKED, not skipped.")

    if config_path:
        save_config(config, config_path)
    return results
