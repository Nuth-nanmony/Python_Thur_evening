
def add():
    print("--- Add Student Information---")
    Id=input("Enter ID: ")
    name=input("Enter Name: ")
    attendance=float(input("Enter Attendance (0-10): "))
    quiz=float(input("Enter Quiz (0-15): "))
    Assign=float(input("Enter Assignment (0-25): "))
    Mid=float(input("Enter Midterm (0-25): "))
    F_e=float(input("Enter Final exam (0-30): "))
    total= attendance+quiz+Assign+Mid+F_e
    grade=find_grade(total)

    student[Id] = {
        "Name": name,
        "Attendance": attendance,
        "Quiz": quiz,
        "Assignment": Assign,
        "Midterm": Mid,
        "Final": F_e,
        "Total": total,
        "Grade": grade
    }
    print("Student added successfully 👍")

def find_grade(total):
    if total>=90: return "A"
    elif total>=80: return "B"
    elif total>=70: return "C"
    elif total>=60: return "D"
    elif total>=50: return "E"
    else: return "F"

student ={}

def store():
    print("\n--- Students Information ---")
    if not student:
        print("No student data.")
    for sid, info in student.items():
        print("ID:", sid, "Info:", info)

def update():
    Id=input("Enter ID to Update:")
    if Id in student:
        print("--- Update Student Information ---")
        name=input("Enter Name: ")
        attendance=float(input("Enter Attendance (0-10): "))
        quiz=float(input("Enter Quiz (0-15): "))
        Assign=float(input("Enter Assignment (0-25): "))
        Mid=float(input("Enter Midterm (0-25): "))
        F_e=float(input("Enter Final exam (0-30): "))
        total= attendance+quiz+Assign+Mid+F_e
        grade=find_grade(total)

        student[Id] = {
            "Name": name,
            "Attendance": attendance,
            "Quiz": quiz,
            "Assignment": Assign,
            "Midterm": Mid,
            "Final": F_e,
            "Total": total,
            "Grade": grade
        }
        print("Information Updated successfully ✨")
    else: print("Student not found!")


def search():
    Id=input("Enter ID to Search: ")
    if Id in student:
        print("--- Information Student ---")
        print(student[Id])
    else: print("Information not found.")

def delete():
    Id=input("Enter ID to Delete: ")
    if Id in student:
        del student[Id]
        print("Student Infomation Deleted 🤷‍♂️")

def view():
    Id=input("Enter ID to Search: ")
    if Id in student:
        print("--- Student Found ---")
        print(student[Id])
    else: print("No Information :<")

student_info =True
def menu():
    while student_info:
        print("---- WU STUDENT MANAGEMENT MENU ----")
        print("1. Add Student Information")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student by ID")
        print("5. Delete Student by ID")
        print("6. Exit")
        ch=input("Choose your option (1-6): ")

        if ch == "1":
            add()
        elif ch == "2":
            view()
        elif ch == "3":
            search()
        elif ch == "4":
            update()
        elif ch == "5":
            delete()
        elif ch == "6":
            print("Thank you for using :>")
            break
        else:
            print("Wrong Option, Try again!")
menu()
        