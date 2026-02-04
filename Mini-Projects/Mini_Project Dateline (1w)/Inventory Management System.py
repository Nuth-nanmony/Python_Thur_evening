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
        (pid,quantity)
    )
    db.commit()
    print("Stock have updated!")

#view low-stock items
def low_stock():
    ls=int(input("Low stock threshold: "))
    cursor.execute(
        "SELECT * FROM products WHERE quantity <= %s", (ls)
    )
    rows=cursor.fetchall()
    print("\n--Low Stock Items--")
    for r in rows:
        print(r)

#delete products
def delete_product():
    pid=int(input("Enter product id to remove: "))
    cursor.execute(
        "DELETE FROM products WHERE id=$s",(pid)
        )
    db.commit()
    print("Product have been deleted")

#export inventory to csv
def export_csv():
    pass

#main 
def main():
    while True:
        pass

if __name__=="__main__":
    main()
