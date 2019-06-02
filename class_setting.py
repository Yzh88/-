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

"""
 IP：176.221.17.11
临时人员基本信息表temp_base，用来存放应聘人员基本信息
序号num 姓名name 电话tel 生日birthday 性别 sex
籍贯native学历education
申请职位want_job期望薪资hope_wage
申请时间apply_time审核状态status

create table temp_base(
   num int(16) auto_increment PRIMARY KEY,
   name varchar(32),
   tel varchar(32),
   birthday varchar(32),
   sex varchar(32),
   native varchar(32),
   education varchar(32),
   want_job varchar(32),
   hope_wage DECIMAL(16,2),
   apply_time datetime,
   status int)default charset=utf8;

insert into temp_base values (null,"张三","15800000000","20000502","男","汉","研究生","总经理","5000","20180801",1),
(null,"李四","15800000001","20000503","女","毛南","本科","董事长","6000","20180205",2);


临时人员详情表temp_details，用来存放应聘人员详细信息
序号num 兴趣爱好hobby 特长speciality  毕业院校graduation
培训经历training 工作经历 career

create table temp_details(
    id  int(16) auto_increment PRIMARY KEY,
    hobby varchar(64),
    speciality varchar(64),
    graduation varchar(32),
    training varchar(256),
    career varchar(1024)
)default charset=utf8;

insert into temp_details values
(null,"下棋","打球","重大","无","无"),
(null,"开车","游泳","西南大学","无","无"),
(null,"跑步","走路","北京大学","无","无"),
(null,"下棋","打球","重大","无","无"),
(null,"开车","游泳","西南大学","无","无"),
(null,"跑步","走路","北京大学","无","无");


职员基本信息表pers_base,用来存放在职职员基本信息
工号id 姓名name 电话tel生日birthday 性别sex
部门department 职位job 基本工资base_salary 绩效评定performance

create table pers_base(
    id varchar(32) PRIMARY KEY,
    name varchar(32),
    tel varchar(32),
   birthday varchar(32),
   sex varchar(32),
   department varchar(32),
   job varchar(32),
   base_salary DECIMAL(16,2),
   performance DECIMAL(16,2)
)default charset=utf8;


职员详情表pers_details,用来存放在职员基本信息的补充信息（详细信息）
工号id 入职时间hiredate 离职时间departure_date
邮箱email 微信wechat  QQ qq
应急联系人(配偶父母直系亲属)emergency_contact   电话contact_tel
兴趣爱好hobby 特长speciality  毕业院校graduation
培训经历training 工作经历 career

create table pers_details(
    id varchar(32) PRIMARY KEY,
    hiredate datetime,
    departure_date datetime,
    email varchar(50),
    wechat varchar(50),
    qq varchar(32),
    emergency_contact varchar(32),
    contact_tel varchar(32),
    hobby varchar(64),
    speciality varchar(64),
    graduation varchar(32),
    training varchar(256),
    career varchar(1024)
)default charset=utf8;


1） 企业信息库enterprise_date: 用来存放注册企业的基本信息
  企业基本信息表enterprise_base
统一社会信用代码registration_no
企业名称enterprise_name
企业类型enterprise_type
住　　所address
法定代表人ceo
法定代表人身份证号码 ceo_id
登录密码 password

企业信息库enterprise_date:
create table enterprise_base(
    registration_no varchar(64),
    enterprise_name varchar(64),
    enterprise_type varchar(32),
    address varchar(64),
    ceo varchar(16),
    ceo_id varchar(64),
    password varchar(40)
)default charset=utf8;
测试：

插入数据：
insert into enterprise_base values(
   '9150010000X','宇宙航母科技有限公司','有限责任公司',
   '重庆市解放碑50号','张三','50001111','null'
)
"""


















