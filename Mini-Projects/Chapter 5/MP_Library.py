#Mini Project: Library Book Management System 
books=[]
def add_book():
    print("===+Add your book+===")
    name=input("Add book: ")
    if name in books:
        print("This already exsit!")
        return
    books.append(name)
    print("Successfully add <3.")

def view_book():
    print("===+All book+===")
    if not books:
        print("There is no book :<")
        return
    for book in books:
        print (f"Title Book : {book}")

def search_book():
    print("===+Search your book+===")
    find=input("Enter name to find: ")

    if find in books:
        print(f"Book Found: {find}")
    else:print("Not found :( ")

def delete_book():
    print("===+Delete Book+===")
    book=input("Enter name to delete: ")
    if book in books:
        books.remove(book)
        print("Successfully deleted.")
        return
    print("There is no match...")

def count_books():
    print("Total book")
    print(f"Total of books: {len(books)}")

def menu():
    while True:
        print("\n===== Library Menu =====")
        print("1. Add new book")
        print("2. View all books")
        print("3. Search book by title")
        print("4. Delete a book")
        print("5. Count total books")
        print("6. Exit")

        choice=input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            count_books()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

#main 
menu()