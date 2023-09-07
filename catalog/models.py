
from django.conf import settings
from django.db import models

from users.models import User


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')

    def __str__(self):
        return self.email


class Product(models.Model):
    email_adress = models.ManyToManyField(Client, through='ProductClient', verbose_name='почта')  # наименование
    topic = models.TextField(verbose_name='тема')  # тема
    description = models.TextField(verbose_name='сообщение')  # описание
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')







class ProductClient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Дополнительные поля, если необходимо