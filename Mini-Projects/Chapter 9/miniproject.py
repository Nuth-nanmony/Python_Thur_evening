#miniproject student management system (deadline3)

import mysql.connector
import csv

db = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="student_db"
)

cursor = db.cursor()

def add_student():
    id=input("ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("Course: ")
    gpa = float(input("GPA: "))
    cursor.execute(
        "INSERT INTO students (id,name,age,course,gpa) VALUES (%s,%s,%s,%s,%s)",
        (id,name, age, course, gpa)
    )
    db.commit()

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def search_student():
    name = input("Search name: ")
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE %s",
        ("%" + name + "%",)
    )
    for row in cursor.fetchall():
        print(row)

def update_student():
    sid = input("ID: ")
    course = input("New course: ")
    gpa = float(input("New GPA: "))
    cursor.execute(
        "UPDATE students SET course=%s, gpa=%s WHERE id=%s",
        (course, gpa, sid)
    )
    db.commit()

def delete_student():
    sid = input("ID: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    db.commit()

def sort_students():
    print("1.Sort by name 2.Sort by course")
    c = input("Choose: ")
    if c == "1":
        cursor.execute("SELECT * FROM students ORDER BY name")
    elif c == "2":
        cursor.execute("SELECT * FROM students ORDER BY course")
    for row in cursor.fetchall():
        print(row)

def export_csv():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","name","age","course","gpa"])
        writer.writerows(rows)

def main():
    while True:
        print("1.Add 2.View 3.Search 4.Update 5.Delete 6.Sort 7.ExportCSV 8.Exit")
        c = input("Choose: ")
        if c == "1":
            add_student()
        elif c == "2":
            view_students()
        elif c == "3":
            search_student()
        elif c == "4":
            update_student()
        elif c == "5":
            delete_student()
        elif c == "6":
            sort_students()
        elif c == "7":
            export_csv()
        elif c == "8":
            break
if __name__=="__main__":
    main()
cursor.close()
db.close()