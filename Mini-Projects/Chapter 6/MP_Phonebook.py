# Chapter 6, Mini-project: Phonebook

phonebook={}

def add_contact(phonebook):
    name=input("Enter Name:")
    num=input("Enter Number: ")
    phonebook[name]=num
    print("Successfully Added")

def view_contact(phonebook):
    if not phonebook:
        print("No Contact")
    else:
        print("Contact: ")
        for name, num in phonebook.items():
            print(name,":",num)

def search_contact(phonebook):
    name=input("Enter name to search:")
    if name in phonebook:
        print(name,":",phonebook[name])
    else:
        print("Not Found")

def delete_contact(phonebook):
    name=input("Enter name to delete: ")
    if name in phonebook:
        phonebook.pop(name)
        print("Good bye")
    else:
        print("Not Found")

def main():
    while True:
        print("===Phonebook===")
        print("1. Add or Update Contact \n2. Show all contacts " \
        "\n3. Find a contact by name \n4. Remove a Contact \n5. Exit")
        
        ch=input("Enter your choice (1-5): ")

        if ch == '1':
            add_contact(phonebook)
        elif ch == '2':
            view_contact(phonebook)
        elif ch == '3':
            search_contact(phonebook)
        elif ch == '4':
            delete_contact(phonebook)
        elif ch == '5':
            print("bye bye")
            break
        else: print("Invalid Choice!")

if __name__ == "__main__":
    main ()