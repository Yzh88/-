from flask import Flask, render_template, request

# 创建Flask的程序实例
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def show_form():
    if request.method == "GET":
        return render_template('login.html')
    else:
        uname = request.form["uname"]
        upwd = request.form["pswd"]
        # remember_pwd=False
        # if "remember_pwd" in request.form:
        #     remember_pwd=True
        # if remember_pwd:
        #     pass

        if uname == "admin" and upwd == "admin":
            return "登录成功"
        else:
            return "<script>alert('登录失败‘);location.href='/';</script>"


if __name__ == '__main__':
    app.run(debug=True)
