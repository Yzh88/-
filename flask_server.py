from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sqlalchemy import or_, func

import math

# 创建Flask的程序实例
app = Flask(__name__)
#连接到MySQL中flaskDB数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/personnel_management"

# app.config['host'] = '0.0.0.0'
#指定不需要信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#指定程序的启动模式为调试模式
app.config['DEBUG'] = True
#指定执行完增删改之后的自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#创建SQLAlchemy的实例
db = SQLAlchemy(app)

#创建Manager对象并指定要管理的app
manager = Manager(app)
#创建Migrate对象,并指定关联的app和db
migrate = Migrate(app,db)
#为manager增加数据库的迁移指令
#为manager增加一个子命令-db(自定义),具体操作由MigrateCommand来提供
manager.add_command('db',MigrateCommand)


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
    status = db.Column(db.Boolean,default=False)

class TempDetails(db.Model):  # 应聘人员 详情 表
    __tablename__ = 'temp_details'
    id = db.Column(db.Integer,primary_key=True)
    hobby = db.Column(db.String(100))
    speciality = db.Column(db.String(100))
    graduation = db.Column(db.String(100))
    training = db.Column(db.String(100))
    career = db.Column(db.String(100))

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
    enterprise_name = db.Column(db.String(64),nullable=False)
    enterprise_type = db.Column(db.String(32),nullable=False)
    address = db.Column(db.String(64),nullable=False)
    ceo = db.Column(db.String(16),nullable=False)
    ceo_id = db.Column(db.String(64),nullable=False)
    password = db.Column(db.String(40),nullable=False)

@app.route('/add_data')
def add_data():
    temp_details = TempDetails()
    # temp_details.id = 1
    temp_details.hobby = '下棋，游泳......'
    temp_details.speciality = 'LOL'
    temp_details.graduation = 'Tarena'
    temp_details.training = 'python,mysql...'
    temp_details.career = '在××实习...'
    db.session.add(temp_details)
    return '1'

@app.route('/',methods=['GET', 'POST'])
def show_first_page():
    flag = 0
    if request.method == 'GET':

        return render_template('login.html',params=locals())
    else:

        username = request.form.get('registration_no')
        password = request.form.get('password')
        users = db.session.query(EnterpriseDate).all()
        for user in users:
            if username in user.registration_no:
                if password in user.password:
                    print(user.registration_no, user.password)
                    return render_template('main.html')
        else:
            flag = 1
            return render_template('login.html',params=locals())  # 账号不存在 render_template('/')


@app.route('/register',methods=['GET', 'POST'])
def show_register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        enterprise = EnterpriseDate()
        enterprise.registration_no = request.form.get('registration_no')
        enterprise.enterprise_name = request.form.get('enterprise_name')
        enterprise.enterprise_type = request.form.get('enterprise_type')
        enterprise.address = request.form.get('address')
        enterprise.ceo = request.form.get('ceo')
        enterprise.ceo_id = 1
        enterprise.password = request.form.get('password')
        db.session.add(enterprise)

        flag = 2
        return render_template('login.html',params=locals())


@app.route('/main', methods=['GET', 'POST'])
@app.route('/main.html', methods=['GET', 'POST'])
def main_page():

    return render_template('main.html')


@app.route('/recruit')
@app.route('/recruit.html')
def recruit():
    pageSize = 5
    currentPage = int(request.args.get('currentPage',1))
    ost = (currentPage-1)*pageSize
    temp_bases = db.session.query(TempBase).offset(ost).limit(pageSize).all()
    totalSize_bases = db.session.query(TempBase).count()
    lastPage_bases = math.ceil(totalSize_bases/pageSize)
    prevPage_bases = 1
    if currentPage > 1:
        prevPage_bases = currentPage - 1
    nextPage_bases = lastPage_bases
    if currentPage < lastPage_bases:
        nextPage_bases = currentPage + 1

    pageSize_d = 5
    currentPage_d = int(request.args.get('currentPage_d', 1))
    ost_d = (currentPage_d - 1) * pageSize_d
    temp_details = db.session.query(TempDetails).offset(ost_d).limit(pageSize_d).all()
    totalSize_details = db.session.query(TempDetails).count()
    lastPage_details = math.ceil(totalSize_details / pageSize_d)
    prevPage_details = 1
    if currentPage_d > 1:
        prevPage_details = currentPage_d - 1
    nextPage_details = lastPage_details
    if currentPage_d < lastPage_details:
        nextPage_details = currentPage_d + 1

    return render_template('recruit.html',params=locals())


@app.route('/attendance')
@app.route('/attendance.html')
def attendance():
    return render_template('attendance.html',params=locals())

@app.route('/notice')
@app.route('/notice.html')
def notice():
    return render_template('notice.html')

@app.route("/staff_view")
def staff_view():
    return render_template('staff-view.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    # manager.run()
