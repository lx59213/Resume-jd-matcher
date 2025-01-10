from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    # 基本配置
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")
    app.config["ALLOWED_EXTENSIONS"] = {"pdf"}

    # 注册蓝图
    from index import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app


# 创建应用实例
app = create_app()
