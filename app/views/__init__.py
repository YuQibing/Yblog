from .user import user
from .main import main

# 蓝本的配置
DEFAULT_BLUEPRINT = (
    # 蓝本名字 蓝本前缀
    (user, '/user'),
    (main, '/main'),
)


# 注册蓝本
def config_blueprint(app):
    for blueprint_name, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint_name, url_prefix=url_prefix)
