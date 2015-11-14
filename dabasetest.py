
import pymysql

db = pymysql.connect('Wiliano.mysql.pythonanywhere-services.com','Williano', 'liberdadeccb','db_liberdadeccb')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version? %s " % data)
db.close()
