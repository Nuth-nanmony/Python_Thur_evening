#write a py program to create a table named students with 

import pyodbc

path="Final-Exam/Part1/school.accdb"

db= (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={path};"
)

try:
    conn=pyodbc.connect(db)
    cursor=conn.cursor()

    create_table = """
    CREATE TABLE Students (
        StudentID AUTOINCREMENT PRIMARY KEY,
        Name TEXT(50),
        Age INTEGER,
        Course TEXT(50)
    )
    """

    cursor.execute(create_table)
    conn.commit()

    print("Students table created successfully")

except pyodbc.Error as e:
    print("Error creating table")
    print(e)
conn.close()