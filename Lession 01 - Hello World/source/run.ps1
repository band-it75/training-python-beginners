$VenvPath = ".venv"
$activate = Join-Path $VenvPath 'Scripts/Activate.ps1'
if (-not (Test-Path $activate)) {
    $activate = Join-Path $VenvPath 'bin/Activate.ps1'
}
if (-not (Test-Path $activate)) {
    Write-Host "Virtual environment not found. Run setup-venv.ps1 first." -ForegroundColor Red
    exit 1
}
& $activate
python main.py
