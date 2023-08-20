import pika

connect_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials = pika.PlainCredentials(
        username = 'usr_queue',
        password = 'pwd_queue'
    )
)

channel = pika.BlockingConnection(connect_parameters).channel()

channel.basic_publish(
    exchange    = "data_exchange",
    routing_key = "",
    body        = "algumaCoisa",
    properties  = pika.BasicProperties(
        delivery_mode = 1
    )
)