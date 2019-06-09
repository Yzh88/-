from flask import Flask,render_template, request,session,make_response

# 创建Flask的程序实例
app = Flask(__name__)



@app.route("/login")
@app.route('/',methods=['GET',"POST"])
@app.route("/login",methods=['GET',"POST"])
def show_form():
    flas = False
    if request.method=="GET":

        return render_template('login.html',params=locals())

    else:
        uname = request.form['uname']
        pswd = request.form["pswd"]
        if uname == 'ljl' and pswd=="123456":
            resp = render_template("main.html")
            if "remember_pwd" in request.form:
                resp.set_cookie('uname',uname,60*60*24)
                resp.set_cookie('pswd',pswd,60*60*24)
            return resp

        else:
            flas = True
            return render_template("login.html",params=locals())




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

@app.route('/register')
@app.route('/register.html')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
