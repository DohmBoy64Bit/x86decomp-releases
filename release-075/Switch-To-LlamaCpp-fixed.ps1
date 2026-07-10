# Switch-To-LlamaCpp.ps1
# Downloads llama.cpp Vulkan build, finds LM Studio GGUF models,
# starts llama-server, tests it, and optionally writes opencode.json.

[CmdletBinding()]
param(
    [string]$InstallDir = "C:\Tools\llama.cpp",

    # Leave empty to pick from LM Studio models interactively.
    [string]$ModelPath = "",

    # Optional multimodal projector file. Leave empty to auto-detect/prompt.
    [string]$MmprojPath = "",

    [string]$HostAddress = "127.0.0.1",
    [int]$Port = 8080,

    # Good starting point. Lower this if you run out of RAM/VRAM.
    [int]$ContextSize = 16384,

    # Use auto so llama.cpp can fit GPU layers to available VRAM.
    [string]$GpuLayers = "auto",

    # This becomes the OpenAI-compatible model name.
    [string]$ModelAlias = "local",

    # Optional Jinja template file, for special Qwen templates.
    [string]$TemplateFile = "",

    [switch]$ForceDownload,
    [switch]$SkipOpenCodeConfig,

    # Leave empty to write ./opencode.json in the current folder.
    [string]$OpenCodeConfigPath = ""
)

$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function ConvertTo-PowerShellStringLiteral {
    param([string]$Value)
    return "'" + ($Value -replace "'", "''") + "'"
}

function Get-ClientBaseUrl {
    param(
        [string]$HostAddress,
        [int]$Port
    )

    $testHost = $HostAddress
    if ($HostAddress -eq "0.0.0.0" -or $HostAddress -eq "::") {
        $testHost = "127.0.0.1"
    }

    return "http://$testHost`:$Port"
}

function Install-LlamaCpp {
    param(
        [string]$InstallDir,
        [switch]$ForceDownload
    )

    if ((Test-Path $InstallDir) -and -not $ForceDownload) {
        $existingServer = Get-ChildItem -Path $InstallDir -Recurse -Filter "llama-server.exe" -ErrorAction SilentlyContinue |
            Select-Object -First 1

        if ($existingServer) {
            Write-Host "Found existing llama-server.exe:"
            Write-Host $existingServer.FullName
            return $existingServer.FullName
        }
    }

    if ($ForceDownload -and (Test-Path $InstallDir)) {
        Write-Step "Removing old llama.cpp install"
        Remove-Item -Path $InstallDir -Recurse -Force
    }

    New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null

    Write-Step "Downloading latest llama.cpp Windows x64 Vulkan release"

    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

    $releaseUrl = "https://api.github.com/repos/ggml-org/llama.cpp/releases/latest"
    $headers = @{
        "User-Agent" = "PowerShell llama.cpp setup"
        "Accept"     = "application/vnd.github+json"
    }

    $release = Invoke-RestMethod -Uri $releaseUrl -Headers $headers

    $asset = $release.assets |
        Where-Object {
            $_.name -match "\.zip$" -and
            $_.name -match "(?i)win" -and
            $_.name -match "(?i)x64" -and
            $_.name -match "(?i)vulkan"
        } |
        Select-Object -First 1

    if (-not $asset) {
        Write-Host "Could not auto-find the Vulkan Windows x64 zip asset." -ForegroundColor Yellow
        Write-Host "Assets found:"
        $release.assets | ForEach-Object { Write-Host " - $($_.name)" }
        throw "No Windows x64 Vulkan asset found in the latest llama.cpp release."
    }

    $zipPath = Join-Path $env:TEMP $asset.name

    Write-Host "Asset: $($asset.name)"
    Write-Host "Saving to: $zipPath"

    Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $zipPath -Headers $headers

    Write-Step "Extracting llama.cpp"
    Expand-Archive -Path $zipPath -DestinationPath $InstallDir -Force

    $server = Get-ChildItem -Path $InstallDir -Recurse -Filter "llama-server.exe" -ErrorAction SilentlyContinue |
        Select-Object -First 1

    if (-not $server) {
        throw "Downloaded/extracted llama.cpp, but llama-server.exe was not found."
    }

    return $server.FullName
}

