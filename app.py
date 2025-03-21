import traceback

from flask import Flask
import config
from blueprints.qa import qa
from blueprints.auth import auth
from models import UserModel

from exts import db
from flask_migrate import Migrate

app = Flask(__name__)
# 导入自定义配置
app.config.from_object(config)
# 数据库初始化
db.init_app(app)


# 数据库迁移
migrate = Migrate(app, db)
# 蓝图注册
app.register_blueprint(qa)
app.register_blueprint(auth)

# 蓝图  电影模块，音乐模块，读书模块
if __name__ == '__main__':
    app.run()