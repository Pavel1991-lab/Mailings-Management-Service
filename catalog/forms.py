from django import forms

from catalog.models import Product, Client, MailingLog
from django.forms import HiddenInput


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)

        # Ограничиваем queryset для выбора клиентов только теми, которых создал текущий пользователь
        self.fields['clients'].queryset = Client.objects.filter(user=user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    class Meta:
        model = Product
        fields = ('topic', 'description', 'mailing_time', 'mailing_date', 'clients', 'period', 'active')


class ClientForm(forms.ModelForm):


    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)



    class Meta:
        model = Client
        fields = ('email', 'full_name', 'comment')






