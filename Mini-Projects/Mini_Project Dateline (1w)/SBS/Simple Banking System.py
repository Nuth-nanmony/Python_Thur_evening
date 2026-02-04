#miniporject, Inventory Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB5_HOST"),
    user=os.getenv("DB5_USER"),
    password=os.getenv("DB5_PASSWORD"),
    database=os.getenv("DB5_NAME"),
)
cursor = db.cursor()

#create account
def create_account():
    print("\n==Create Account Holder")
    name=input("Enter account holder name: ")
    cursor.execute(
        "INSERT INTO accounts (name,balance) VALUES (%s,%s)",
        (name,0)
    )
    db.commit()
    print("Successfully created account.")

#deposit money
def deposit():
    print("\n==Deposit your money==")
    acc_id=int(input("Enter account ID: "))
    deposit=float(input("Enter amount to deposit: "))
    cursor.execute(
        "UPDATE accounts SET balance=balance+%s WHERE id=%s",
        (deposit,acc_id)
    )
    cursor.execute(
        "INSERT INTO transactions (account_id,type,amount) VALUES (%s,%s,%s)",
        (acc_id,"Deposit",acc_id)
    )
    db.commit()
    print("Successfully deposit!")

#withdraw money
def withdraw():
    print("\n==Withdraw your money==")
    acc_id=int(input("Enter account ID: "))
    withdraw=float(input("Enter amount to withdraw: "))
    cursor.execute(
        "SELECT balance FROM accounts WHERE id=%s",
        (acc_id,)
    )
    balance=cursor.fetchone()
    if balance and balance[0] >= withdraw:
        cursor.execute(
            "UPDATE accounts SET balance=balance-%s WHERE id=%s",
            (withdraw,acc_id)
        )
        cursor.execute(
            "INSERT INTO transactions (account_id,type,amount) VALUES (%s,%s,%s)",
            (acc_id,"Withdraw",withdraw)
        )
        db.commit()
        print("Withdraw Completed")
    else:
        print("Insufficient balance")

#View balance
def view_balance():
    print("\n==View Your Balance==")
    acc_id=int(input("Enter account ID: "))
    cursor.execute(
        "SELECT name,balance FROM accounts WHERE id=%s",
        (acc_id,)
    )
    account=cursor.fetchone()
    if account:
        print(f"Name: {account[0]}")
        print(f"Balance: ${account[1]}")
    else:
        print("Account not Found")

#Export csv
def export_csv():
    print("\n==Export transactions to CSV==")
    acc_id=int(input("Enter account ID: "))
    cursor.execute(
        "SELECT type, amount, date FROM transactions WHERE account_id=%s",
        (acc_id,)
    )
    record=cursor.fetchall()

    with open("Transactions.csv","w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["Type","Amount","Date"])
        writer.writerows(record)
    print("Export to CSV file successfully.")

#main
def main():
    while True:
        print("""
        ===Simple Banking System===
        1. Create Account
        2. Deposit Money
        3. Withdraw Money
        4. View Balance
        5. Export Transactions
        6. Exit
            """)
        ch=input("Choose option: ")

        if ch== "1":
            create_account()
        elif ch== "2":
            deposit()
        elif ch== "3":
            withdraw()
        elif ch== "4":
            view_balance()
        elif ch== "5":
            export_csv()
        elif ch== "6":
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()