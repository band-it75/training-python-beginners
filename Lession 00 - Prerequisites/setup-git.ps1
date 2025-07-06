$Name  = Read-Host "Enter your Git display name"
$Email = Read-Host "Enter your Git email address"

git config --global user.name  "$Name"
git config --global user.email "$Email"
git config --global init.defaultBranch main

Write-Host "Git configuration updated for $Name <$Email>" -ForegroundColor Green
