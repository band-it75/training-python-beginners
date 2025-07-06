# SESSION 01 – Hello World/source/run.ps1

# 1) Where am I?
$scriptDir   = $PSScriptRoot
$projectRoot = Join-Path $scriptDir '..'
$venvPath    = Join-Path $projectRoot '.venv'
$setupScript = Join-Path $scriptDir  'setup-venv.ps1'

# 2) If there's no virtual environment, create it
if (-not (Test-Path $venvPath)) {
    Write-Host "No virtual environment found at $venvPath. Running setup-venv.ps1…" -ForegroundColor Yellow
    & $setupScript

    # After setup, make sure it actually exists
    if (-not (Test-Path $venvPath)) {
        Write-Host "ERROR: Failed to create virtual environment. Aborting." -ForegroundColor Red
        exit 1
    }
}

# 3) Find the activation script
$activateScript = Join-Path $venvPath 'Scripts\Activate.ps1'
if (-not (Test-Path $activateScript)) {
    $activateScript = Join-Path $venvPath 'bin/Activate.ps1'
}
if (-not (Test-Path $activateScript)) {
    Write-Host "Virtual environment activation script not found. Abort." -ForegroundColor Red
    exit 1
}

# 4) Activate and run main.py
& $activateScript

$mainFile = Join-Path $scriptDir 'main.py'
if (-not (Test-Path $mainFile)) {
    Write-Host "ERROR: main.py not found at $mainFile" -ForegroundColor Red
    exit 1
}
python $mainFile
