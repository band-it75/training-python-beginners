Write-Host "Checking prerequisites..." -ForegroundColor Cyan

$missing = @()

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    $missing += 'Python'
} else {
    python --version
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    $missing += 'Git'
} else {
    git --version
}

if (-not (Get-Command code -ErrorAction SilentlyContinue)) {
    $missing += 'VSCode'
} else {
    code --version
}

if ($missing.Count -eq 0) {
    Write-Host "All prerequisites found." -ForegroundColor Green
} else {
    Write-Host "Missing: $($missing -join ', ')" -ForegroundColor Red
    exit 1
}