function Select-GgufModel {
    param([string]$ModelPath)

    if ($ModelPath -and (Test-Path $ModelPath)) {
        return (Resolve-Path $ModelPath).Path
    }

    if ($ModelPath -and -not (Test-Path $ModelPath)) {
        throw "ModelPath was provided but does not exist: $ModelPath"
    }

    Write-Step "Searching LM Studio model folders for GGUF files"

    $candidateRoots = @(
        "$env:USERPROFILE\.lmstudio\models",
        "$env:LOCALAPPDATA\LM Studio\models"
    ) | Where-Object { Test-Path $_ }

    if (-not $candidateRoots -or $candidateRoots.Count -eq 0) {
        Write-Host "Could not find LM Studio model folders automatically." -ForegroundColor Yellow
        $manual = Read-Host "Paste the full path to your .gguf model"
        if (-not (Test-Path $manual)) {
            throw "Model path does not exist: $manual"
        }
        return (Resolve-Path $manual).Path
    }

    $ggufs = foreach ($root in $candidateRoots) {
        Get-ChildItem -Path $root -Recurse -Filter "*.gguf" -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -notmatch '^(?i:mmproj)' }
    }

    $ggufs = $ggufs | Sort-Object LastWriteTime -Descending

    if (-not $ggufs -or $ggufs.Count -eq 0) {
        Write-Host "No .gguf files found in LM Studio folders." -ForegroundColor Yellow
        $manual = Read-Host "Paste the full path to your .gguf model"
        if (-not (Test-Path $manual)) {
            throw "Model path does not exist: $manual"
        }
        return (Resolve-Path $manual).Path
    }

    Write-Host ""
    Write-Host "Pick a model:"
    for ($i = 0; $i -lt $ggufs.Count; $i++) {
        $sizeGb = [math]::Round($ggufs[$i].Length / 1GB, 2)
        Write-Host ("[{0}] {1}  ({2} GB)" -f ($i + 1), $ggufs[$i].FullName, $sizeGb)
    }

    do {
        $choiceRaw = Read-Host "Enter number"
        $choice = 0
        [void][int]::TryParse($choiceRaw, [ref]$choice)
    } while ($choice -lt 1 -or $choice -gt $ggufs.Count)

    return $ggufs[$choice - 1].FullName
}

function Select-MmprojModel {
    param(
        [string]$ModelPath,
        [string]$MmprojPath
    )

    if ($MmprojPath -and (Test-Path $MmprojPath)) {
        return (Resolve-Path $MmprojPath).Path
    }

    if ($MmprojPath -and -not (Test-Path $MmprojPath)) {
        throw "MmprojPath was provided but does not exist: $MmprojPath"
    }

    $modelDir = Split-Path $ModelPath -Parent

    $mmprojs = Get-ChildItem -Path $modelDir -Filter "mmproj*.gguf" -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending

    if (-not $mmprojs -or $mmprojs.Count -eq 0) {
        return ""
    }

    Write-Host ""
    $answer = Read-Host "Found multimodal projector file(s). Run in multimodal mode with --mmproj? [y/N]"

    if ($answer -notmatch "^(y|yes)$") {
        return ""
    }

    if ($mmprojs.Count -eq 1) {
        Write-Host "Selected multimodal projector:"
        Write-Host $mmprojs[0].FullName
        return $mmprojs[0].FullName
    }

    Write-Host ""
    Write-Host "Pick a multimodal projector:"
    for ($i = 0; $i -lt $mmprojs.Count; $i++) {
        $sizeGb = [math]::Round($mmprojs[$i].Length / 1GB, 2)
        Write-Host ("[{0}] {1}  ({2} GB)" -f ($i + 1), $mmprojs[$i].FullName, $sizeGb)
    }

    do {
        $choiceRaw = Read-Host "Enter number"
        $choice = 0
        [void][int]::TryParse($choiceRaw, [ref]$choice)
    } while ($choice -lt 1 -or $choice -gt $mmprojs.Count)

    return $mmprojs[$choice - 1].FullName
}

