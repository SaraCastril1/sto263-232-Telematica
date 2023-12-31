#!/usr/bin/env python
import pika, sys, os

def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello') #it's a good practice to repeat declaring the queue in both programs.

#Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue. 
#Whenever we receive a message, this callback function is called by the Pika library. In our case this function 
#will print on the screen the contents of the message.

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
