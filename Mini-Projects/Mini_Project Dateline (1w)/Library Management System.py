#miniporject, Library management system

import mysql.connector
import csv

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Nimoinmysql123@",
    database="library_db"
)
cursor = db.cursor()
#1. Add new books
def add():
    print("==Please fill the the Title==")
    title=input("Title of the book: ")
    author=input("Author of the book: ")
    category=input("Category of the book: ")
    status=input("Status: ")
    cursor.execute(
        "INSERT INTO books (title,author,category,status) VALUES (%s,%s,%s,%s)",(title,author,category,status)
    )
    db.commit()

#2. Search book by title
#3. Issue book
#4. Return book
#5. Export book to CSV
#6. View all book
#7. Main Driven
#8. Exit