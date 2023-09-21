import psycopg2
from django.core.mail import send_mail

from catalog.classDB_meneger_ import DBManager
from django.core.mail import send_mail
from datetime import datetime

from catalog.models import Product
from config import settings


def my_scheduled_job():
    current_time = datetime.now().strftime('%H:%M')
    all_product = Product.objects.all()
    print(all_product)
    for product in all_product:
        send_mail(
            subject=product.topic,
            message='hi',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["sotnikov.pavel.91@mail.ru"]
        )




#
# all_product = Product.objects.all()
# for product in all_product:
#     print(product.topic)
#

