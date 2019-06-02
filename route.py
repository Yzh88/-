from flask import render_template
from db import *


@app.route('/attendance')
def attendance_views():
    pres = Pers_details.query.all()
    return render_template("attendance.html", pres=pres)


if __name__ == '__main__':
    manager.run()
