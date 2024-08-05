import pika
from models import make_fake_contacts

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue='email_sending')
    
    contacts = make_fake_contacts(10)
    
    for contact in contacts:
        message = str(contact.id)
        channel.basic_publish(exchange='', routing_key='email_sending', body=message.encode())
        print(f" [x] Sent {message} to {contact}")
    
    connection.close()

if __name__ == '__main__':
    main()
