from django import forms

from catalog.models import Product, Client
from django.shortcuts import render


class ProductForm(forms.ModelForm):



    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)

    class Meta:
        model = Product
        fields = ["name", "topic", "description"]



class ClientForm(forms.ModelForm):

    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)

    class Meta:
        model = Client
        fields = ["email", "comment"]
