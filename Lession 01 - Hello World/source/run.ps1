# SESSION 01 – Hello World/source/run.ps1

# 1) Where am I?
$scriptDir  = $PSScriptRoot
$projectRoot = Join-Path $scriptDir '..'
$venvPath    = Join-Path $projectRoot '.venv'

# 2) Find the activation script
$activateScript = Join-Path $venvPath 'Scripts\Activate.ps1'
if (-not (Test-Path $activateScript)) {
    $activateScript = Join-Path $venvPath 'bin/Activate.ps1'
}
if (-not (Test-Path $activateScript)) {
    Write-Host "Virtual environment not found. Run setup-venv.ps1 first." -ForegroundColor Red
    exit 1
}

# 3) Activate and run main.py
& $activateScript

$mainFile = Join-Path $scriptDir 'main.py'
if (-not (Test-Path $mainFile)) {
    Write-Host "ERROR: main.py not found at $mainFile" -ForegroundColor Red
    exit 1
}
python $mainFile
