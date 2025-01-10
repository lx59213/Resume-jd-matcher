@echo off
echo Setting up Python PATH...

set PYTHON_PATH=E:\PYTHON

:: 检查 Python 是否存在
if not exist "%PYTHON_PATH%\python.exe" (
    echo Error: Python not found at %PYTHON_PATH%
    pause
    exit /b 1
)

:: 添加到系统环境变量 PATH
echo Adding Python to System PATH...
setx /M PATH "%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%"

:: 立即更新当前会话的 PATH
set PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%

:: 验证 Python 安装
echo Testing Python installation...
python --version

echo Setup complete!
echo Please restart your terminal to use Python.
pause 