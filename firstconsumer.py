import pika
import time
import random
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f'First consumer: received new message: {body}')

    # processing_time = random.randint(1, 6)
    # print(f'First recieved: {body}, will take {processing_time} to process')
    # time.sleep(processing_time)
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    # print('Finished processing the message')


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print('Started consuming')

channel.start_consuming()
