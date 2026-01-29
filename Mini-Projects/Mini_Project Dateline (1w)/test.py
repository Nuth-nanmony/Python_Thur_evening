import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Nimoinmysql123@",
    database="library_db",
    port=3306
)

print("MYSQL CONNECTED SUCCESSFULLY")
