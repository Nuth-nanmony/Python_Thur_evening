#miniporject, Inventory Management System

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB4_HOST"),
    user=os.getenv("DB4_USER"),
    password=os.getenv("DB4_PASSWORD"),
    database=os.getenv("DB4_NAME"),
)
cursor = db.cursor()

#add product
def add_product():
    print("\n--Add Product--")
    product=input("Enter product name: ")
    quantity=int(input("Amount of quantity: "))
    price=float(input("Enter product price: "))
    supplier=input("Supplier company: ")
    cursor.execute(
        "INSERT INTO products (product,quantity,price,supplier) VALUES (%s,%s,%s,%s)",
        (product,quantity,price,supplier)
    )
    db.commit()
    print("Successfully added new products!")

#update stock quantity
def update_stock():
    print("\n--Update Stock Quantity")
    pid=input("Enter product ID to update: ")
    quantity=int(input("New quantity: "))
    cursor.execute(
        "UPDATE products SET quantity=%s WHERE id=%s",
        (quantity,pid)
    )
    db.commit()
    print("Stock have updated!")

#view low-stock items
def low_stock():
    ls=int(input("Low stock threshold: "))
    cursor.execute(
        "SELECT * FROM products WHERE quantity <= %s", (ls,)
    )
    rows=cursor.fetchall()
    if not rows:
        print("There are no Low Stock Items.")
    else:
        print("\n--Low Stock Items--")
        for pid, name, qty, price, supplier in rows:
            print(f"ID:{pid} | {name} | Qty:{qty}")
#delete products
def delete_product():
    pid=int(input("Enter product id to remove: "))
    confirm = input("Are you sure? (y/n): ").lower()
    if confirm.lower() == "y":
        cursor.execute(
            "DELETE FROM products WHERE id=%s",
            (pid,)
            )
        db.commit()
        if cursor.rowcount == 0:
            print("No product found with that ID")
        else:
            print("Product has been deleted")
    else:
        print("❎ Delete cancelled")
#export inventory to csv
def export_csv():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Quantity", "Price", "Supplier"])
        writer.writerows(rows)

    print("Inventory exported to inventory.csv")

#main 
def main():
    while True:
        print("""
        === Inventory Management System ===
        1. Add Product
        2. Update Stock
        3. View Low Stock
        4. Delete Product
        5. Export to CSV
        6. Exit
        """)
        choice = input("Choose option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            low_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            export_csv()
        elif choice == "6":
            print("Bye have great day")
            break
        else:
            print("nvalid choice")      

if __name__=="__main__":
    main()
