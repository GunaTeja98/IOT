import serial
import pymysql
import time
from datetime import datetime

ser = serial.Serial('/dev/ttyUSB0',115200)
db = pymysql.connect(host="localhost",user="root",password="qwerty",db="basic")

while(True):
	line = str(ser.readline())[55:-6]
	print(line)
	try:
		with db.cursor() as cursor:
			val = float(line)
			now = datetime.now()
			query = "Insert into readings(tstamp, sensortype, sensorID, value) values(%s,%s,%s,%s)"
			valu=(now,"BME680",1,val)
			cursor.execute(query, valu)
			db.commit()
	except Exception as e:
		print(e) 
