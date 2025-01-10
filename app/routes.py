from flask import Blueprint, render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.ai_matcher import generate_matched_resume
from random import choice
from app.utils.slogans import SLOGANS

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    slogan = choice(SLOGANS)
    return render_template("index.html", slogan=slogan)


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
                    # 直接从内存中读取文件，不保存到磁盘
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
            # 生成匹配结果（现在返回包含多个部分的字典）
            result = generate_matched_resume(resume_texts, jd_text)
            return jsonify(result)  # 直接返回包含所有分析结果的字典
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
