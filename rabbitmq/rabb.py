import pika

try:
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='himanshu')

    # Get user input
    message = input("Enter the message: ")

    # Publish the message to the queue
    channel.basic_publish(exchange='',
                        routing_key='himanshu',  # Use the correct queue name
                        body=message)

    print(f" [x] Sent '{message}'")

except pika.exceptions.AMQPConnectionError as e:
    print(f"Error connecting to RabbitMQ server: {e}")

finally:
    # Ensure the connection is closed properly
    if 'connection' in locals() and connection.is_open:
        connection.close()
