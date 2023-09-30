
from django.conf import settings
from django.db import models

from users.models import User

class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='коментарии')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  verbose_name='пользователь')

    def __str__(self):
        return self.email



class Product(models.Model):
    PERIOD_CHOICES = (
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    )
    ACTIVE_CHOICES = (
        ('yes', 'Активна'),
        ('no', 'Не активна'),
    )

    topic = models.TextField(verbose_name='тема')  # тема
    description = models.TextField(verbose_name='сообщение')  # описание
    clients = models.ManyToManyField(Client, verbose_name='клиенты', related_name='product')
    mailing_time = models.TimeField(blank=True, null=True, verbose_name='время рассылки')
    mailing_date = models.DateField(blank=True, null=True, verbose_name='дата рассылки')
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, verbose_name='период')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='пользователь')
    active = models.CharField(max_length=10, choices=ACTIVE_CHOICES, verbose_name='статус')


    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Расслыка'

        permissions = [
            ('can_change_product_active', 'Can_change_product_active'),
        ]

class MailingLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    response = models.TextField(blank=True, null=True)





