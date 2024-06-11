import mysql.connector
import pika
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', filename='my_app.log')
logger = logging.getLogger(__name__)

def get_data_from_db():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Him@8850',
            database='himanshu'
        )
        cursor = conn.cursor()
        logger.info('Connected to the database successfully')

        # Execute a query to get data
        cursor.execute("SELECT id, name, age, Dept FROM yourdata")
        rows = cursor.fetchall()
        logger.info(f"Fetched {len(rows)} rows from the database")

    except mysql.connector.Error as err:
        logger.error(f"Error fetching data from the database: {err}")
        return []
    finally:
        # Close the connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            logger.info('Database connection closed')

    return [{'id': row[0], 'name': row[1], 'age': row[2], 'Dept': row[3]} for row in rows]

def send_to_rabbitmq(data):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        logger.info('Connected to RabbitMQ successfully')

        channel.queue_declare(queue='hello')
        logger.info('Queue "hello" declared')

        for item in data:
            # Convert to JSON format
            json_data = json.dumps(item)
            # Ensure data is a string and encode it to bytes
            channel.basic_publish(exchange='', routing_key='hello', body=json_data.encode('utf-8'))
            logger.info(f"Sent data to RabbitMQ: {json_data}")
        
        logger.info("Data successfully sent to RabbitMQ")
    
    except pika.exceptions.AMQPError as err:
        logger.error(f"Error sending data to RabbitMQ: {err}")
    finally:
        if connection and connection.is_open:
            connection.close()
            logger.info('RabbitMQ connection closed')

# Retrieve data from the database
db_data = get_data_from_db()

# Push data to RabbitMQ
if db_data:
    send_to_rabbitmq(db_data)