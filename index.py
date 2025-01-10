from app import create_app

# 创建应用实例
app = create_app()

# Vercel 需要这个入口
app.debug = False


# 处理 WSGI 请求
def handler(event, context):
    return app(event, context)
