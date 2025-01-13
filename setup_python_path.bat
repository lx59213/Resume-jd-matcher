@echo off
setlocal enabledelayedexpansion

:: 保持窗口打开并显示标题
title Python Setup

:: 记录日志
echo Setup started at %TIME% > python_setup.log

:: 尝试查找 Python
for %%P in (
    "C:\Python313\python.exe"
    "C:\Users\hasee\AppData\Local\Programs\Python\Python313\python.exe"
    "C:\不要放这里\Python313\python.exe"
) do (
    if exist %%P (
        echo Found Python at %%P >> python_setup.log
        set "PYTHON_EXE=%%P"
        for %%I in ("%%~dpP.") do set "PYTHON_PATH=%%~fI"
        goto :found_python
    )
)

:python_not_found
echo Python not found in common locations >> python_setup.log
echo Python installation not found in expected locations.
echo Please check python_setup.log for details.
pause
exit /b 1

:found_python
echo Using Python at: %PYTHON_EXE% >> python_setup.log

:: 验证 Python
"%PYTHON_EXE%" -V >> python_setup.log 2>&1
if errorlevel 1 (
    echo Failed to run Python >> python_setup.log
    echo Failed to run Python. Check python_setup.log for details.
    pause
    exit /b 1
)

:: 设置环境变量
set "PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%"
echo PATH updated >> python_setup.log

:: 显示成功信息
echo Python configured successfully at %PYTHON_PATH%
echo Setup completed successfully >> python_setup.log

:: 导出变量
endlocal & (
    set "PATH=%PATH%"
    set "PYTHON_PATH=%PYTHON_PATH%"
    set "PYTHON_EXE=%PYTHON_EXE%"
)

:: 确保看到结果
echo Setup complete. Press any key to continue...
pause > nul 