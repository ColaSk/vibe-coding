# Build the frozen control-plane sidecar into packaging/dist/cursor-switch-server/
# Freezes from a neutral SystemDrive tree so the binary does not embed profile paths.
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$BuildRoot = if ($env:CURSOR_SWITCH_BUILD_ROOT) {
  $env:CURSOR_SWITCH_BUILD_ROOT
} else {
  Join-Path $env:SystemDrive "cursor-switch-build"
}
$Src = Join-Path $BuildRoot "src"
$Out = Join-Path $Root "packaging\dist\cursor-switch-server"
$DeveloperHomePrefix = if ($Root -match '^(?:[A-Za-z]:)?\\Users\\[^\\]+') {
  $Matches[0]
} else {
  $null
}

function Test-NeutralPath([string]$PathValue) {
  return -not ($PathValue -match '(?i)([\\/]Users[\\/]|\\home\\)')
}

Write-Host "Build root: $BuildRoot"
if (Test-Path $BuildRoot) { Remove-Item -Recurse -Force $BuildRoot }
New-Item -ItemType Directory -Path $Src | Out-Null

robocopy $Root $Src /E /NFL /NDL /NJH /NJS /nc /ns /np `
  /XD .git .venv node_modules `
  "apps\desktop\dist" "apps\desktop\release" "packaging\build" "packaging\dist" `
  __pycache__ .pytest_cache | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed with code $LASTEXITCODE" }

$env:HOME = Join-Path $BuildRoot "home"
$env:USERPROFILE = $env:HOME
$env:APPDATA = Join-Path $env:HOME "AppData\Roaming"
$env:LOCALAPPDATA = Join-Path $env:HOME "AppData\Local"
$env:USER = "builder"
$env:USERNAME = "builder"
$env:PYTHONNOUSERSITE = "1"
Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path $env:HOME -Force | Out-Null

if ($env:CURSOR_SWITCH_BUILD_PYTHON) {
  $BuildPython = $env:CURSOR_SWITCH_BUILD_PYTHON
  if (-not (Test-NeutralPath $BuildPython)) {
    throw "CURSOR_SWITCH_BUILD_PYTHON must not live under a user profile path."
  }
} else {
  $MambaRoot = Join-Path $BuildRoot "mamba"
  $EnvPrefix = Join-Path $BuildRoot "env"
  $MambaBinDir = Join-Path $BuildRoot "bin"
  New-Item -ItemType Directory -Path $MambaBinDir -Force | Out-Null
  $Zip = Join-Path $BuildRoot "micromamba.tar.bz2"
  Write-Host "Bootstrapping isolated Python under $BuildRoot via micromamba..."
  Invoke-WebRequest -Uri "https://micro.mamba.pm/api/micromamba/win-64/latest" -OutFile $Zip
  tar -xf $Zip -C $BuildRoot
  $MambaExe = Get-ChildItem -Path $BuildRoot -Recurse -Filter micromamba.exe | Select-Object -First 1
  if (-not $MambaExe) { throw "micromamba.exe not found after download" }
  $env:MAMBA_ROOT_PREFIX = $MambaRoot
  & $MambaExe.FullName create -y -p $EnvPrefix "python=3.12" pip
  $BuildPython = Join-Path $EnvPrefix "python.exe"
}

Write-Host "Build python: $BuildPython"
if (-not (Test-NeutralPath $BuildPython)) {
  throw "Build python path is not neutral: $BuildPython"
}

& $BuildPython -m pip install -U pip
& $BuildPython -m pip install -e $Src
& $BuildPython -m pip install "pyinstaller>=6.11"

$buildDir = Join-Path $Src "packaging\build"
$distDir = Join-Path $Src "packaging\dist"
if (Test-Path $buildDir) { Remove-Item -Recurse -Force $buildDir }
if (Test-Path $distDir) { Remove-Item -Recurse -Force $distDir }

Set-Location $Src
$env:PYTHONPATH = "server"
& $BuildPython -m PyInstaller `
  --noconfirm `
  --clean `
  --distpath packaging\dist `
  --workpath packaging\build `
  packaging\cursor-switch-server.spec

$rootDist = Join-Path $Root "packaging\dist"
$rootBuild = Join-Path $Root "packaging\build"
if (Test-Path $rootBuild) { Remove-Item -Recurse -Force $rootBuild }
if (Test-Path $rootDist) { Remove-Item -Recurse -Force $rootDist }
New-Item -ItemType Directory -Path $rootDist | Out-Null
Copy-Item -Recurse (Join-Path $Src "packaging\dist\cursor-switch-server") $rootDist

if ($DeveloperHomePrefix) {
  $find = & cmd /c "findstr /S /M /C:$DeveloperHomePrefix `"$Out\*`"" 2>$null
  if ($LASTEXITCODE -eq 0 -and $find) {
    throw "ERROR: packaged sidecar embeds developer home path $DeveloperHomePrefix:`n$($find -join "`n")"
  }
}

Write-Host "Built: $Out"
