import mysql.connector
import logging
import json

# Configure logging
logging.basicConfig(filename='database_Himanshu.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def connect_to_db():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="Him@8850", database="Himanshu")
        logging.info("Connected to the database successfully")
        return conn
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to the database: {err}")
        return None

def create_table(cursor):
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS yourdata (id INT, name VARCHAR(50), age INT, dept VARCHAR(100))''')
        logging.info("Table created or verified successfully")
    except mysql.connector.Error as err:
        logging.error(f"Error creating table: {err}")

def insert_data(cursor, id, name, age, dept):
    try:
        cursor.execute('''INSERT INTO yourdata (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (id, name, age, dept))
        logging.info(f"Data inserted: {id}, {name}, {age}, {dept}")
    except mysql.connector.Error as err:
        logging.error(f"Error inserting data: {err}")

def read_data(cursor):
    try:
        cursor.execute("SELECT * FROM yourdata")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data_array = [dict(zip(columns, row)) for row in rows]
        logging.info("Data read successfully")
        return data_array
    except mysql.connector.Error as err:
        logging.error(f"Error reading data: {err}")
        return []
    finally:
        cursor.close()

def update_data(cursor):
    try:
        cursor.execute("UPDATE yourdata SET age = %s WHERE name = %s AND dept = %s", (26, 'Ankit', 'MCA'))
        logging.info("Data updated successfully for Ankit in MCA")
    except mysql.connector.Error as err:
        logging.error(f"Error updating data: {err}")
    finally:
        cursor.close()

def delete_data(cursor):
    try:
        cursor.execute("DELETE FROM yourdata WHERE name = %s AND dept = %s", ('Ankit', 'MCA'))
        logging.info("Data deleted successfully for Ankit in MCA")
    except mysql.connector.Error as err:
        logging.error(f"Error deleting data: {err}")
    finally:
        cursor.close()

def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logging.error(f"JSON file '{filename}' not found")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON file '{filename}'")
        return []

def write_json(data, filename):
    try:
        # Read existing data file
        existing_data = read_json(filename)

        existing_data.extend(data)

        # Write the combined data back to the file
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
            logging.info(f"Data appended to JSON file '{filename}'")
    except Exception as e:
        logging.error(f"Error writing to JSON file '{filename}': {e}")

def main():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        create_table(cursor)

        # Insert initial data
        insert_data(cursor, 88, 'Himanshu', 25, 'MCA')
        insert_data(cursor, 68, 'Ankit', 30, 'MCA')
        insert_data(cursor, 89, 'Rohit', 22, 'Btech')
        
        # Commit initial inserts
        conn.commit()

        # New user input for insert data
        user_id = int(input("Enter ID: "))
        user_name = input("Enter name: ")
        user_age = int(input("Enter age: "))
        user_dept = input("Enter department: ")
        
        insert_data(cursor, user_id, user_name, user_age, user_dept)
        conn.commit()
        
        # Read data and convert to array
        cursor = conn.cursor()
        data_array = read_data(cursor)
        print("Data as array:", data_array)

        # Update data
        cursor = conn.cursor()
        update_data(cursor)
        conn.commit()

        # Delete data
        cursor = conn.cursor()
        delete_data(cursor)
        conn.commit()

        conn.close()
        logging.info("Connection closed successfully")
        
        # Write data in JSON file
        write_json(data_array, '.json')
    else:
        logging.error("Failed to connect to the database.")

if __name__ == "__main__":
    main()
