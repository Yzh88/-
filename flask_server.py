from flask import Flask,render_template, request
# 创建Flask的程序实例
app = Flask(__name__)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable = False,unique = True,index = True)
    age = db.Column(db.Integer,nullable=True)
    email = db.Column(db.String(120),unique=True)
    #增加一个列isAcive
    isActive =db.Column(db.Boolean,default=True)
    birthday = db.Column(db.Date)
    def __repr__(self):
        return "<%d,%s,%s,%s,%s>"%(self.id,self.username,self.age,self.email,self.birthday)




@app.route('/')
def show_form():
    return render_template('login.html')


@app.route('/main', methods=['GET', 'POST'])
@app.route('/main.html', methods=['GET', 'POST'])
def main_page():

    username = request.form.get('uname')
    password = request.form.get('pswd')
    print(username, password)
    return  render_template('main.html')

@app.route('/recruit')
@app.route('/recruit.html')
def recruit():

    return render_template('recruit.html',params=locals())

@app.route('/attendance')
@app.route('/attendance.html')
def attendance():
    return render_template('attendance.html')

@app.route('/notice')
@app.route('/notice.html')
def notice():
    return render_template('notice.html')

@app.route('/update')
def update():
    pageCount = 5  # 每页显示的记录的数量
    pageCurrent = request.args.get('pageCurrent', 1)  # 当前想看的页数
    if pageCurrent == '':
        pageCurrent = 1
    pageCurrent = int(pageCurrent)
    pages = math.ceil(db.session.query(Users).count() / 5)
    if pageCurrent >= pages:
        pageCurrent = pages
    elif pageCurrent <= 0:
        pageCurrent = 1

    ost = (pageCurrent - 1) * pageCount  # 1、计算要跳过多少条数据
    users = db.session.query(Users).offset(ost).limit(pageCount).all()  # 2、查询对应的数据
    # 判断是否有kw参数传递到视图中
    if 'kw' in request.args:
        kw = str(request.args['kw'])
        if kw != '':
            users = db.session.query(Users).filter(
                or_(
                    Users.username.like('%' + kw + '%'),
                    Users.email.like('%' + kw + '%')
                )
            )
            pages = math.ceil(users.count() / 5)
            users = users.offset(ost).limit(pageCount).all()
            kws = 1

    return render_template("01-update.html", params=locals())


if __name__ == '__main__':
    app.run(debug=True)
