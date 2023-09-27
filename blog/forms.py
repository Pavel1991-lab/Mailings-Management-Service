from blog.models import Blog
from django import forms


class BlogForm(forms.ModelForm):



    def form_valid(self, form):
        form.instance.user = self.request.user  # привязываем текущего пользователя к полю user
        return super().form_valid(form)

    class Meta:
        model = Blog
        fields = '__all__'