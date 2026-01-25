#EnterID, name, Sex, Number hours, RatePerHour
Staff_ID=input("Enter Staff ID: ");Name=(input("Enter Name: "));Sex=input("Enter Sex (M/F): ");Num_hours=float(input("Enter Number of Hours Worked: "));Rate_per_hour=float(input("Enter Rate per Hour: "))
#Process Find Salary
Salary=Num_hours*Rate_per_hour
#Display staff information
print("\n===== Staff Information =====")

print(f'{"ID":<10} {"Name":<15} {"Sex":<5} {"Hours Worked":<15} {"Rate per Hour":<15} {"Salary":<10}')
print(f'{Staff_ID:<10} {Name:<15} {Sex:<5} {Num_hours:<15} {Rate_per_hour:<15.2f} {Salary:<10}')