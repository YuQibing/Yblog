from flask import Blueprint
from app.models import User
from flask import render_template
from app.forms import Register

# 创建一个蓝本
user = Blueprint('user', __name__)


@user.route('/login')
def login():
    return render_template('main/index.html')


@user.route('/register')
def register():
    form = Register()
    return render_template('user/register.html', form=form)
