#Mini-Project 3: EMS with function
#Input viraible
def info():
    print("---Employee Management System---")
    empID=int(input("Employee ID: "))
    empName=input("Employee Name: ")
    hour=float(input("Hours: "))
    rateperhour=float(input("Rate/Hour: "))
    return empID,empName,hour,rateperhour
#process
#0% tax under 1,500,000
def Tax_cal (info):
    EX=4021
    total=hour*rateperhour*EX
    if total<=1500000: 
        return 0
    elif total>=1500001 : 
        return (total*0.05)-75000
    elif total>=2000001 : 
        return(total*0.1)-175000
    elif total>=8500001 : 
        return(total*0.15)-600000
    else: 
        return(total*0.2)-1225000

#output
empID,empName,hour,rateperhour=info()
EX=4021
total=hour*rateperhour*EX
salary=round((total-Tax_cal(info))/EX,2)
Tax=round(Tax_cal(info)/EX,2)
print(f'{"EmpID":<12} {"EmpName":<15} {"Hours":<10} {"Rate/hour":<12} {"Tax":<13} {"Salary"}')
print(f'{empID:<12} {empName:<15} {hour:<10} {rateperhour:<12} ${Tax:<12} ${salary}')