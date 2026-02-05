# Python Search 

fp="Final-Exam/Part1/students.txt"

def search():
    name=input("Enter name for searching: ")
    with open(fp,"r") as f:
        name1=f.read()
    if name in name1:
        print(f"Student name {name} exist")
    else:
        print("Students not found")

search()