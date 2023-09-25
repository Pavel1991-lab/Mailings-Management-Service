from django import template
from catalog.models import Product

register = template.Library()

@register.filter
def count_active():
    products = Product.objects.filter(active=True)
    return products.count()