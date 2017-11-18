import os
from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

# 设置配置文件名字
config_name = os.environ.get('CONFIG') or 'default'

# 调用create_app()方法创建一个实例app
app = create_app(config_name)

# 用manager来管理app
manager = Manager(app)

# 添加终端管理
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
