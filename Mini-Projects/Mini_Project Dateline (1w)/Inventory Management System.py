#miniporject, Inventory Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB4_HOST"),
    user=os.getenv("DB4_USER"),
    password=os.getenv("DB4_PASSWORD"),
    database=os.getenv("DB4_NAME"),
)
cursor = db.cursor()
