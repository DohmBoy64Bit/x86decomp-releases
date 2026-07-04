"""Bounded local-model proposal and exact byte-match integration."""

from .matching import generate_candidate, run_match_loop, verify_match_report
from .profiles import create_profile, load_profile, provider_catalog, validate_profile
from .prompts import build_messages, load_job, prompt_record
from .transport import probe_profile

__all__ = [
    "build_messages",
    "create_profile",
    "generate_candidate",
    "load_job",
    "load_profile",
    "probe_profile",
    "prompt_record",
    "provider_catalog",
    "run_match_loop",
    "validate_profile",
    "verify_match_report",
]
