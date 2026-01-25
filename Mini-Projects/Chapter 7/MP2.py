#Create User Registration and User Login with Strong Password

users={}

def Register():
    username=input("Enter Username: ")
    if username in users: 
        print("Already Register!!") 
        return 
    password=input("Enter Password: ")
    strength=0
    if len(password) >=8: strength += 1
    if any(char.isupper() for char in password): strength+=1
    if any(char.islower() for char in password): strength+=1
    if any(char.isdigit() for char in password): strength+=1
    if any(char in "!@#$%^&*()-_+=" for char in password): strength+=1

    if strength ==  5: print("Strong Password")
    elif 3<=strength<5:print("Medium Password")
    else: print("Weak Password")
    users[username]=password
    print("Registration Successful!")

def login(): 
    username=input("Enter Username: ")
    if username not in users:
        print("User not found!")
        return
    
    password=input("Enter Password: ")
    if users[username]==password:
        print("Login Successful!")
    else:print("Incorrect password:(")

def interface():
    while True:
        print("\n====Login/Register====")
        print("1.Registor ")
        print("2.Login ")
        print("3.Exit ")
        ch=input("Choose your Choice(1-3): ")
        if ch == '1':Register()
        elif ch == '2':login()
        elif ch == '3': 
            print ("Bye bye")
            break
        else: print("Wrong choice Try again!")

interface()