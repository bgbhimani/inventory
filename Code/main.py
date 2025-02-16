# print("શ્રી ગણેશાય નમ:")
import admin, manager
from Database_Files.database import Database
db = Database()


def main():
    # db.initialize_db()  # Ensure this is called without arguments
    print("-x-x-x-x-x-x-x-x-x-x-")
    print("1.Admin")
    print("2.Manager")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            # print("Admin")
            while not admin.login():
                print("Admin login failed")
                print("1. Try Again")
                print("2. Exit")
                choice = int(input("Enter your choice: "))
                print("-x-x-x-x-x-x-x-x-x-x-")
                if choice == 2:
                    break
            else:
                print("Admin login successful")
                admin.menu()
        case 2:
            print("Manager")
            while not manager.login():
                print("Manager login failed")
                print("1. Try Again")
                print("2. Exit")
                choice = int(input("Enter your choice: "))
                print("-x-x-x-x-x-x-x-x-x-x-")
                if choice == 2:
                    break
            else:
                print("Manager login successful")
                manager.menu()
        case _:
            print("Invalid choice")
            
    print("-x-x-x-x-x-x-x-x-x-x-")
    
if __name__ == "__main__":
    main()