from flask import Flask


# 封装一个对外公开的方法，专门用于创建Flask对象
def create_app(config):
    # 创建一个应用实例
    app = Flask(__name__)
    app.config
    return app
