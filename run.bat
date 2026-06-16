@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ========================================================
echo    Auto Helper System - Windows Automation
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

REM Check if dependencies are installed
echo Checking dependencies...
python -c "import yaml" >nul 2>&1
if errorlevel 1 (
    echo WARNING - Dependencies not installed, installing now...
    echo.
    call install.bat
    if errorlevel 1 (
        echo Installation failed
        pause
        exit /b 1
    )
)

echo.
echo OK - All dependencies ready
echo.
echo Starting Auto Helper System...
echo.
echo ========================================================
echo.

REM Run main program
python main.py

echo.
pause
