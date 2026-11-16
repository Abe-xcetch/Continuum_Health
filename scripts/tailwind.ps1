<#
.SYNOPSIS
  Build or watch Continuum's CSS with the Tailwind standalone CLI (no Node.js).

.EXAMPLE
  .\scripts\tailwind.ps1            # one-off minified build
  .\scripts\tailwind.ps1 -Watch     # rebuild on template changes
#>
param([switch]$Watch)

$ErrorActionPreference = "Stop"

# Keep in sync with scripts/tailwind.sh
$Version = "v4.3.3"
$Sha256 = "e0e260ce048014e9268f6237ff18f8ccf02cef521cbd0ae04e82c2cdf7aa3955"

$Root = Split-Path -Parent $PSScriptRoot
$BinDir = Join-Path $Root "bin"
$Exe = Join-Path $BinDir "tailwindcss-$Version.exe"
$Url = "https://github.com/tailwindlabs/tailwindcss/releases/download/$Version/tailwindcss-windows-x64.exe"

if (-not (Test-Path $Exe)) {
    New-Item -ItemType Directory -Force $BinDir | Out-Null
    Write-Host "Downloading Tailwind CLI $Version ..."
    $Tmp = "$Exe.download"
    Invoke-WebRequest -Uri $Url -OutFile $Tmp -UseBasicParsing
    $Actual = (Get-FileHash $Tmp -Algorithm SHA256).Hash.ToLower()
    if ($Actual -ne $Sha256) {
        Remove-Item $Tmp -Force
        throw "Tailwind CLI checksum mismatch: expected $Sha256, got $Actual"
    }
    Move-Item $Tmp $Exe
}

$InputCss = Join-Path $Root "assets\tailwind.css"
$OutputCss = Join-Path $Root "static\css\app.css"

# The CLI writes its banner and progress to stderr. Under "Stop", Windows PowerShell 5.1
# turns that into a terminating error when output is redirected (2>&1), so rely on the
# exit code instead.
$ErrorActionPreference = "Continue"
if ($Watch) {
    & $Exe -i $InputCss -o $OutputCss --watch
} else {
    & $Exe -i $InputCss -o $OutputCss --minify
}
if ($LASTEXITCODE -ne 0) { throw "Tailwind build failed ($LASTEXITCODE)" }