function New-LlamaLauncher {
    param(
        [string]$ServerExe,
        [string]$ModelPath,
        [string]$InstallDir,
        [string]$HostAddress,
        [int]$Port,
        [int]$ContextSize,
        [string]$GpuLayers,
        [string]$ModelAlias,
        [string]$TemplateFile,
        [string]$MmprojPath
    )

    Write-Step "Creating llama-server launcher"

    $serverDir = Split-Path $ServerExe -Parent
    $launcherPath = Join-Path $InstallDir "start-llama-server.ps1"

    $serverArgs = @(
        "--model", $ModelPath,
        "--ctx-size", "$ContextSize",
        "--gpu-layers", "$GpuLayers",
        "--no-mmap",
        "--host", $HostAddress,
        "--port", "$Port",
        "--alias", $ModelAlias
    )

    if ($MmprojPath -and (Test-Path $MmprojPath)) {
        $serverArgs += @("--mmproj", (Resolve-Path $MmprojPath).Path)
    }
    elseif ($MmprojPath -and -not (Test-Path $MmprojPath)) {
        throw "MmprojPath was provided but does not exist: $MmprojPath"
    }

    if ($TemplateFile -and (Test-Path $TemplateFile)) {
        $serverArgs += @("--jinja", "--chat-template-file", (Resolve-Path $TemplateFile).Path)
    }
    elseif ($TemplateFile -and -not (Test-Path $TemplateFile)) {
        throw "TemplateFile was provided but does not exist: $TemplateFile"
    }

    $argArrayText = ($serverArgs | ForEach-Object {
        "    " + (ConvertTo-PowerShellStringLiteral $_)
    }) -join ",`r`n"

    $launcherContent = @"
`$ErrorActionPreference = 'Stop'

Set-Location $(ConvertTo-PowerShellStringLiteral $serverDir)

`$argsForServer = @(
$argArrayText
)

Write-Host 'Starting llama-server...' -ForegroundColor Cyan
Write-Host $(ConvertTo-PowerShellStringLiteral "$ServerExe") -ForegroundColor DarkGray
Write-Host (`$argsForServer -join ' ') -ForegroundColor DarkGray

& $(ConvertTo-PowerShellStringLiteral $ServerExe) @argsForServer
"@

    Set-Content -Path $launcherPath -Value $launcherContent -Encoding UTF8

    Write-Host "Launcher created:"
    Write-Host $launcherPath

    return $launcherPath
}

function Start-LlamaServerWindow {
    param([string]$LauncherPath)

    Write-Step "Starting llama-server in a new PowerShell window"

    Start-Process `
        -FilePath "powershell.exe" `
        -ArgumentList "-NoExit -ExecutionPolicy Bypass -File `"$LauncherPath`"" `
        -WorkingDirectory (Split-Path $LauncherPath -Parent) | Out-Null
}

function Wait-ForLlamaServer {
    param(
        [string]$BaseUrl,
        [int]$TimeoutSeconds = 120
    )

    Write-Step "Waiting for llama-server to become ready"

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)

    while ((Get-Date) -lt $deadline) {
        try {
            Invoke-RestMethod -Uri "$BaseUrl/v1/models" -Method Get -TimeoutSec 5 | Out-Null
            Write-Host "llama-server is responding at $BaseUrl"
            return $true
        }
        catch {
            Start-Sleep -Seconds 2
        }
    }

    Write-Host "Server did not respond within $TimeoutSeconds seconds." -ForegroundColor Yellow
    Write-Host "It may still be loading the model. Check the llama-server PowerShell window."
    return $false
}

