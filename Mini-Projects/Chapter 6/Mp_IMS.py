#Chapter 6, Mini Project 2: Inventory Management System

inventory={
    "Apple":{"quantity":50, "price":1.2},
    "Banana":{"quantity":30, "price":0.5}
}

def add_products(inventory):
    pro=input("Add Product: ")
    quan=int(input("Quantity: "))
    price=float(input("Price: "))
    inventory[pro]= {
        "quantity":quan,
        "price":price
    }
    print("Successfully Added :>")

def view_products(inventory):
    if not inventory:
        print("Nothing here :(")
    else:
        print("List Contain")
        for name, info in inventory.items():
            print(
                "Product:", name,
                "| Quantity:", info["quantity"],
                "| Price:", info["price"]
            )

def update_products(inventory):
    pro=input("Enter product name: ")
    if pro in inventory:
        n_quan=input("Update Quantity: ")
        n_price=input("Update Price: ")
        if n_quan:
            inventory[pro]["quantity"]= int(n_quan)
        if n_price:
            inventory[pro]["price"]= float(n_price)
        print(f"{pro} Updated Successfully")
    else:
        print("Product not have :<")

def delete_products(inventory):
    pro=input("Enter Product to Delete: ")
    if pro in inventory:
        inventory.pop(pro)
        print("Successfully deleted")
    else:
        print("Product not found")

def main():
    while True:
        print("==Inventory Management System==")
        print("="*10)
        print("1. Add a new product (name, quantity, price)")
        print("2. View all products")
        print("3. Update product quantity")
        print("4. Delete a product")
        print("5. Exit")
        print("="*10)
        ch=input("Choose your choice (1-5): ")

        if ch == '1':
            add_products(inventory)
        elif ch == '2':
            view_products(inventory)
        elif ch == '3':
            update_products(inventory)
        elif ch == '4':
            delete_products(inventory)
        elif ch == '5':
            print("Bye Bye Bye")
            break
        else: print("Wrong Choice!")

if __name__=="__main__":
    main()        