#Chapter 8, Assignment 2

List="students.txt"

i=int(input("Number to Add: "))

with open(List,"a") as students:
    for j in range(i):
        print(f"\nStudent info {j+1}")
        name=input("Name: ")
        Id=input("ID: ")
        sco=input("Score: ")

        students.write(f"Name: {name}, ID: {Id}, Score: {sco}\n")

with open(List,"r") as info:
    print("\nStudent info\n")
    print(info.read())


