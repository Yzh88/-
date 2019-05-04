# 连接数据库

import pymysql

db = pymysql.connect("localhost", "root", "123456", "datamanner")
cursor = db.cursor()
