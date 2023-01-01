import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='jokes')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

    print(ch)
    print(method)
    print(properties)

channel.basic_consume(queue='jokes',
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()