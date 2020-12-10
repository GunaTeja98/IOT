import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host="localhost",user="root",password="qwerty",db="basic")

    sql_select_Query = "select * from readings"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in BME680 readings are: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        print("tstamp = ", row[0], )
        print("sensortype = ", row[1])
        print("sensorID  = ", row[2])
        print("value  = ", row[3], "*C \n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
