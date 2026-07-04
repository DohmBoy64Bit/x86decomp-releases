param([string]$Config = "x86decomp-test.json")
$ErrorActionPreference = "Stop"
& x86decomp-test run --config $Config --verbose
exit $LASTEXITCODE
