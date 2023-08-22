from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    FORBIDDEN = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in self.FORBIDDEN:
            if word.lower() in name.lower():
                raise forms.ValidationError('Запрещенное слово: {}'.format(word))
        return name


    class Meta:
        model = Product
        fields = "__all__"



class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']


