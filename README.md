Підготовка:

a) pip install pika pymongo[tls] mongoengine faker
b) 
c)
d) 
e)
f) 


1. Запускаємо producer.py: створюється база з 10 клієнтів і віжправляються їхні айді до RabbitMQ
2. Потім запускаємо файл consumer.py, - він буде обробляти ці повідомлення і імітувати відправку повідомлень.

