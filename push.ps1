#!/usr/bin/env pwsh
# GitHub Push Script

$token = "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"
$repo = "https://${token}@github.com/rudranshprabhakar-coder/Malaria-Detection-using-Deep-Learning.git"

Set-Location "c:\Users\rudra\OneDrive\Desktop\Malaria Detection"

Write-Host "Pushing to GitHub..."
$output = git push $repo master 2>&1
Write-Output $output

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Successfully pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "✗ Push failed with exit code $LASTEXITCODE" -ForegroundColor Red
    Write-Output $output
}
