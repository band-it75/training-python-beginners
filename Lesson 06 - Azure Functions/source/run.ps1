# Session 01 - Hello World/source/run.ps1

# 1) Determine script & project dirs
$scriptDir    = $PSScriptRoot
$projectDir   = Join-Path $scriptDir '..'
$venvDir      = Join-Path $projectDir '.venv'
$setupScript  = Join-Path $scriptDir  'setup-venv.ps1'
$testsDir     = Join-Path $scriptDir  'tests'
$mainScript   = Join-Path $scriptDir  'main.py'

# 2) Bootstrap the virtual-env if missing
if (-not (Test-Path $venvDir)) {
    Write-Host "No virtual environment found at $venvDir. Running setup-venv.ps1..." -ForegroundColor Yellow
    & $setupScript
    if (-not (Test-Path $venvDir)) {
        Write-Host "ERROR: Could not create virtual environment. Aborting." -ForegroundColor Red
        exit 1
    }
}

# 3) Activate the venv
$activateScript = Join-Path $venvDir 'Scripts\Activate.ps1'
if (-not (Test-Path $activateScript)) {
    $activateScript = Join-Path $venvDir 'bin/Activate.ps1'
}
if (-not (Test-Path $activateScript)) {
    Write-Host "ERROR: Activation script not found. Aborting." -ForegroundColor Red
    exit 1
}
& $activateScript

# 4) Run tests (installing pytest if needed, abort on failure)
if (Test-Path $testsDir) {
    # ensure pytest is available
    Write-Host "Checking for pytest..." -ForegroundColor Cyan
    & python -m pytest --version > $null 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "pytest not found. Installing pytest..." -ForegroundColor Yellow
        pip install pytest
    }

    # run the suite
    Write-Host "Running tests in $testsDir..." -ForegroundColor Cyan
    & python -m pytest $testsDir
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Tests failed with exit code $LASTEXITCODE. Aborting run." -ForegroundColor Red
        exit $LASTEXITCODE
    }
    Write-Host "✅ All tests passed." -ForegroundColor Green
} else {
    Write-Host "No tests directory at $testsDir; skipping tests." -ForegroundColor Yellow
}

# 5) Run main.py
if (-not (Test-Path $mainScript)) {
    Write-Host "ERROR: main.py not found at $mainScript" -ForegroundColor Red
    exit 1
}
Write-Host "Launching main.py..." -ForegroundColor Green
python $mainScript
