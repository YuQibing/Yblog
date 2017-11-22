from flask import Blueprint
from app.models import User
from flask import render_template
from app.forms import Register, Login

# 创建一个蓝本
user = Blueprint('user', __name__)


@user.route('/login')
def login():
    form = Login()
    return render_template('user/login.html', form=form)


@user.route('/register')
def register():
    form = Register()
    return render_template('user/register.html', form=form)
