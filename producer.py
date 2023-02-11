import pika
import time
import random
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "hello I want to broadcast this message"

channel.basic_publish(exchange='pubsub', routing_key='', body=message)

print(f'Sent message: {message}')
time.sleep(random.randint(1, 4))

# message_id = 1

# while True:
#     message = f'Sending message_id: {message_id}'
#     channel.basic_publish(exchange='', routing_key='letterbox', body=message)
#     print(f'Sent message: {message}')
#     time.sleep(random.randint(1, 4))
#     message_id += 1
