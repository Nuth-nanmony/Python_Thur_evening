#Wesetern Employee  Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor()

def dbCon_employee():
   name = input("Enter Employee Name: ")
   position = input("Enter position: ")
   salary = input("Enter Salary: ")
   cursor.execute(
       "INSERT INTO employees (name,position,salary) VALUES (%s,%s,%s)",
    (name,position,salary)
   )
   db.commit()

def add_employee():
    name=input("Enter name: ")
    position=input("Enter position: ")
    salary=float(input("Enter salary: "))
    cursor.execute(
        "INSERT INTO employees (name,position,salary) VALUES (%s,%s,%s)",
        (name,position,salary)
    )
    db.commit()
    print("Employee added successfully")
 
def view_employee():
    cursor.execute("SELECT * FROM employees")
    rows=cursor.fetchall()
    if rows:
        print(
        f"""
                    Employees list
        {'ID':<5}{'Name':<20}{'Position':<15}{'Salary':<10}
        """)
        for row in rows:
            sid,name,position,salary=row
            print(
        f"""
        {sid:<5}{name:<20}{position:<15}{salary:<10}
        """)
    else:
        print("No employees found")

def update_employee():
    sid = input("Enter Employee ID to update: ")
    new_name = input("Enter new name: ")
    new_position = input("Enter new position: ")
    new_salary = float(input("Enter new salary: "))
    cursor.execute(
        "UPDATE employees SET name=%s, position=%s, salary=%s WHERE id=%s",
        (new_name, new_position, new_salary, sid)
    )
    db.commit()
    print("Employee updated successfully")

def delete_employees():
    emp_id = input("Enter Employee ID to delete: ")
    cursor.execute(
        "DELETE FROM employees WHERE emp_id=%s",
        (emp_id,)
    )
    db.commit()
    print("Employee deleted successfully\n")

def manu():
    while True:
        print(
        """
        ==== Employee Management System ====
        1. Add Employee
        2. View Employee
        3. Update Employee
        4. Delete Employee
        5. Exit
        """
        )
        ch=input("Enter choice (1-5): ")
        if ch=='1':add_employee()
        elif ch=='2':view_employee()
        elif ch=='3':update_employee()
        elif ch=='4':delete_employees()
        elif ch=='5':break
        else: print("Try again")

if __name__=="__main__":
    manu()