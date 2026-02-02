#miniporject, Attendance Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB2_HOST"),
    user=os.getenv("DB2_USER"),
    password=os.getenv("DB2_PASSWORD"),
    database=os.getenv("DB2_NAME"),
)
cursor = db.cursor()