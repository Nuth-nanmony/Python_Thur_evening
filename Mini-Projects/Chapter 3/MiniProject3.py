#Mini-Project 3: EMS
#Input
print("---Employee Management System---")
empID=int(input("Employee ID: "))
empName=input("Employee Name: ")
hour=float(input("Hours: "))
rateperhour=float(input("Rate/Hour: "))
#process
EX=4021
total=hour*rateperhour*EX
#0% tax under 1,500,000
if total<=1500000: 0
elif total>=1500001 : Tax=(total*0.05)-75000
elif total>=2000001 : Tax=(total*0.1)-175000
elif total>=8500001 : Tax=(total*0.15)-600000
else: Tax=(total*0.2)-1225000
salary=round((total-Tax)/EX,2)
Tax=round(Tax/EX,2)
#output
print(f'{"EmpID":<12} {"EmpName":<15} {"Hours":<10} {"Rate/hour":<12} {"Tax":<16} {"Salary"}')
print(f'{empID:<12} {empName:<15} {hour:<10} {rateperhour:<12} ${Tax:<15} ${salary} ')