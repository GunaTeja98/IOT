import pandas as pd
import pymysql 



datab = pymysql.connect(host="localhost",user="root",password="qwerty",db="basic")

sql_query = pd.read_sql_query(''' 
                              select * from basic.readings
                              '''
                              ,datab) # here, the 'db' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_csv (r'/home/pi/bme_data.csv', index = False) # place 'r' before the path name to avoid any errors in the path
