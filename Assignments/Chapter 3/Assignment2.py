#making calculator'
import math
num1=float(input("Enter number: "))
operat = input("Enter Operator (+, -, *, /, //, **, %): ")
num2=float(input("Enter number: "))

if operat == '+' :
    total=num1+num2
elif operat == '-':
    total=num1-num2
elif operat == '/':
    total=num1/num2
elif operat == '*':
    total=num1*num2
elif operat == '//':
    total=num1//num2
elif operat == '**':
    total=num1**num2
elif operat == '%':
    total=num1 % num2
else :print("Invild Operator")
print(f"Result: {num1} {operat} {num2} = {total}")