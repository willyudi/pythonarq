
import pymysql

db = pymysql.connect(host='Wiliano.mysql.pythonanywhere-services.com', user='wiliano', passwd='willy01', db='Wiliano$db_liberdadeccb', charset='utf8', use_unicode=True)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version? %s " % data)
db.close()
