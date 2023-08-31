from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)



    class Meta:
        model = Product
        fields = ["name", "description"]



class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']