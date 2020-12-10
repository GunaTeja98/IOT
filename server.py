from flask import Flask
import pymysql

app=Flask(__name__)
db = pymysql.connect(host="localhost",user="root",password="qwerty",db="basic")

@app.route("/")
def index():
    with db.cursor() as cursor:
        cursor.execute("select * from readings")
        data = cursor.fetchall()
        results = []
        response = "<body>"
        for row in data:
            for d in row:
                response+=" "
                response+=str(d)
            response+="<br>"
        response+="</body>"
        return response

if __name__ == '__main__':
    app.run()
    