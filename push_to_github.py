#!/usr/bin/env python3
import subprocess
import os

os.chdir('c:\\Users\\rudra\\OneDrive\\Desktop\\Malaria Detection')

with open('.push_log.txt', 'w', encoding='utf-8') as log:
    log.write('=== Git Push Log ===\n\n')
    
    # Kill any blocking git processes
    log.write('1. Killing git processes...\n')
    subprocess.run(['taskkill', '/F', '/IM ', 'git.exe', '/T'], 
                   capture_output=True, stderr=subprocess.DEVNULL)
    log.write('   Done\n\n')
    
    # Add all files
    log.write('2. Adding files to git...\n')
    result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    log.write(f'   Exit code: {result.returncode}\n')
    if result.stdout:
        log.write(f'   stdout: {result.stdout}\n')
    if result.stderr:
        log.write(f'   stderr: {result.stderr}\n')
    log.write('\n')
    
    # Check git status
    log.write('3. Checking git status...\n')
    result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
    log.write(result.stdout + '\n\n')
    
    # Commit
    log.write('4. Committing files...\n')
    result = subprocess.run(['git', 'commit', '-m', 'Add project files and deployment setup'],
                          capture_output=True, text=True)
    log.write(f'   Exit code: {result.returncode}\n')
    log.write(f'   Output: {result.stdout}\n')
    if result.stderr:
        log.write(f'   Errors: {result.stderr}\n')
    log.write('\n')
    
    # Check log
    log.write('5. Git log:\n')
    result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
    log.write(result.stdout + '\n\n')
    
    # Try push with token
    log.write('6. Pushing to GitHub...\n')
    token = "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"
    push_url = f"https://rudranshprabhakar-coder:{token}@github.com/rudranshprabhakar-coder/Malaria-Detection-using-Deep-Learning.git"
    
    try:
        result = subprocess.run(['git', 'push', '-u', push_url, 'master'],
                              capture_output=True, text=True, timeout=60)
        log.write(f'   Exit code: {result.returncode}\n')
        log.write(f'   Output: {result.stdout}\n')
        if result.stderr:
            log.write(f'   Errors: {result.stderr}\n')
        
        if result.returncode == 0:
            log.write('\n✓ SUCCESS: Code pushed to GitHub!\n')
        else:
            log.write('\n✗ FAILED: Push returned non-zero exit code\n')
    except subprocess.TimeoutExpired:
        log.write('   ✗ TIMEOUT: Push command timed out after 60 seconds\n')
    except Exception as e:
        log.write(f'   ✗ ERROR: {str(e)}\n')

# Print the log file
print(open('.push_log.txt').read())
