import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')

result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

ch.queue_bind(exchange='logs', queue=qname)
print('Waiting for logs')

def callback(ch, method, properties, body):
	print(f'Received {body}')
	print(f'Q {qname}')

ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
ch.start_consuming()