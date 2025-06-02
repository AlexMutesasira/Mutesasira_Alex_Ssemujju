# Create an inventory management - Use loops to display or update a list of stock items

# Simple Inventory Management Program

inventory = []

def display_inventory():
    if not inventory:
        print("\nInventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for i, item in enumerate(inventory):
            print(f"{i + 1}. {item['name']} - Quantity: {item['quantity']}")

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory.append({'name': name, 'quantity': quantity})
    print(f"{name} added to inventory.")

def update_item():
    display_inventory()
    if not inventory:
        return
    index = int(input("Enter item number to update: ")) - 1
    if 0 <= index < len(inventory):
        new_quantity = int(input(f"Enter new quantity for {inventory[index]['name']}: "))
        inventory[index]['quantity'] = new_quantity
        print("Item updated successfully.")
    else:
        print("Invalid item number.")

def remove_item():
    display_inventory()
    if not inventory:
        return
    index = int(input("Enter item number to remove: ")) - 1
    if 0 <= index < len(inventory):
        removed_item = inventory.pop(index)
        print(f"{removed_item['name']} removed from inventory.")
    else:
        print("Invalid item number.")

def menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting Inventory Management Program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the program
menu()

