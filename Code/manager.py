import sqlite3, numpy as np, user
from Database_Files.database import Database
db = Database()

manager_name = None
def login():
    global manager_name
    username = input("Enter Your username:")
    password = input("Enter Your password:")
    login_data = db.check_user(username, password, 'Manager')
    if login_data[0]:
        manager_name = login_data[1]
    return login_data[0]
    print("-x-x-x-x-x-x-x-x-x-x-")

def menu():
    print("1. Add Product")
    print("2. Update Product")
    print("3. Update Stock")
    print("4. View Inventory")
    print("5. Logout")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            user.add_product()
            menu()
        case 2:
            user.update_product()
            menu()
        case 3:
            user.update_stock()
            menu()
        case 4:
            print("1. View all products")
            print("2. View products by category")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user.view_products()
            if choice == 2:
                user.view_category()
            menu()
        case 5:
            print("Logout")
            db.log_action(manager_name,"Manager logged out")
        case _:
            print("Invalid choice")
            menu()