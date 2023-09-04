
from django.conf import settings
from django.db import models

from users.models import User



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='почта')  # наименование
    topic = models.TextField(verbose_name='тема')  # тема
    description = models.TextField(verbose_name='сообщение')  # описание
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')

