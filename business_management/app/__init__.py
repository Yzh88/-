# 主要工作
# 1.构建Flask的应用实例以及各种配置
# 2.创建SQLAlchemy的应用实例
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/blog"
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "hello word"
    db.init_app(app)
    from .topic import tbp as topic_blueprint
    app.register_blueprint(topic_blueprint)
    from .users import ubp as users_blueprint
    app.register_blueprint(users_blueprint)
    return app