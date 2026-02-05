# Write a Python program to create a text file name
name_stu=["1.Nimo","2.Pisey","3.Vanny","4.Pheak","5.Dara"]
file_path="students.txt"

with open(file_path,"w") as List:
    for name in name_stu:
        List.write(name + "\n")
