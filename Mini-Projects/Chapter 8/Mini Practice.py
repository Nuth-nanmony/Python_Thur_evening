
def read():
    with open("User Note.txt","r") as note:
        notes=note.read()
        print("\nYour note:\n",notes)

def addon():
    with open("User Note.txt","a") as add:
        print("=== NOTE ===")
        add.write(input("\nType to note: "))

def menu():
    print("Note Pad")
    print("1. Write \n2. Read \n3. Exit")

def main():
    while True:
        menu()
        choice=input("Choose to do: ")
        if choice=='1': addon()
        elif choice=='2': read()
        elif choice=='3':break
        else: print("Try again!")

main()