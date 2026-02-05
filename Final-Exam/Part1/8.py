#write a program that Update and delete

import pyodbc

path="Final-Exam/Part1/school.accdb"

db= (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={path};"
)

conn=pyodbc.connect(db)
cursor=conn.cursor()

def update():
    student_id=int(input("Enter ID to update: "))
    new_course=input("Enter course to update: ")
    cursor.execute(
        "UPDATE Students SET Course=? WHERE StudentID=?",
        (new_course,student_id)
    )
    conn.commit()
    print(f"StudentID {student_id} course has been updated to {new_course}")
    
def delete():
    sid=int(input("Enter ID to delte: "))
    cursor.execute(
        "DELETE FROM Students WHERE StudentID=?",
        (sid,)
    )
    conn.commit()
    
conn.close()