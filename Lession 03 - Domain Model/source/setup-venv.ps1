# SESSION 01 – Hello World/source/setup-venv.ps1

# 1) Where am I?
$scriptDir = $PSScriptRoot

# 2) Build the paths we need
$projectRoot  = Join-Path $scriptDir '..'
$venvPath     = Join-Path $projectRoot '.venv'
$reqFile      = Join-Path $scriptDir  'requirements.txt'

# 3) Create the virtualenv
Write-Host "Creating virtual environment in $venvPath"
python -m venv $venvPath

# 4) Find the activation script
$activateScript = Join-Path $venvPath 'Scripts\Activate.ps1'
if (-not (Test-Path $activateScript)) {
    $activateScript = Join-Path $venvPath 'bin/Activate.ps1'
}
if (-not (Test-Path $activateScript)) {
    Write-Host "ERROR: venv activation script not found. Did venv creation fail?" -ForegroundColor Red
    exit 1
}

# 5) Activate and install
& $activateScript

if (-not (Test-Path $reqFile)) {
    Write-Host "ERROR: Requirements file not found at $reqFile" -ForegroundColor Red
    exit 1
}
Write-Host "Installing dependencies from $reqFile"
pip install --upgrade pip
pip install -r $reqFile

Write-Host "✅ Virtual environment ready."