function Test-LlamaChat {
    param(
        [string]$BaseUrl,
        [string]$ModelAlias
    )

    Write-Step "Testing OpenAI-compatible chat endpoint"

    $body = @{
        model = $ModelAlias
        messages = @(
            @{
                role = "user"
                content = "Say hello in one sentence."
            }
        )
        max_tokens = 64
        temperature = 0.2
    } | ConvertTo-Json -Depth 10

    try {
        $response = Invoke-RestMethod `
            -Uri "$BaseUrl/v1/chat/completions" `
            -Method Post `
            -ContentType "application/json" `
            -Headers @{ Authorization = "Bearer no-key" } `
            -Body $body `
            -TimeoutSec 120

        $reply = $response.choices[0].message.content
        Write-Host ""
        Write-Host "Model replied:" -ForegroundColor Green
        Write-Host $reply
    }
    catch {
        Write-Host "Chat test failed." -ForegroundColor Yellow
        Write-Host $_.Exception.Message
        Write-Host "The server may still be warming up, or the selected model/chat template may need adjustment."
    }
}

function Write-OpenCodeConfig {
    param(
        [string]$Path,
        [string]$BaseUrl,
        [string]$ModelAlias
    )

    Write-Step "Writing OpenCode config"

    $parent = Split-Path $Path -Parent
    if ($parent -and -not (Test-Path $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    if (Test-Path $Path) {
        $backup = "$Path.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
        Copy-Item -Path $Path -Destination $backup -Force
        Write-Host "Existing config backed up to:"
        Write-Host $backup
    }

    $models = [ordered]@{}
    $models[$ModelAlias] = [ordered]@{
        name = "Local llama.cpp Model"
    }

    $json = @"
{
  "`$schema": "https://opencode.ai/config.json",
  "provider": {
    "llama.cpp": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "llama-server local",
      "options": {
        "baseURL": "$BaseUrl/v1"
      },
      "models": {
        "$ModelAlias": {
          "name": "Local llama.cpp Model"
        }
      }
    }
  },
  "model": "llama.cpp/$ModelAlias",
  "small_model": "llama.cpp/$ModelAlias"
}
"@

    Set-Content -Path $Path -Value $json -Encoding UTF8

    Write-Host "OpenCode config written:"
    Write-Host $Path
}

# ---------------- MAIN ----------------

Write-Step "Checking Windows architecture"

if (-not [Environment]::Is64BitOperatingSystem) {
    throw "This script expects 64-bit Windows."
}

$serverExe = Install-LlamaCpp -InstallDir $InstallDir -ForceDownload:$ForceDownload
$selectedModel = Select-GgufModel -ModelPath $ModelPath

Write-Step "Selected model"
Write-Host $selectedModel

$selectedMmproj = Select-MmprojModel -ModelPath $selectedModel -MmprojPath $MmprojPath

$launcher = New-LlamaLauncher `
    -ServerExe $serverExe `
    -ModelPath $selectedModel `
    -InstallDir $InstallDir `
    -HostAddress $HostAddress `
    -Port $Port `
    -ContextSize $ContextSize `
    -GpuLayers $GpuLayers `
    -ModelAlias $ModelAlias `
    -TemplateFile $TemplateFile `
    -MmprojPath $selectedMmproj

Start-LlamaServerWindow -LauncherPath $launcher

$clientBaseUrl = Get-ClientBaseUrl -HostAddress $HostAddress -Port $Port

$ready = Wait-ForLlamaServer -BaseUrl $clientBaseUrl -TimeoutSeconds 120

if ($ready) {
    Test-LlamaChat -BaseUrl $clientBaseUrl -ModelAlias $ModelAlias
}

if (-not $SkipOpenCodeConfig) {
    if (-not $OpenCodeConfigPath) {
        $OpenCodeConfigPath = Join-Path (Get-Location) "opencode.json"
    }

    Write-Host ""
    $answer = Read-Host "Write OpenCode config to '$OpenCodeConfigPath'? Existing file will be backed up. [Y/n]"

    if ($answer -notmatch "^(n|no)$") {
        Write-OpenCodeConfig -Path $OpenCodeConfigPath -BaseUrl $clientBaseUrl -ModelAlias $ModelAlias
    }
    else {
        Write-Host "Skipped OpenCode config."
    }
}

Write-Host ""
Write-Host "Done." -ForegroundColor Green
Write-Host "llama.cpp endpoint: $clientBaseUrl/v1"
Write-Host "Model alias: $ModelAlias"
Write-Host "Launcher: $launcher"