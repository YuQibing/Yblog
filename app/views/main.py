from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)


@main.route('/index')
def index():
    return render_template('main/index.html')
