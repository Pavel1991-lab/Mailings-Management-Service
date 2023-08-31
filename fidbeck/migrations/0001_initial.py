# Generated by Django 4.2.4 on 2023-08-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fidbeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='название')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(unique=True, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, unique=True, upload_to='product_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
