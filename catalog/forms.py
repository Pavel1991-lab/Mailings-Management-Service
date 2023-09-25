from django import forms

from catalog.models import Product, Client




class ProductForm(forms.ModelForm):



    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)

    class Meta:
        model = Product
        fields = [field.name for field in Product._meta.fields if field.name != 'user']



class ClientForm(forms.ModelForm):


    class Meta:
        model = Client
        fields = '__all__'



