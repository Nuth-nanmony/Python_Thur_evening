#assignment deadline 3 day

import mysql.connector

conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="company_db"
)

cursor = conn.cursor()
def addemployee():
    id=int(input("Enter ID: "))
    sname=input("Enter name: ")
    salary=float(input("Enter Salary: "))
    department=input("Enter Department: ")

    sql="INSERT INTO employees (id,sname, salary, department) VALUES (%s,%s, %s, %s)"
    values=(id,sname,salary,department)

    cursor.execute(sql,values)
    conn.commit()
    print("Successfully Added!")

def viewemployee():
    cursor.execute("SELECT * FROM employees")
    rows=cursor.fetchall()
    print("ID | Name | Salary | Department")
    print("----------------------------------")
    for row in rows:
        print(row[0], "|", row[1], "|", row[2], "|", row[3])
    print()

def searchemployee():
    name=input("Enter name to search: ")
    sql="select * from employees where sname like %s"
    cursor.execute(sql,('%'+name+'%',))
    rows=cursor.fetchall()

    if rows:
        print("\nSearch Results:")
        print("ID | Name | Salary | Department")
        print("----------------------------------")
        for row in rows:
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
    else:
        print("No employee found with that name.")
    print()

def main():
    while True:
        print("Employee Management System")
        print("1. Add New Employee \n2. View All Employees \n3. Search Employee by Name \n4. Exit")
        ch=input("Enter your choice(1-4): ")
        if ch=='1':addemployee()
        elif ch=='2':viewemployee()
        elif ch=='3':searchemployee()
        elif ch=='4':
            print("Bye!!!")
            break
        else:print("Invalid choice! Try again!!")

if __name__ == "__main__":
    main()
    
cursor.close()
conn.close()