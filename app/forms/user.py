from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FileField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask.ext.wtf.file import FileRequired, FileAllowed
from app.extensions import photos
from app.models import User


# 定义一个注册类
class Register(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(6, 10, message='长度为6到10个字符之间')])
    password = PasswordField('密码', validators=[DataRequired, Length(6, 10, message='密码必须是6到10位字符')])
    password_confirm = PasswordField('确认密码', validators=[EqualTo(password, message='两次输入密码不同')])
    email = StringField('邮箱', validators=[Email(message='请输入正确到邮箱地址')])
    icon = FileField('头像', validators=[FileRequired('请选择上传的头像'), FileAllowed(photos, message='只能上传图片')])
    submit = SubmitField('立即注册')

    # 自定义表单验证
    def validate_username(self, field):
        user = User.query.filter_by(username=field.username)
        if user.first():
            # raise 是引发异常 后面跟error名称
            raise ValidationError('该用户已存在')

    def validate_email(self, field):
        email = User.query.filter_by(email=field.email)
        if email.first():
            raise ValidationError('该邮箱已被注册')