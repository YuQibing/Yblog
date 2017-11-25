from PIL import Image
from flask import Blueprint
from flask import make_response
from flask import redirect
from flask import request
from flask import session
import base64

from flask_login import current_user
from flask_login import login_user

from app import checkcode
from flask import url_for
from app.email import send_mail
import os
import random
from flask import current_app
from flask import flash
from app.extensions import photos, db
from app.models import User
from flask import render_template
from app.forms import Register, Login

# 创建一个蓝本
user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    verify_code = form.verifyCode.data
    u = User.query.filter_by(username=form.username.data).first()
    if not form.validate_on_submit():
        print('errors', form.errors)
    if form.validate_on_submit():
        if u:
            if u.verify_password(form.password.data):
                print(session['verifyCode'])
                if session['verifyCode'] != verify_code and 'verify_code' in session:
                    flash('验证码错误')
                else:
                    #  用户登录
                    login_user(u, remember=form.username.data)
                    return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash('无效密码')
        else:
            flash('无效用户名')
            current_user.is_authenticated
    return render_template('user/login.html', form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        verify_code = form.verify_code.data
        username = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        print(verify_code)
        if username:
            flash('该账户已经注册')
        if email:
            flash('该邮箱已经绑定，请换一个')
        if 'verify_code' in session and session['verifyCode'] != verify_code:
            flash('验证码错误')
        else:
            flash('验证码正确')
            # 获取上传文件的后缀
            suffix = os.path.splitext(form.icon.data.filename)[1]
            # 生成新的头像名字
            name = randStr() + suffix
            photos.save(form.icon.data, name=name)
            # 在指定路径生成文件
            pathName = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], name)
            # 打开文件
            img = Image.open(pathName)
            #  设置尺寸
            img.thumbnail((64, 64))
            #  保存缩略图
            img.save(pathName)
            # 创建用户
            u = User(username=form.username.data, password=form.password.data, email=form.email.data, icon=name)
            # 保存数据到数据库
            db.session.add(u)
            # 手动提交到数据库
            db.session.commit()
            # 发送激活邮件到邮箱
            token = u.generate_activate_token()
            send_mail(form.email.data, '账户激活', 'email/activate', token=token, username=form.username.data)
            flash('激活邮件已发送，请激活')
            return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)


@user.route('/Verify/')
def verifyCode():
    img, text = checkcode.generate_verification_code()
    session['verifyCode'] = text
    response = make_response(img)
    response.headers['Content-Type'] = 'image/jpeg'
    return response


@user.route('/activate/<token>')
def activate(token):
    if User.check_activate_token(token):
        flash('激活成功')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败')
        return redirect(url_for('main.index'))


# 生成随机的字符串 用来作为 图片的名字
def randStr(length=32):
    baseStr = 'asdfjlkuio12355oywerwer'
    newStr = ''.join([random.choice(baseStr) for i in range(length)])
    return newStr
