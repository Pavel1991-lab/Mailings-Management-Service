from django import forms

from catalog.models import Product, Client
from django.forms import HiddenInput


class ProductForm(forms.ModelForm):
    user = forms.CharField(widget=HiddenInput)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Product
        fields = ('topic', 'description', 'mailing_time', 'mailing_date', 'clients', 'period', 'active' )



class ClientForm(forms.ModelForm):
    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)

    class Meta:
        model = Client
        fields = ('email', 'full_name', 'comment')



