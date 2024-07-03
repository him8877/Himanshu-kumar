import requests

base_url = "http://127.0.0.1:5000"  # Update this with the address where your Flask server is running

def create_data():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ")
    data = {"id": id, "name": name, "age": age, "dept": dept}
    endpoint = "/create"
    url = base_url + endpoint
    response = requests.post(url, json=data)
    return response.json()

def read_all_data():
    endpoint = "/retrieve"
    url = base_url + endpoint
    response = requests.get(url)
    return response.json()

def update_specific_data():
    id = int(input("Enter ID of the record to update: "))
    age = int(input("Enter new age: "))
    data = {"age": age}
    endpoint = f"/update/{id}"
    url = base_url + endpoint
    response = requests.put(url, json=data)
    return response.json()

def delete_specific_data():
    id = int(input("Enter ID of the record to delete: "))
    endpoint = f"/delete/{id}"
    url = base_url + endpoint
    response = requests.delete(url)
    return response.json()

# Example usage:
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Create data")
        print("2. Read all data")
        print("3. Update specific data")
        print("4. Delete specific data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(create_data())
        elif choice == '2':
            print(read_all_data())
        elif choice == '3':
            print(update_specific_data())
        elif choice == '4':
            print(delete_specific_data())
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
