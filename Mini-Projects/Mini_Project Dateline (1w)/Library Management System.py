#miniporject, Library management system

import mysql.connector
import csv
from dotenv import load_dotenv
import os
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor()

#1. Add new books
def add():
    print("\n==Please fill the the Title==")
    title=input("Title of the book: ")
    author=input("Author of the book: ")
    category=input("Category of the book: ")
    status=input("Status (Available): ")
    cursor.execute(
        "INSERT INTO books (title,author,category,status) VALUES (%s,%s,%s,%s)",(title,author,category,status)
    )
    db.commit()

#2. Search book by title
def search():
    print("\n==Search Your Book==")
    title=input("Enter the title: ")
    cursor.execute(
        "SELECT * FROM books where title LIKE %s ",
        ("%"+title+"%",)
    )
    for row in cursor.fetchall():
        print(row)
    
#3. Issue book
def issue():
    print("\n==Issue the book==")
    title=input("Enter book title to issue: ")
    cursor.execute(
        "SELECT status FROM books WHERE title= %s",
        (title,)
    )
    result=cursor.fetchone()
    if result is None:
        print("Book not found!")
    elif result[0]=="Issued":
        print("Already Issued.")
    else:
        cursor.execute(
            "UPDATE books SET status=%s WHERE title=%s",
            ("Issued",title)
        )
        db.commit()
        print("Book issued Successfully <3")

#4. Return book
def Return():
    print("\n==Return the book==")
    title=input("Enter book title to return: ")
    cursor.execute(
        "SELECT status FROM books WHERE title=%s",
        (title,)
    )
    result=cursor.fetchone()
    if result is None: print("Book not found")
    elif result[0]=="Available": print("Book is already available")
    else: 
        cursor.execute(
        "UPDATE books SET status=%s WHERE title=%s",
        ("Available",title)
        )
        db.commit()
        print("Book returned successfully")

#5. Export book to CSV
def datacsv():
    cursor.execute("SELECT * FROM books")
    row=cursor.fetchall()
    with open("books.csv","w",newline="") as f:
        write=csv.writer(f)
        write.writerow(["id","title","auther","category","status"])
        write.writerows(row)
    print("\nSuccesfully Export!")

#6. View all book
def All():
    print("\n==View all books==")
    cursor.execute("SELECT * FROM books")
    for row in cursor.fetchall():
        print(row)

#7. Main Driven
def main():
    while True:
        print("\n==Welcome to Library Management System==")
        print("1. Add new books \n2. Search book by title \n3. Issue book " \
        "\n4. Return Book \n5.Export books to CSV \n6.View all books \n7. Exit"
        )
        ch=input("Enter your choice (1-7): ")
        if ch=='1': add()
        elif ch=='2': search()
        elif ch=='3': issue()
        elif ch=='4': Return()
        elif ch=='5': datacsv()
        elif ch=='6': All()
        elif ch=='7': break
        else: print("Invaild Choice, Try Again!")
#8. Exit
if __name__=="__main__":
    main()