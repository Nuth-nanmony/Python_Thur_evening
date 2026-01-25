#make EDC Management System with function
#input
def info():
    print("===EDC Management System===\n")
    Id=input("Customer ID: ")
    name=input("Customer Name: ")
    loc=input("location: ")
    oldkw=float(input("Your Oldkw: "))
    newkw=float(input("Your Newkw: "))
    return Id,name,loc,oldkw,newkw
#process
def totalkw(newkw,oldkw):
    return newkw-oldkw
def rate(totalkw):
    if totalkw<=10:
        return 380
    elif totalkw<=50: 
        return 480
    elif totalkw<=200: 
        return 610
    else: return 730
def total(totalkw,rate):
    return totalkw*rate
Id,name,loc,oldkw,newkw=info()
totalkw=totalkw(newkw,oldkw)
rate=rate(totalkw)
totalpaid=total(totalkw,rate)
#output
print(f'{"Customer ID":<12} {"Customer Name":<15} {"Location":<12} {"totalkw":<12} {"Total Paid"}')
print(f'{Id:<12} {name:<15} {loc:<12} {totalkw:<12} {totalpaid} Reil')