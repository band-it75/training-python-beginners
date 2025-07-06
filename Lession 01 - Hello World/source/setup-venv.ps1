$VenvPath = ".venv"
Write-Host "Creating virtual environment in $VenvPath" -ForegroundColor Cyan
python -m venv $VenvPath

$activate = Join-Path $VenvPath 'Scripts/Activate.ps1'
if (-not (Test-Path $activate)) {
    $activate = Join-Path $VenvPath 'bin/Activate.ps1'
}
& $activate
pip install -r requirements.txt
Write-Host "Virtual environment ready." -ForegroundColor Green
