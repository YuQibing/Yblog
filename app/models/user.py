from flask import current_app
from app.extensions import db
# 导入密码散列和校验
from werkzeug.security import generate_password_hash, check_password_hash
# 生成token所使用到到类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#  用户状态的使用需要实现几个回调函数，UserMixin类已经做了实现
from flask_login import UserMixin
from app.extensions import login_manager


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(150))
    email = db.Column(db.String(40), unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    icon = db.Column(db.String(100), default='')

    # 保护密码字段
    @property
    def password(self):
        # raise 是引发异常 后面跟error名称
        raise AttributeError('密码不可读')

    # 设置密码
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 密码验证
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 生成用户验证token
    def generate_activate_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id})

    # 账户激活
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        user = User.query.get(data.get('id'))
        if user is None:
            #  不存在此用户
            return False
        if not user.confirmed:
            #  若没有激活 激活账户
            user.confirmed = True
            db.session.add(user)
        return True


# 登录认证回调
@login_manager.user_loader
def loader_user(user_id):
    user = User.query.get(int(user_id))
    return user
