#miniporject, Attendance Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
from datetime import date
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB2_HOST"),
    user=os.getenv("DB2_USER"),
    password=os.getenv("DB2_PASSWORD"),
    database=os.getenv("DB2_NAME"),
)
cursor = db.cursor()

#Mark Present/absent
def mark():
    print("\n--Attendance--")
    name=input("Name: ")
    status=input("Status (Present/Absent): ").capitalize()
    today=date.today()

    cursor.execute(
        "INSERT INTO attendance (name, date, status) VALUES (%s,%s,%s)",
        (name,today,status)
    )
    db.commit()
    print("Attendance check.")

#View attendance by date
def view_attendance():
    date=input("Enter date (YYYY-MM-DD): ")
    cursor.execute(
        "SELECT * FROM attendance WHERE date=%s",
        (date,)
    )
    rows=cursor.fetchall()
    if not rows:
        print("No attendance found.")
    else:
        for r in rows:
            print(r)

#Search attendance by name
def search():
    name=input("Enter name: ")
    cursor.execute(
        "SELECT * FROM attendance WHERE name LIKE %s",
        ('%'+name+'%',)
    )
    rows=cursor.fetchall()
    if not rows:
        print("No Track")
    else:
        for r in rows:
            print(r)

#Monthly attendance report
def monthly_attendance():
    month=input("Enter month (MM): ")
    year=input("Enter year (YYYY)")
    cursor.execute(
        """SELECT name,
        SUM(status='Present') AS Present_Days,
        SUM(status='Absent') AS Absent_Days
        FROM attendance
        WHERE MONTH(date)=%s AND YEAR(date)=%s
        GROUP BY name
        """,
        (month,year)
    )
    rows=cursor.fetchall()
    if not rows:
        print("NO date for this,")
    else: 
        print("\nMonthly Attendance Report")
        for r in rows:
            print(r)

#Export attendance to CSV
def export_csv():
    cursor.execute("SELECT * FROM attendance")
    rows=cursor.fetchall()

    with open("attendance.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["ID","Name","Date","Status"])
    print("Attendance exported.")

#main
def main():
    while True:
        print("\n=== Attendance Management System ===")
        print("1. Mark Attendance")
        print("2. View Attendance by Date")
        print("3. Search Attendance by Name")
        print("4. Monthly Attendance Report")
        print("5. Export Attendance to CSV")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            mark()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            search()
        elif choice == "4":
            monthly_attendance()
        elif choice == "5":
            export_csv()
        elif choice == "0":
            print("hAVE A Nice Day A")
            break
        else:
            print(" Invalid choice")

if __name__ == "__main__":
    main()