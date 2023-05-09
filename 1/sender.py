import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch1 = connection.channel()

ch1.queue_declare(queue='hello')

ch1.basic_publish(exchange='', routing_key='hello', body='Hello World')

print('Message sent')

connection.close()