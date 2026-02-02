#miniporject, Inventory Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB5_HOST"),
    user=os.getenv("DB5_USER"),
    password=os.getenv("DB5_PASSWORD"),
    database=os.getenv("DB5_NAME"),
)
cursor = db.cursor()