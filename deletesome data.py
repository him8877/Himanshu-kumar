import mysql.connector
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def delete_data_from_db(condition):
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Him@8850',
            database='himanshu'
        )
        cursor = conn.cursor()
        logging.info('Connected to the database successfully')
        
        # Define the delete query with a condition
        delete_query = f"DELETE FROM yourdata_new WHERE {condition}"
        cursor.execute(delete_query)
        conn.commit()
        
        logging.info(f"Deleted data from the table where {condition}")
        
    except mysql.connector.Error as err:
        logging.error(f"Error deleting data from the database: {err}")
    finally:
        # Close the connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            logging.info('Database connection closed')

# Example usage: delete records where age is greater than 30
delete_data_from_db("age > 30")
