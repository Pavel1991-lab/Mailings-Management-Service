# Generated by Django 4.2.4 on 2023-09-04 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_mail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mail',
        ),
    ]