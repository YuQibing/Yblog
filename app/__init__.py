from flask import Flask
from app.config import config
from app.views import config_blueprint
from app.extensions import config_extensions


# 封装一个对外公开的方法，专门用于创建Flask对象
def create_app(config_name):
    # 创建一个应用实例
    app = Flask(__name__)
    # 初始化配置
    app.config.from_object(config[config_name])
    # 调用初始化函数
    config[config_name].init_app(app)
    # 初始化扩展
    config_extensions(app)
    # 初始化蓝本
    config_blueprint(app)
    return app
