import psycopg2
from django.core.mail import send_mail

from catalog.classDB_meneger_ import DBManager
from django.core.mail import send_mail
from datetime import datetime
from config import settings


def my_scheduled_job():
    current_time = datetime.now().strftime('%H:%M')
    db_manager = DBManager()
    all_products = db_manager.product_all()
    id_list = []
    for product in all_products:
        if product[3].strftime('%H:%M') <= current_time:
            id_list.append(product[0])

    email_prod_id = db_manager.for_email_prod_id()
    email_lists = []
    for email_prod in email_prod_id:
        if email_prod[1] in id_list:
            email_lists.append(email_prod)

    our_information = []
    for email_list in email_lists:
        topic = ''
        desc = ''
        for product in all_products:
            if product[0] == email_list[1]:
                topic += product[1]
                desc += product[2]

        our_information.append([topic, desc, email_list[0]])

    return our_information
