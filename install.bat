@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ========================================================
echo    Installing Dependencies
echo    Please wait...
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not detected
    echo Please install Python: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo OK - Python detected
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing required packages...
echo.

REM Install dependencies
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation failed!
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo OK - All dependencies installed successfully!
echo ========================================================
echo.
echo Next steps:
echo 1. Open config.yaml and replace 'YourUsername' with your Windows username
echo 2. Double-click run.bat to start Auto Helper
echo.
pause
