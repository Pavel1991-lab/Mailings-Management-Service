import psycopg2
from django.core.mail import send_mail

from classDB_meneger_ import  DBManager
#
# from django.core.mail import send_mail
#
# from celery import shared_task
from datetime import datetime

from config import settings


# @shared_task
# def send_email_at_specific_time():
#     current_time = datetime.now().strftime('%H:%M')
#     if current_time == '19:43':
#         # Здесь добавьте код для отправки письма
#         send_mail(
#             subject='Тема письма',
#             message='Текст письма',
#             from_email='alexpervosotnikov@yandex.ru',
#             recipient_list=['pavpervo@rambler.ru']
#         )
#
#


def send_email(mailing, client):
        db_manager = DBManager()

        send_mail(
            subject=mailing.title,
            message=mailing.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email],
            fail_silently=False
        )





def my_scheduled_job():
    current_time = datetime.now().strftime('%H:%M')
    db_manager = DBManager()
    all = db_manager.product_all()
    id = []
    for i in db_manager.product_all():
        if i[3].strftime('%H:%M') <= current_time:
          id.append(i[0])
    email_prod_id = db_manager.for_email_prod_id()
    email = []
    for i in email_prod_id:
        if i[1] in id:
            email.append(i)
    our_email = []
    for y in email:
        our_email.append(y[0])


    topic = []
    for to in all:
        if to[0] in id:
            topic.append(to[1])
    our_topic = ''
    for to in topic:
        our_topic += to


    desc = []
    for des in all:
        if des[0] in id:
            desc.append(des[2])
    d = ''
    for des in desc:
        d +=des
    return d


print(my_scheduled_job())



