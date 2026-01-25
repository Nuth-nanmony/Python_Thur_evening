#Miniproject: ATM simulator
#objective: Simulate an ATM system using function and loop
def deposit ():
    amount =  float(input("Enter an amount to deposit: "))
    
    if amount < 0:
        print("Not valid amount")
        print("-"*15)
        return 0
    else:
        print("Your money have been deposited.")
        print("-"*15)
        return amount

def withdraw(balance):
    withdraw = float(input("Enter an amount to withdraw: "))
    
    if withdraw > balance:
        print("Not Enough Balance!")
        print("-"*15)
        return 0
    elif withdraw < 0:
        print("Cannot withdraw below 0!")
        print("-"*15)
        return 0
    else: 
        print("You have withdraw successful.")
        return withdraw

def show_history(history):
    print("==Transaction History==")
    if not(history): 
        print("There is no Transaction yet.")
    else: 
        print(history)
        print("-"*15)

def check_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    print("-"*15)

def menu():
    balance=0
    transactions=[]
    atm_running = True

    while atm_running:
        print("===ATM Machine===")
        print("1.Depost")
        print("2.Withdraw")
        print("3.View Transaction")
        print("4.Check Balance")
        print("5.Exit")

        ch = input("Select Number to Process (1-5): ")
        print("-"*15)

        if ch == '1':
            amount = deposit()
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: ${amount:.2f}")
        elif ch == '2':
            amount = withdraw(balance)
            if amount >0:
               balance -= amount
               transactions.append(f"Withdrawed: ${amount:.2f}")

        elif ch == '3':
            show_history(transactions)
        elif ch == '4':
            check_balance(balance)
        elif ch == '5':
            atm_running = False
        else: print("Incorrect order. Please try again!")

    print("Thank you for using our ATM machince.")

menu()