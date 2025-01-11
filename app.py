from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    jsonify,
    current_app,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import os
from random import choice

# 判断是否在 Vercel 环境
IS_VERCEL = os.environ.get("VERCEL") == "1"


# 配置类
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    ALLOWED_EXTENSIONS = {"pdf"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    if not IS_VERCEL:  # 只在本地环境创建上传目录
        UPLOAD_FOLDER = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "uploads"
        )
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 创建蓝图
main = Blueprint("main", __name__)

# 幽默标语
SLOGANS = [
    "面试者问我的专长是什么，我说长相。他很惊讶地说：'马上好？'我说：'不，是从一家公司跳到另一家公司。'",
    "HR问我跳槽频率是什么，我说大家说。她说这不是跳槽频率？我说但我刚刚才想到了。",
]


@main.route("/", methods=["GET"])
def index():
    slogan = choice(SLOGANS)
    return render_template("index.html", slogan=slogan)


@main.route("/favicon.ico")
def favicon():
    return "", 204


@main.route("/upload", methods=["POST"])
def upload_files():
    try:
        if "files[]" not in request.files:
            return jsonify({"error": "没有上传文件"}), 400

        files = request.files.getlist("files[]")
        jd_text = request.form.get("jd", "")

        if not jd_text:
            return jsonify({"error": "没有提供JD"}), 400

        resume_texts = []
        for file in files:
            if file.filename == "":
                continue

            if file and allowed_file(file.filename):
                try:
                    if IS_VERCEL:
                        # Vercel 环境使用模拟数据
                        resume_texts.append("简历内容示例")
                    else:
                        # 本地环境使用实际功能
                        from app.utils.pdf_parser import extract_text_from_pdf

                        text = extract_text_from_pdf(file)
                        resume_texts.append(text)
                except Exception as e:
                    return (
                        jsonify(
                            {"error": f"处理文件 {file.filename} 时出错: {str(e)}"}
                        ),
                        400,
                    )

        if not resume_texts:
            return jsonify({"error": "没有有效的简历文件"}), 400

        try:
            if IS_VERCEL:
                # Vercel 环境使用模拟数据
                result = {
                    "job_analysis": "职位分析示例 (Vercel 演示版本)",
                    "match_analysis": "匹配分析示例 (Vercel 演示版本)",
                    "resume": "生成的简历示例 (Vercel 演示版本)",
                }
            else:
                # 本地环境使用实际功能
                from app.utils.ai_matcher import generate_matched_resume

                result = generate_matched_resume(resume_texts, jd_text)

            return jsonify(result)
        except Exception as e:
            return jsonify({"error": f"生成匹配简历时出错: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"服务器错误: {str(e)}"}), 500


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )


# 创建应用
def create_app():
    if IS_VERCEL:
        # Vercel 环境
        app = Flask(
            __name__, static_folder="app/static", template_folder="app/templates"
        )
    else:
        # 本地环境
        app = Flask(__name__)

    app.config.from_object(Config)
    app.register_blueprint(main)
    return app


# 创建应用实例
app = create_app()
