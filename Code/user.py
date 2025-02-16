import sqlite3, numpy as np
from Database_Files.database import Database
db = Database()

def update_product():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        view_products()
        product_id = int(input("Enter the ID of the product you want to update: "))
        company_name = input("Enter the new company name of the product: ") 
        name = input("Enter the new name of the product: ")
        category = input("Enter the new category of the product: ")
        price = float(input("Enter the new price of the product: "))
        
        cursor.execute("UPDATE products SET name = ?, company_name = ? category = ?, price = ? WHERE product_id = ?", (name, company_name, category, price, product_id))
        conn.commit()
        print("Product updated successfully")

def delete_product():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        view_products()
        product_id = int(input("Enter the ID of the product you want to delete: "))
        
        cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        conn.commit()
        print("Product deleted successfully")
    
def update_stock():
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        view_products()
        product_id = int(input("Enter the ID of the product you want to update: "))
        quantity = int(input("Enter the new quantity of the product: "))
        
        cursor.execute("UPDATE products SET quantity = ? WHERE product_id = ?", (quantity, product_id))
        conn.commit()
        print("Product updated successfully")
    
def add_product():
    name = input("Enter the name of the product: ")
    company_name = input("Enter the name of Company: ")
    category = input("Enter the category of the product: ")
    quantity = int(input("Enter the quantity of the product: "))
    price = float(input("Enter the price of the product: "))
    
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name,company_name, category, quantity, price) VALUES (?, ?, ?, ?, ?)", (name, company_name, category, quantity, price))
        conn.commit()
        print("Product added successfully")
               
def view_products():
    print("\n::::::The Products:::::::")
    print("-x-x-x-x-x-x-x-x-x-x-")
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        
        np.array(products)
        
        print(f" {"="*97}")
        print(f" | {'ID':<4} | {'Company-Name':15} | {'Name':27} | {'Category':15} | {'Quantity':<8} | {'Price':<10}|")
        print(f" {"-"*97}")
        for product in products:
            print(f" | {product[0]:<4} | {product[1]:15} | {product[2]:27} | {product[3]:15} | {product[4]:<8} | ₹{product[5]:<10}|")
        print(f" {"="*97}")
        
    print("-x-x-x-x-x-x-x-x-x-x-")
    
def view_category():
    print("\n::::::The Products:::::::")
    print("-x-x-x-x-x-x-x-x-x-x-")
    with sqlite3.connect("inventory.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        
        np.array(products)
        categories = set(product[3] for product in products)
        categories = list(categories)
        
        print("Categories:")
        for i,category in enumerate(categories):
            count = len([p for p in products if p[3] == category])
            print(f"{(i+1):3}. {categories[i]}({count})")
        
        choice = int(input("Enter the category number: "))
        print(f"Products in {categories[choice-1]} category:")
        print(f" {"="*97}")
        print(f" | {'ID':<4} | {'Company-Name':15} | {'Name':27} | {'Category':15} | {'Quantity':<8} | {'Price':<10}|")
        print(f" {"-"*97}")
        for product in products:
            if product[3] == categories[choice-1]:
                print(f" | {product[0]:<4} | {product[1]:15} | {product[2]:27} | {product[3]:15} | {product[4]:<8} | ₹{product[5]:<10}|")
        print(f" {"="*97}")