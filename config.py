import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    ALLOWED_EXTENSIONS = {"pdf"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

    # OpenAI API 配置
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    # 上传文件配置
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")

    # 确保上传目录存在
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
