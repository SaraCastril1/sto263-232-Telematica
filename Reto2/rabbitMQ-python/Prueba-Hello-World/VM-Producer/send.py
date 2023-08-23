#Establish the conecction with the RabbitMQ server
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
  pika.ConnectionParameters('localhost')) #We're connected now, to a broker on the local machine
channel = connection.channel()

#Create the hello Queue
channel.queue_declare(queue='hello')

#In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
#This exchange is special ‒ it allows us to specify exactly to which queue the message should go. 
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
