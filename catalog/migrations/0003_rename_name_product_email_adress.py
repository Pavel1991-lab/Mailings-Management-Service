# Generated by Django 4.2.5 on 2023-09-07 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_client_user_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='email_adress',
        ),
    ]