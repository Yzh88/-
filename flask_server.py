from flask import Flask, render_template, request

# 创建Flask的程序实例
app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('login.html')


@app.route('/main', methods=['GET', 'POST'])
@app.route('/main.html', methods=['GET', 'POST'])
def main_page():
    username = request.form.get('uname')
    password = request.form.get('pswd')
    print(username, password)
    return render_template('main.html')


@app.route('/recruit')
@app.route('/recruit.html')
def recruit():
    return render_template('recruit.html')


@app.route('/attendance')
@app.route('/attendance.html')
def attendance():
    return render_template('attendance.html')


@app.route('/notice')
@app.route('/notice.html')
def notice():
    return render_template('notice.html')


if __name__ == '__main__':
    app.run(debug=True)
