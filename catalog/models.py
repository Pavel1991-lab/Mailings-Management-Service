
from django.conf import settings
from django.db import models

from users.models import User



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='почта')  # наименование
    description = models.TextField(verbose_name='сообщение')  # описание
    created_date = models.DateTimeField(auto_now_add=True)  # дата создания
    last_modified_date = models.DateTimeField(auto_now=True)  # дата последнего изменения
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='пользователь')

class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=20, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='имя версии')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.version_name
