#Write a python program to insert new students record

import pyodbc

path="Final-Exam/Part1/school.accdb"

db= (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={path};"
)

try:
    conn=pyodbc.connect(db)
    cursor=conn.cursor()

    name=input("Enter your name: ")
    #ID auto insert
    age=int(input("Enter your age: "))
    course=input("Enter course: ")
    insert_table= "INSERT INTO students (Name,Age,Course) VALUES (?,?,?)"
    cursor.execute(insert_table,(name,age,course))
    conn.commit()

    print("Students insert successfully")

except pyodbc.Error as e:
    print("Error insert record")
    print(e)
conn.close()