import sqlite3, numpy as np , user
from Database_Files.database import Database
db = Database()

admin_name = None
def login():
    global admin_name
    username = input("Enter Your username:")
    password = input("Enter Your password:")
    print("-x-x-x-x-x-x-x-x-x-x-")
    login_data =  db.check_user(username, password, 'Admin')
    if login_data[0]:
        admin_name = login_data[1]
    return login_data[0]

def menu():
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Update Stock")
    print("5. View Inventory")
    # print("6. Visualizations")
    print("7. Manage Users")
    # print("8. Generate Bill")
    # print("9. View Transactions")
    print("10. View Audit Logs")
    # print("12. Manage Suppliers")
    # print("13. Manage Restock Requests")
    # print("14. Manage Discounts/Offers")
    print("15. Exit")
    print("-x-x-x-x-x-x-x-x-x-x-")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            user.add_product()
            menu()
        case 2:
            user.update_product()
            menu()
        case 3:
            user.delete_product()
            menu()
        case 4:
            user.update_stock()
            menu()
        case 5:
            print("1. View all products")
            print("2. View products by category")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user.view_products()
            if choice == 2:
                user.view_category()
            menu()
        case 7:
            manage_users()
            menu()
        case 10:
            view_audit_logs()
            menu()
        case 15:
            print("Logout")
            db.log_action(admin_name,"Admin logged out")
        case _:
            print("Invalid choice")
            menu()
            
def view_audit_logs():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM audit_logs")
        data = cursor.fetchall()
        print("="*67)
        print(f"| {"ID":5} | {"User":10} | {"Action":20} | {"Timestamp"[:19]:20} |")
        print("-"*67)
        for log in data:
            print(f"|{log[0]:5} | {log[1]:10} | {log[2]:20} | {log[3][:19]:20} |")
        print("="*67)

def manage_users():
    print("1. Add User")
    print("2. Update User")
    print("3. Delete User")
    print("4. View Users")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            # add_user()
            with sqlite3.connect("inventory.db") as conn:
                cursor = conn.cursor()
                username = input("Enter the username: ")
                password = input("Enter the password: ")
                print("1. Admin")
                print("2. Manager")
                role = int(input("Select the role: "))
                if role == 1:
                    role = "Admin"
                elif role == 2:
                    role = "Manager"
                else:
                    print("Invalid choice")
                    manage_users()
                cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
                conn.commit()
                print("User added successfully")
            manage_users()
        case 2:
            # update_user()
            manage_users()
        case 3:
            # delete_user()
            with sqlite3.connect("inventory.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users")
                view_users()
                user_id = int(input("Enter the ID of the User you want to delete: "))
                cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
                conn.commit()
                print("Product deleted successfully")
            manage_users()
        case 4:
            view_users()
            manage_users()
        case 5:
            menu()
        case _:
            print("Invalid choice")
            manage_users()

def view_users():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        print("="*45)
        print(f"| {"ID":5} | {"Username":15} | {"Role":15} |")
        print("-"*45)
        for user in data:
            print(f"|{user[0]:5} | {user[1]:15} | {user[3]:15} |")
        print("="*45)
        
# manage_users()