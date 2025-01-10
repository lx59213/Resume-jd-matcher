@echo off
echo Initializing project structure...

:: 创建必要的目录
mkdir app 2>nul
mkdir app\static 2>nul
mkdir app\static\css 2>nul
mkdir app\static\js 2>nul
mkdir app\templates 2>nul
mkdir app\utils 2>nul
mkdir uploads 2>nul

:: 创建 utils/__init__.py
echo.> app\utils\__init__.py

:: 创建并写入所有文件内容
call :create_init_py
call :create_config_py
call :create_run_py
call :create_requirements
call :create_env
call :create_routes_py
call :create_pdf_parser
call :create_ai_matcher
call :create_base_html
call :create_index_html
call :create_style_css
call :create_main_js

echo Project structure initialized!
echo Now running pip install...

:: 安装依赖
pip install -r requirements.txt

echo Setup complete! You can now run dev_start.bat
pause
exit /b 0

:create_init_py
echo from flask import Flask> app\__init__.py
echo from config import Config>> app\__init__.py
echo.>> app\__init__.py
echo def create_app(config_class=Config):>> app\__init__.py
echo     app = Flask(__name__)>> app\__init__.py
echo     app.config.from_object(config_class)>> app\__init__.py
echo.>> app\__init__.py
echo     from app.routes import main>> app\__init__.py
echo     app.register_blueprint(main)>> app\__init__.py
echo.>> app\__init__.py
echo     return app>> app\__init__.py
exit /b 0

:create_config_py
echo import os> config.py
echo from dotenv import load_dotenv>> config.py
echo.>> config.py
echo load_dotenv()>> config.py
echo.>> config.py
echo class Config:>> config.py
echo     SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'>> config.py
echo     UPLOAD_FOLDER = 'uploads'>> config.py
echo     MAX_CONTENT_LENGTH = 16 * 1024 * 1024>> config.py
echo     ALLOWED_EXTENSIONS = {'pdf'}>> config.py
echo     OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')>> config.py
exit /b 0

:create_run_py
echo from app import create_app> run.py
echo.>> run.py
echo app = create_app()>> run.py
echo.>> run.py
echo if __name__ == '__main__':>> run.py
echo     app.run(debug=True)>> run.py
exit /b 0

:create_requirements
echo flask==2.0.1> requirements.txt
echo python-dotenv==0.19.0>> requirements.txt
echo PyPDF2==3.0.1>> requirements.txt
echo openai==1.3.0>> requirements.txt
echo python-multipart==0.0.6>> requirements.txt
exit /b 0

:create_env
echo OPENAI_API_KEY=your-api-key-here> .env
echo SECRET_KEY=your-secret-key-here>> .env
exit /b 0

:create_routes_py
echo from flask import Blueprint, render_template, request, jsonify, current_app> app\routes.py
echo from werkzeug.utils import secure_filename>> app\routes.py
echo import os>> app\routes.py
echo from app.utils.pdf_parser import extract_text_from_pdf>> app\routes.py
echo from app.utils.ai_matcher import generate_matched_resume>> app\routes.py
echo.>> app\routes.py
echo main = Blueprint("main", __name__)>> app\routes.py
echo.>> app\routes.py
call :create_routes_content>> app\routes.py
exit /b 0

:create_pdf_parser
echo import PyPDF2> app\utils\pdf_parser.py
echo import io>> app\utils\pdf_parser.py
echo.>> app\utils\pdf_parser.py
call :create_pdf_parser_content>> app\utils\pdf_parser.py
exit /b 0

:create_ai_matcher
echo import openai> app\utils\ai_matcher.py
echo from flask import current_app>> app\utils\ai_matcher.py
echo.>> app\utils\ai_matcher.py
call :create_ai_matcher_content>> app\utils\ai_matcher.py
exit /b 0

:create_base_html
echo ^<!DOCTYPE html^>> app\templates\base.html
call :create_base_html_content>> app\templates\base.html
exit /b 0

:create_index_html
echo {% extends "base.html" %}> app\templates\index.html
call :create_index_html_content>> app\templates\index.html
exit /b 0

:create_style_css
echo .card {> app\static\css\style.css
call :create_style_css_content>> app\static\css\style.css
exit /b 0

:create_main_js
echo document.getElementById("uploadForm").addEventListener("submit", async function(e) {> app\static\js\main.js
call :create_main_js_content>> app\static\js\main.js
exit /b 0 