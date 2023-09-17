import psycopg2
from django.core.mail import send_mail

from classDB_meneger_ import DBManager
from django.core.mail import send_mail
from datetime import datetime
from config import settings









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
        d += des


    our_information = [our_topic, d, our_email]

    return our_information



def send_email():
    info = my_scheduled_job()

    send_mail(
        subject=info[0],
        message=info[1],
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=info[2],
        fail_silently=False
    )


send_email()
print(my_scheduled_job())



