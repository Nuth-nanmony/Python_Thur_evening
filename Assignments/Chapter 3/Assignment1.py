#ask for a user age
#age for 13=child. 13-19 teenager. 20-59=adult. else=Senior citizen
age=int(input("Enter your age: "))
if age<=13 :print("Child")
elif age>=13 and age<=19 :print("Teenager")
elif age>=20 and age <59 :print("Adult")
else :print("Senior Citizen")
