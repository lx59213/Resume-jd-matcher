@echo off
setlocal enabledelayedexpansion

:: Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not accessible. Please ensure Python is installed and in your PATH.
    pause
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Install dependencies
if exist "requirements.txt" (
    echo Installing dependencies...
    pip install -r requirements.txt
)

:: Create uploads directory if it doesn't exist
if not exist "uploads" mkdir uploads

:: Set Flask environment variables
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1

:: Start Flask server
echo Starting Flask server...
start cmd /k "venv\Scripts\activate.bat && python -m flask run"

:: Wait for server to start
timeout /t 3 /nobreak

:: Open browser
start http://localhost:5000

echo Development environment is ready!
pause