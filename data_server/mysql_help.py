from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from config.data_config import *


def create_db():
    return "test"


name = create_db()
con = pymysql.connect(HOST, USER, SQL_PWD)
cur = con.cursor()
cur.execute(f"create database {name} character set utf8;")
cur.close()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{USER}:{SQL_PWD}@{HOST}:{SQL_PORT}/{name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 查询时会显示原始SQL语句
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


class Enterprise_base(db.Model):
    registration_no = db.Column(db.String(32), primary_key=True)
    enterprise_name = db.Column(db.String(128), unique=True)
    enterprise_type = db.Column(db.String(64), unique=True)
    address = db.Column(db.String(128), unique=True)
    ceo = db.Column(db.String(64), unique=True)
    ceo_id = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)

    def __init__(self, **kwargs):
        self.registration_no = kwargs["registration_no"]
        self.enterprise_name = kwargs["enterprise_name"]
        self.enterprise_type = kwargs["enterprise_type"]
        self.address = kwargs["address"]
        self.ceo = kwargs["ceo"]
        self.ceo_id = kwargs["ceo_id"]
        self.password = kwargs["password"]

    # repr()方法显示一个可读字符串

    def __repr__(self):
        return f'Enterprise_base {self.enterprise_name}'


if __name__ == "__main__":
    create_db()
    db.create_all()
