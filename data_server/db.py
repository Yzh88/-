from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import pymysql
from config.data_config import *

pymysql.install_as_MySQLdb()
con = pymysql.connect(HOST, USER, SQL_PWD)
cur = con.cursor()
try:
    cur.execute(f"create database {NAME} character set utf8 collate utf8_general_ci;")
    cur.close()
except pymysql.err.ProgrammingError:
    pass
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{USER}:{SQL_PWD}@{HOST}:{SQL_PORT}/{NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = DEBUG
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


class Pers_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    section = db.Column(db.String(16))
    postion = db.Column(db.String(16))
    tel = db.Column(db.String(16))
    birthday = db.Column(db.Date)
    sex = db.Column(db.String(8))
    native = db.Column(db.String(16))
    education = db.Column(db.String(16))
    graduation = db.Column(db.String(64))
    hiredate = db.Column(db.DateTime)
    departure_date = db.Column(db.DateTime)
    email = db.Column(db.String(64))
    wechat = db.Column(db.String(32))
    qq = db.Column(db.String(16))
    emergency_contact = db.Column(db.String(32))
    contact_tel = db.Column(db.String(16))
    hobby = db.Column(db.String(128))
    speciality = db.Column(db.String(128))
    training = db.Column(db.String(1024 * 3))
    career = db.Column(db.String(1024 * 5))
    signin_time = db.Column(db.DateTime)
    signout_time = db.Column(db.DateTime)
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"))
    status = db.Column(db.String(16))
    is_astive = db.Column(db.String(8), default=True)


if __name__ == "__main__":
    manager.run()
