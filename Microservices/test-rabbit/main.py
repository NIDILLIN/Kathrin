import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='jokes')

while True:
    st = input()
    channel.basic_publish(exchange='',
                      routing_key='jokes',
                      body=st)

    print(" [x] Sent '%s'" % st)