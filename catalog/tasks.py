

from django.core.mail import send_mail

from celery import shared_task
from datetime import datetime

@shared_task
def send_email_at_specific_time():
    current_time = datetime.now().strftime('%H:%M')
    if current_time == '19:43':
        # Здесь добавьте код для отправки письма
        send_mail(
            subject='Тема письма',
            message='Текст письма',
            from_email='alexpervosotnikov@yandex.ru',
            recipient_list=['pavpervo@rambler.ru']
        )