#miniporject, Course Registration System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB3_HOST"),
    user=os.getenv("DB3_USER"),
    password=os.getenv("DB3_PASSWORD"),
    database=os.getenv("DB3_NAME"),
)
cursor = db.cursor()