@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

echo.
echo ========================================================
echo    Auto Helper Setup
echo ========================================================
echo.

REM Get Windows username
for /f "tokens=*" %%A in ('whoami /user /fo list /v ^| findstr UserName') do (
    set "line=%%A"
    for /f "tokens=2*" %%B in ('echo !line!') do (
        set USERNAME=%%C
    )
)

if not defined USERNAME (
    set USERNAME=%username%
)

echo Found Windows username: %USERNAME%
echo.

echo Updating configuration files...
echo.

REM Update config.yaml
python -c "import sys; sys.exit(0)" >nul 2>&1
if errorlevel 1 (
    echo Error: Python not detected
    echo Please install Python: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

python -c "username = '%USERNAME%'; content = open('config.yaml', 'r', encoding='utf-8').read(); content = content.replace('YourUsername', username); open('config.yaml', 'w', encoding='utf-8').write(content); print(f'Updated config with username: {username}')"

echo.
echo OK - Configuration updated
echo.

REM Install dependencies
echo Installing dependencies...
echo.
call install.bat

if errorlevel 1 (
    echo.
    echo Setup failed!
    pause
    exit /b 1
)

echo.
echo ========================================================
echo SETUP COMPLETE!
echo ========================================================
echo.
echo Next: Double-click run.bat to start Auto Helper
echo.
pause
