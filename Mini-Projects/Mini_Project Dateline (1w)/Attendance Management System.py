#Mini project, 

import mysql.connector
import csv

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="student_db"
)

cursor = db.cursor()