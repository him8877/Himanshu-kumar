import mysql.connector
import pika
import json
import logging

# Configure logging
logging.basicConfig(filename='ap.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def insert_data_into_db(data):
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
        
        # Insert data into the new table
        insert_query = "INSERT INTO yourdata_new (id, name, age, Dept) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (data['id'], data['name'], data['age'], data['Dept']))
        conn.commit()
        logging.info(f"Inserted data into the new table: {data}")
        
    except mysql.connector.Error as err:
        logging.error(f"Error inserting data into the database: {err}")
    finally:
        # Close the connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            logging.info('Database connection closed')

def callback(ch, method, properties, body):
    try:
        data = json.loads(body)
        logging.info(f"Received data from RabbitMQ: {data}")
        insert_data_into_db(data)
    except json.JSONDecodeError as err:
        logging.error(f"Error decoding JSON: {err}")

def consume_from_rabbitmq():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        logging.info('Connected to RabbitMQ successfully')

        channel.queue_declare(queue='hello')
        logging.info('Queue "hello" declared')

        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
        logging.info('Started consuming from RabbitMQ')

        channel.start_consuming()
    
    except pika.exceptions.AMQPError as err:
        logging.error(f"Error consuming from RabbitMQ: {err}")
    finally:
        if connection and connection.is_open:
            connection.close()
            logging.info('RabbitMQ connection closed')

# Start consuming from RabbitMQ
consume_from_rabbitmq()
