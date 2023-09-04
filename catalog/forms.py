from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)



    class Meta:
        model = Product
        fields = ["name", "topic", "description"]



