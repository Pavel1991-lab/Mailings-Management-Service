
from django.conf import settings
from django.db import models

from users.models import User



class Product(models.Model):
    topic = models.TextField(verbose_name='тема')  # тема
    description = models.TextField(verbose_name='сообщение')  # описание
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')
    mailing_time = models.DateTimeField(blank=True, null=True, verbose_name='mailing_time')


class Client(models.Model):
    email = models.EmailField(verbose_name='почта')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='коментарии')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='емейл')



# class ProductClient(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     # Дополнительные поля, если необходимо