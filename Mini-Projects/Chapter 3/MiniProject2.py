#make EDC Management System
#input
print("===EDC Management System===\n")
ID=input("Customer ID: ")
Name=input("Customer Name: ")
Loc=input("location: ")
OldKw=float(input("Your Oldkw: "))
NewKw=float(input("Your Newkw: "))
#process
Totalkw=NewKw-OldKw
if Totalkw<=10: rate=380
elif Totalkw<=50: rate=480
elif Totalkw<=200: rate=610
else: rate=730
Total=Totalkw*rate
#output
print(f'{"Customer ID":<12} {"Customer Name":<15} {"Location":<12} {"OldKW":<12} {"NewKW":<12} {"Total Paid"}')
print(f'{ID:<12} {Name:<15} {Loc:<12} {OldKw:<12} {NewKw:<12} {Total} Reil')