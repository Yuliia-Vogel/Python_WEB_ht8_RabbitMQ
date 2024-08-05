import os

from mongoengine import Document, StringField, BooleanField, connect, disconnect
from faker import Faker

from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("MONGO_URI")
task_db = os.getenv("DB_NAME")

disconnect()
connect(host=URI, db=task_db)


class Contacts(Document):
    fullname = StringField(required=True)
    email = StringField(required=True, unique=True)
    email_sent = BooleanField(default=False)

    def __str__(self):
        return f"Contact (fullname={self.fullname}, email={self.email}, email_sent={self.email_sent})"


fake = Faker()

def make_fake_contacts(n=10):
    contacts = []
    try:
        for _ in range(n):
            contact = Contacts(
                fullname=fake.name(),
                email=fake.email()
            )
            contact.save()
            contacts.append(contact)
            print(f'Created: {contact}')
        return contacts
    except Exception as e:
        print(f"Error during making fake contacts: {e}")


if __name__ == "__main__":
    make_fake_contacts()
    # for contact in Contacts():
    #     print(contact)
