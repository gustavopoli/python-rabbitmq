import pika

def fnc_callback(ch, method, properties, body):
    decoded_message = body.decode("utf-8")
    print(decoded_message)

connect_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials = pika.PlainCredentials(
        username = 'usr_queue',
        password = 'pwd_queue'
    )
)

channel = pika.BlockingConnection(connect_parameters).channel()

channel.queue_declare(
    queue="data_queue",
    durable=True
)

channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    on_message_callback=fnc_callback
)

print('Listen RabbitMQ on Port 5672')

channel.start_consuming()
