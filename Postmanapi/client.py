import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/items"

def get_all_items():
    response = requests.get(BASE_URL)
    print(response.json())

def get_item(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}")
    if response.status_code == 404:
        print("Item not found")
    else:
        print(response.json())

def create_item(name):
    response = requests.post(BASE_URL, json={"name": name})
    if response.status_code == 201:
        print("Item created:", response.json())
    else:
        print("Failed to create item")

def update_item(item_id, name):
    response = requests.put(f"{BASE_URL}/{item_id}", json={"name": name})
    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 400: 
        print("Bad request")
    else:
        print("Item updated:", response.json())

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 404:
        print("Item not found")
    else:
        print("Item deleted:", response.json())

def main():
    while True:
        print("Choose an operation:")
        print("1. Get all items")
        print("2. Get an item by ID")
        print("3. Create a new item")
        print("4. Update an item")
        print("5. Delete an item")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_all_items()
        elif choice == '2':
            item_id = input("Enter item ID: ")
            get_item(item_id)
        elif choice == '3':
            name = input("Enter item name: ")
            create_item(name)
        elif choice == '4':
            item_id = input("Enter item ID: ")
            name = input("Enter new item name: ")
            update_item(item_id, name)
        elif choice == '5':
            item_id = input("Enter item ID: ")
            delete_item(item_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
