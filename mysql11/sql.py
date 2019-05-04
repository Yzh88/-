import pymysql

sql = "select * from stu where id='s00001'"
db = pymysql.connect("localhost", "root", "123456", "stu")

cursor = db.cursor()
