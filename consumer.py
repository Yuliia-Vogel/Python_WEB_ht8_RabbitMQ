import pika
from models import Contact
from bson.objectid import ObjectId

def send_email_stub(contact):
    # Імітація відправки email
    print(f"Sending email to {contact.email}")

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_sending')

    def callback(ch, method, properties, body):
        contact_id = body.decode()
        contact = Contact.objects(id=ObjectId(contact_id)).first()
        if contact and not contact.email_sent:
            send_email_stub(contact)
            contact.update(email_sent=True)
            print(f" [x] Processed and updated contact {contact_id}")

    channel.basic_consume(queue='email_sending', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
