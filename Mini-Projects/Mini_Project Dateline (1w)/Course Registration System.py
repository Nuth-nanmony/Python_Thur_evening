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

# add
def add_course():
    print("\n--Add Course Program--")
    name=input("Course Name: ")
    instruc=input("Instructor name: ")
    credit=int(input("Credits: "))

    cursor.execute(
        "INSERT INTO courses (course_name, instructor, credits) VALUES (%s,%s,%s)",
        (name,instruc,credit)
    )
    db.commit()
    print("Successfully added course.")

#register
def register():
    print("--Register Student--")
    student=input("Student Name: ")
    cursor.execute("SELECT * FROM courses")
    courses=cursor.fetchall()

    if not courses:
        print("No courses available.")
        return
    
    print("\nAvailable Courses:")
    for s in courses:
        print(f"{s[0]} - {s[1]} ({s[2]})") 
    course_id=int(input("Enter Course ID: "))
    cursor.execute(
        "INSERT INTO registrations (student_name, course_id) VALUES (%s,%s)",
        (student,course_id)
    )
    db.commit()
    print("Student registered successfully")

# View
def view_registrations():
    cursor.execute(
        """SELECT r.id, r.student_name, c.course_name 
        FROM registrations r
        JOIN courses c ON r.course_id=c.id"""
    )
    rows=cursor.fetchall()
    if not rows:
        print("No registrations found")
    else:
        print("\nRegistrations info")
        for r in rows:
            print(r)

#search
def search():
    name=input("Enter student name: ")
    cursor.execute(
    """SELECT r.id, r.student_name, c.course_name
    FROM registrations r
    JOIN courses c ON r.course_id=c.id
    WHERE r.student_name Like %s""",
    ('%'+name+'%',)
    )
    rows=cursor.fetchall()
    if not rows:
        print("No record found")
    else:
        for r in rows:
            print(r)

#export csv
def export_csv():
    cursor.execute(
        """ SELECT r.id, r.student_name, c.course_name
        FROM registrations r
        JOIN courses c ON r.course_id=c.id"""
    )
    row=cursor.fetchall()

    with open("registrations.csv","w", newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["ID","Student Name","Course"])
        writer.writerows(row)
    print("Exported to CSV file")

#main
def main():
    while True:
        print("\n=== Course Registration System ===")
        print("1. Add New Course")
        print("2. Register Student")
        print("3. View Registrations")
        print("4. Search by Student Name")
        print("5. Export to CSV")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            register()
        elif choice == "3":
            view_registrations()
        elif choice == "4":
            search()
        elif choice == "5":
            export_csv()
        elif choice == "0":
            print("Have a nice day.")
            break
        else: 
            print("Invlid choice, try again!")
if __name__=="__main__":
    main()