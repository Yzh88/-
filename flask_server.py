from flask import render_template, request
from data_server.db import *


@app.route('/attendance')
def show_form():
    pres = Pers_details()
    return render_template("attendance.html", pres=pres)


if __name__ == '__main__':
    manager.run()
