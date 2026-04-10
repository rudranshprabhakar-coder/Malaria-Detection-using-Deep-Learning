@echo off
cd /d "c:\Users\rudra\OneDrive\Desktop\Malaria Detection"
taskkill /F /IM git.exe /T 2>nul
timeout /t 1
git add app.py requirements.txt train_model.py templates/ static/ models/ dataset/ .gitignore push.ps1 2>&1
if errorlevel 1 (
    echo Add failed
    exit /b 1
)
git commit -m "Add all project files" 2>&1
if errorlevel 1 (
    echo Commit failed  
    exit /b 1
)
echo Files committed successfully
git log --oneline -3
