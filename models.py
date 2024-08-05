from mongoengine import Document, StringField, BooleanField, connect, disconnect
from faker import Faker

URI = "uri"

disconnect()
connect(host=URI, db="my_db")


class Contact(Document):
    fullname = StringField(required=True, unique=True)
    email = StringField(required=True)
    email_sent = BooleanField(default=False)

    def __str__(self):
        return f"Contact (fullname={self.fullname}, email={self.email}, email_sent={self.email_sent})"


fake = Faker()

def make_fake_contacts(n=10):
    contacts = []
    for _ in range(n):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email()
        )
        contact.save()
        contacts.append(contact)
    return contacts
