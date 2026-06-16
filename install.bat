@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

echo.
echo ========================================================
echo    Installing Dependencies
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
python -m pip install --upgrade pip >nul 2>&1

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
echo OK - All dependencies installed!
echo ========================================================
echo.
pause
