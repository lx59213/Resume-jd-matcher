@echo off
echo Starting development environment...

:: 检查 Python 是否安装
python --version > nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

:: 检查项目结构
if not exist "app" (
    echo Error: Project structure not found. Please run init_project.bat first
    pause
    exit /b 1
)

:: 创建虚拟环境（如果不存在）
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

:: 激活虚拟环境
call venv\Scripts\activate
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

:: 安装依赖
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

:: 创建uploads文件夹（如果不存在）
if not exist "uploads" mkdir uploads

:: 设置 Flask 环境变量
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1

:: 启动新的命令行窗口运行 Flask
echo Starting Flask server...
start cmd /k "venv\Scripts\activate && python -m flask run"

:: 等待服务器启动
echo Waiting for server to start...
timeout /t 10

:: 启动无安全限制的Chrome（用于开发测试）
echo Starting Chrome with disabled security...
start chrome --user-data-dir="%TEMP%\chrome_dev" --disable-web-security --disable-site-isolation-trials --allow-file-access-from-files http://localhost:5000

echo Development environment is ready!
pause 