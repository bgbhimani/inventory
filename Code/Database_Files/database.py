import sqlite3, csv, os
from datetime import datetime

class Database:
        
    def check_user(self, username, password, role):
        query = "SELECT COUNT(*) FROM Users WHERE username = ? AND password = ? AND role = ?"
        try:
            # Establish a connection directly within the method
            conn = sqlite3.connect("inventory.db")
            cursor = conn.cursor()
            cursor.execute(query, (username, password, role))
            result = cursor.fetchone()[0]
            # print(f"Query result: {result}")  #check
            if result > 0:
                self.log_action(username, f"{role} logged in")
                return [True, username]
            else:
                self.log_action(username, f"{role} Login failed")
                return [False,username]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return [False,username]
        finally:
            conn.close()

    def initialize_db(self):
        
        folder_path = os.path.join(os.getcwd(), "Database_Files")
        os.chdir(folder_path)
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        
        
        # c.execute('''
        c.executescript('''
                CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT CHECK(role IN ('Admin', 'Co-worker', 'Manager')) NOT NULL
         );
         
                CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL DEFAULT 0,
        price REAL NOT NULL
        );
        
                CREATE TABLE IF NOT EXISTS audit_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_name INTEGER NOT NULL,               
        action TEXT NOT NULL,                    
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_name) REFERENCES users(user_name)
        );
        
        
                CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        date DATETIME DEFAULT CURRENT_TIMESTAMP,
        total_amount DECIMAL(10,2),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        );

         ''')
        conn.commit()
        
        self.import_csv_to_db("inventory.db", "users", "Users.csv")
        self.import_csv_to_db("inventory.db", "products", "products.csv")
        # self.check("Users")
        # self.check("products")
        
    def import_csv_to_db(self,db_path, table_name, csv_path):
        
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            with open(csv_path, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)  # Get the column names from the first row of the CSV
                placeholders = ", ".join("?" for _ in headers)  # Create placeholders for values
                columns = ", ".join(headers)  # Join column names for the INSERT statement
                
                # Create the SQL INSERT statement dynamically
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                
                # Read and insert each row
                for row in reader:
                    try:
                        cursor.execute(sql, row)  # Insert each row into the table
                    except sqlite3.IntegrityError as e:
                        print(f"Skipping row {row}: {e}")
                conn.commit()
                print(f"Data from {csv_path} has been successfully imported into {table_name}.")
                
    def log_action(self,user_name, action):
        try:
            with sqlite3.connect("inventory.db") as conn:
                cursor = conn.cursor()

                # SQL to insert the action into the audit_logs table
                cursor.execute("""
                    INSERT INTO audit_logs (user_name, action, timestamp)
                    VALUES (?, ?, ?)
                """, (user_name, action, datetime.now()))

                print(f"Action '{action}' logged successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")           
                
    def check(self,table_name):
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        
        c.execute(f'''Select * from {table_name} limit 15''')
        print(c.fetchall())
        conn.commit()
                
db = Database()
db.initialize_db()