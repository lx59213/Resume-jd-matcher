from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册蓝图
    from app.routes import main

    app.register_blueprint(main)

    return app


# 创建应用实例供 Vercel 使用
app = create_app()
