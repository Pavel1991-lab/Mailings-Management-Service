from django import template
from catalog.models import Client
register = template.Library()


@register.filter
def mymedia(val):
    if val:
        return f'/media/{val}'
    return  '#'

@register.filter
def count_active():
    client = Client.objects.all()
    return  client.count()