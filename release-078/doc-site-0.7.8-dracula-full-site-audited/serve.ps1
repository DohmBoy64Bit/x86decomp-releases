$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root
python -m mkdocs serve
if ($LASTEXITCODE -ne 0) {
    throw "mkdocs serve failed with exit code $LASTEXITCODE"
}
