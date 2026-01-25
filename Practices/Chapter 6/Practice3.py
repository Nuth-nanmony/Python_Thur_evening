dictionary = {"Name":"Ny" , "Age":"67" , "ID":"000" , "Course":"CS" , "GPA":"Unknown"}

dictionary.pop("Age")

for key, value in dictionary.items():
    print(key,":",value)

print("Length: ",len(dictionary))
