from django.contrib import admin

from catalog.models import Client, Product


@admin.register(Product)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('pk',)
    search_fields = ('description',)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')

