#Take two numbers as input
num1=int(input("Enter first number: ")); num2=int(input("Enter second number: "))
#Calculate sum, difference, product and quotient
sum_result=num1+num2
diff_result=num1-num2
prod_result=num1*num2
if num2 != 0:
    quot_result=num1/num2
#Display the results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Quotient:", quot_result)
