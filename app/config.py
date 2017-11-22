import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 设置基类
class Config:
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'happy123happy'
    # 配置数据库
    # 每次执行完成后自动提交到数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 数据库关闭警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 设置邮件
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp:163.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '18395960686@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'zhangchi1204'
    # 设置图片大小
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    # 设置图片路径
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'static/upload')

    @staticmethod
    def init_app(app):
        pass


# 配置Sqlite数据库
class SqlDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'web-dev.sqlite')


class SqlTestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'web-test.sqlite')


class SqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'web.sqlite')


# 配置mysql数据库

class MysqlDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/db?charset=ut8'


class MysqlTestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/db?charset=ut8'


class MysqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/db?charset=ut8'

config = {
    'sqldevconfig': SqlDevelopmentConfig,
    'sqltesconfig': SqlTestConfig,
    'sqlconfig': SqlConfig,
    'mysqldevconfig': MysqlDevelopmentConfig,
    'mysqltestconfig': MysqlTestConfig,
    'mysqlconfig': MysqlConfig,
    'default': SqlDevelopmentConfig
}