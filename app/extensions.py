# 导入相关类库、扩展库
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate
from flask_uploads import configure_uploads, patch_request_class
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES

# 创建相关对象
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
migrate = Migrate(db=db)
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)


# 完成相关对象的初始化
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, photos)

    # 指定上传文件的大小
    # 如果设置是None值 则会从app.config中get('MAX_CONTENT_LENGTH')
    patch_request_class(app, size=None)
    # 当访问一些必须登录之后才能访问当路由会提示
    login_manager.login_message = '登录后才能访问'
    # 指定登录的视图函数
    login_manager.login_view = 'user.login'
    # 设置登录的session保护等级
    login_manager.session_protection = 'strong'
