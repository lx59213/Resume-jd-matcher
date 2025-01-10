from flask import Flask, jsonify
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.routes import main

    app.register_blueprint(main)

    # 添加全局错误处理
    @app.errorhandler(Exception)
    def handle_error(error):
        return jsonify({"error": str(error)}), 500

    return app


# 创建应用实例供 Vercel 使用
app = create_app()

# 确保导出 app 变量
if __name__ == "__main__":
    app.run()
