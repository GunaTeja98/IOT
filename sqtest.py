import pymysql
import datetime

db = pymysql.connect(host="localhost",user="root",password="qwerty",db="basic")

try:
	with db.cursor() as cursor:
		value = 21.0
		query = "Insert into readings(tstamp,sensortype, sensorID,value) values(%s,%s,%s,%s)"
		values=(datetime.date.today(),"BME680",1,21.0)
		cursor.execute(query, values)
		db.commit()
except Exception as e:
	print(e) 
