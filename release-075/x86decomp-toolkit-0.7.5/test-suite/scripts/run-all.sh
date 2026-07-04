#!/usr/bin/env sh
set -eu
CONFIG="${1:-x86decomp-test.json}"
exec x86decomp-test run --config "$CONFIG" --verbose
