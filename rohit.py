import mysql.connector
from mysql.connector import Error
import logging
import json

def connect_to_mysql(config):
    """Connect to the MySQL database using the provided configuration."""
    try:
        conn = mysql.connector.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )
        if conn.is_connected():
            logging.info("Connection successful.")
            return conn, None
    except Error as e:
        logging.error(f"Error connecting to MySQL: {e}")
        return None, "Failed to connect to the database. Please check the logs for more details."

def create_table(conn):
    """Create a table in the database."""
    cursor = conn.cursor()
    table_name = input("Enter table name: ")
    columns = input("Enter columns (e.g. id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), calories INT): ")

    try:
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} ({columns})
        ''')
        conn.commit()
        logging.info(f"Table '{table_name}' created successfully.")
    except Error as e:
        logging.error(f"Error creating table '{table_name}': {e}")
        return "Failed to create table. Please check the logs for more details."

def insert_data(conn):
    """Insert data into the table."""
    cursor = conn.cursor()
    table_name = input("Enter table name: ")
    columns = input("Enter columns (comma-separated, e.g., name, calories): ")
    values = input("Enter values (comma-separated, e.g., 'Pasta', 200): ")

    try:
        # Construct the SQL query with placeholders
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s'] * len(values.split(',')))})"
        # Convert input values to a tuple
        values_tuple = tuple(value.strip().strip("'") for value in values.split(','))
        # Execute the query with the values tuple
        cursor.execute(sql, values_tuple)
        conn.commit()
        logging.info(f"Data inserted into table '{table_name}': {values_tuple}")
    except Error as e:
        logging.error(f"Error inserting data into table '{table_name}': {e}")
        return "Failed to insert data. Please check the logs for more details."

def read_data(conn):
    """Read data from the table and store it in a list."""
    cursor = conn.cursor()
    table_name = input("Enter table name: ")

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        data_array = [list(row) for row in rows]  # Store rows in a list of lists
        logging.info(f"Data retrieved from table '{table_name}': {data_array}")
        return data_array, None
    except Error as e:
        logging.error(f"Error reading data from table '{table_name}': {e}")
        return None, "Failed to read data. Please check the logs for more details."

def update_data(conn):
    """Update data in the table."""
    cursor = conn.cursor()
    table_name = input("Enter table name: ")
    set_clause = input("Enter SET clause (e.g., calories = 250): ")
    condition = input("Enter condition (e.g., id = 1): ")

    try:
        cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {condition}")
        conn.commit()
        logging.info(f"Data updated in table '{table_name}' where {condition}: {set_clause}")
    except Error as e:
        logging.error(f"Error updating data in table '{table_name}': {e}")
        return "Failed to update data. Please check the logs for more details."

def delete_data(conn):
    """Delete data from the table."""
    cursor = conn.cursor()
    table_name = input("Enter table name: ")
    condition = input("Enter condition (e.g., id = 1): ")

    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        conn.commit()
        logging.info(f"Data deleted from table '{table_name}' where {condition}")
    except Error as e:
        logging.error(f"Error deleting data from table '{table_name}': {e}")
        return "Failed to delete data. Please check the logs for more details."

def dump_to_json(data_array, filename):
    """Dump final data array to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(data_array, file, indent=4)
        logging.info(f"Final data array dumped to '{filename}' successfully.")
    except Exception as e:
        logging.error(f"Error dumping data array to file '{filename}': {e}")

def main():
    config_file = input("Enter the path to the configuration file: ")
    config, err = load_config(config_file)
    if err:
        print(err)
        return
    
    conn, err = connect_to_mysql(config)
    if err:
        print(err)
        return
    
    if conn:
        while True:
            print("\nChoose an operation:")
            print("1. Create a table")
            print("2. Insert data")
            print("3. Read data")
            print("4. Update data")
            print("5. Delete data")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                err = create_table(conn)
                if err:
                    print(err)
            elif choice == '2':
                err = insert_data(conn)
                if err:
                    print(err)
            elif choice == '3':
                data_array, err = read_data(conn)
                if err:
                    print(err)
                else:
                    for row in data_array:
                        print(row)
            elif choice == '4':
                err = update_data(conn)
                if err:
                    print(err)
            elif choice == '5':
                err = delete_data(conn)
                if err:
                    print(err)
            elif choice == '6':
                # Dump final data array to JSON before exiting
                dump_to_json(data_array, 'final_data.json')
                break
            else:
                print("Invalid choice. Please try again.")

        # Close the connection
        conn.close()
        logging.info("Connection closed.")
        print("Connection closed.")

if __name__ == "__main__":
    main()
