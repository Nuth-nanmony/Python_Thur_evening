# Explain how python connect to MS access db
"""
    Python connect to MS Access database by using ODBC
    ODBC uses as bridge
    By sending command from Python to MS Accesss
"""

import pyodbc

path="Final-Exam/Part1/school.accdb"

db= (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={path};"
)

try:
    conn=pyodbc.connect(db)
    print("Connected to Microsoft Access successfully")

except pyodbc.Error as e:
    print("Failed to connect to Microsoft Access")
    print("Error:", e)