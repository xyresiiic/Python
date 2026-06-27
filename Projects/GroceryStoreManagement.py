# Basic Project: Grocery Store Management System
# This project uses Classes, Dictionaries, and Loops to manage store inventory!

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class GroceryStore:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = {}  # Dictionary to hold our products

    def add_product(self, name, price, stock):
        if name in self.inventory:
            print(f"{name} is already in the inventory. Use update stock instead.")
        else:
            self.inventory[name] = Product(name, price, stock)
            print(f"Added {name} to inventory.")

    def update_stock(self, name, amount):
        if name in self.inventory:
            self.inventory[name].stock += amount
            print(f"Updated {name} stock. New stock: {self.inventory[name].stock}")
        else:
            print(f"Product '{name}' not found!")

    def sell_product(self, name, quantity):
        if name in self.inventory:
            product = self.inventory[name]
            if product.stock >= quantity:
                product.stock -= quantity
                total_cost = product.price * quantity
                print(f"Sold {quantity}x {name}. Total: ${total_cost:.2f}")
            else:
                print(f"Not enough stock! We only have {product.stock} {name}(s) left.")
        else:
            print(f"Product '{name}' not found!")

    def display_inventory(self):
        print(f"\n--- {self.store_name} Inventory ---")
        if not self.inventory:
            print("The inventory is empty.")
            return
            
        for name, product in self.inventory.items():
            print(f"Item: {name.ljust(10)} | Price: ${product.price:.2f} | Stock: {product.stock}")
        print("-----------------------------\n")


# --- Testing our Grocery Store Management System ---

print("Welcome to the Grocery Store Manager!")

# 1. Create a store
my_store = GroceryStore("Fresh Foods Market")

# 2. Add some products
my_store.add_product("Apples", 0.99, 50)
my_store.add_product("Bananas", 0.59, 100)
my_store.add_product("Milk", 3.49, 20)

# 3. View the initial inventory
my_store.display_inventory()

# 4. Sell some items
my_store.sell_product("Apples", 10)
my_store.sell_product("Milk", 5)

# 5. Try to sell more than we have!
my_store.sell_product("Milk", 25)

# 6. Receive a new shipment (update stock)
my_store.update_stock("Milk", 30)

# 7. View the final inventory
my_store.display_inventory()
