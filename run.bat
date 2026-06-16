@echo off
chcp 65001 >nul
echo.
echo ════════════════════════════════════════════════════
echo    🤖 Windows 自动化助手系统
echo    Auto Helper System
echo ════════════════════════════════════════════════════
echo.

REM 检查 Python 是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未检测到 Python
    echo 请先安装 Python: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python 已检测到
echo.

REM 检查依赖是否已安装
echo 📦 检查依赖...
python -c "import yaml" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  依赖未安装，正在安装...
    echo.
    call install.bat
    if errorlevel 1 (
        echo ❌ 安装失败
        pause
        exit /b 1
    )
)

echo.
echo ✅ 所有依赖已就绪
echo.
echo 📋 启动自动化助手...
echo.
echo ════════════════════════════════════════════════════
echo.

REM 运行主程序
python main.py

echo.
pause
