from flask_mail import Message
from app.extensions import mail
from flask import current_app, render_template
from threading import Thread


def async_send_mail(app, msg):
    # 邮件发送需要诚信上下文，否则发送不了
    # 由于是新的线程，没有上下文，需要手动创建
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    # 获取原生的app对象
    app = current_app._get_current_object()
    sender = current_app.config['MAIL_USERNAME']
    msg = Message(subject=subject, recipients=[to], sender=sender)
    # 网页接收内容
    msg.html = render_template(template + '.html', **kwargs)
    # 终端接收内容
    msg.body = render_template(template + '.txt', **kwargs)
    thr = Thread(target=async_send_mail, args=[app, msg])
    thr.start()
    return thr
