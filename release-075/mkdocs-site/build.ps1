$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

function Invoke-CheckedNative($Command, $Arguments) {
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Command failed with exit code $LASTEXITCODE"
    }
}

Invoke-CheckedNative python @('-m', 'mkdocs', 'build', '--strict')
Invoke-CheckedNative python @('.\scripts\verify_end_user_site.py')
