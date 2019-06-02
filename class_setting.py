from flask_server import *
class TempBase(db.Model):  # 应聘人员 基本 信息
    __tablename__ = 'temp_base'
    num = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    tel = db.Column(db.String(32))
    birthday = db.Column(db.String(32))
    sex = db.Column(db.String(32))
    native = db.Column(db.String(32))
    education = db.Column(db.String(32))
    want_job = db.Column(db.String(32))
    hope_wage = db.Column(db.Float)
    apply_time = db.Column(db.DateTime)

class TempDetails(db.Model):  # 应聘人员 详情 表
    __tablename__ = 'temp_details'
    num = db.Column(db.Integer,primary_key=True)
    hobby = db.Column(db.String(1024))
    speciality = db.Column(db.String(1024))
    graduation = db.Column(db.String(1024))
    training = db.Column(db.String(1024))
    career = db.Column(db.String(1024))

class PersBase(db.Model):  # 正式职员 基本 信息表
    __tablename__ = 'pers_base'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    tel = db.Column(db.String(32))
    birthday = db.Column(db.String(32))
    sex = db.Column(db.String(32))
    department = db.Column(db.String(32))
    job = db.Column(db.String(32))
    base_salary = db.Column(db.Float)
    performance = db.Column(db.Float)

class PersDetails(db.Model):  # 职员 详细 信息表
    id = db.Column(db.Integer,primary_key=True)
    hiretime = db.Column(db.DateTime)
    departure_date = db.Column(db.DateTime)
    email = db.Column(db.String(64))
    wechat = db.Column(db.String(50))
    qq = db.Column(db.String(32))
    emergency_contact = db.Column(db.String(32))
    contact_tel = db.Column(db.String(32))
    hobby = db.Column(db.String(1024))
    speciality = db.Column(db.String(1024))
    graduation = db.Column(db.String(1024))
    training = db.Column(db.String(1024))
    career = db.Column(db.String(1024))

class EnterpriseDate(db.Model):  # 企业基本信息表
    __tablename__ = 'enterprise_base'
    registration_no = db.Column(db.String(64),primary_key=True)
    enterprise_name = db.Column(db.String(64))
    enterprise_type = db.Column(db.String(32))
    address = db.Column(db.String(64))
    ceo = db.Column(db.String(16))
    ceo_id = db.Column(db.String(64))
    password = db.Column(db.String(40))




















