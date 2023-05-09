import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.queue_declare(queue='first', durable=True)

message = 'This is a testing message'

ch.basic_publish(exchange='', routing_key='first', body=message, properties=pika.BasicProperties(delivery_mode=2, headers={'name':'amir'}))

print('sent message')

connection.close()