@echo off
chcp 65001 >nul
echo.
echo ════════════════════════════════════════════════════
echo    📦 安装依赖
echo    Installing Dependencies
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

REM 升级 pip
echo 🔄 升级 pip...
python -m pip install --upgrade pip

echo.
echo 📥 正在安装依赖包...
echo.

REM 安装依赖
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ❌ 安装失败！
    echo.
    pause
    exit /b 1
)

echo.
echo ════════════════════════════════════════════════════
echo ✅ 所有依赖安装完成！
echo ════════════════════════════════════════════════════
echo.
echo 下一步:
echo 1. 编辑 config.yaml 文件配置您的任务
echo 2. 修改配置文件中的用户名和路径
echo 3. 双击 run.bat 启动自动化助手
echo.
pause
