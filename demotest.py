import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    database="basic"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
    
#mycursor.execute("CREATE TABLE readings(tstamp DATETIME, sensortype VARCHAR(64), sensorID INT, value FLOAT)")

