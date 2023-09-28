
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from blog.forms import BlogForm
from blog.models import Blog


class Blogcreateview(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        return super().form_valid(form)



class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Титульная страница блога'
        context['blogs'] = Blog.objects.all()  # Получение всех объектов блога из базы данных
        return context

class Blogupdateview(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        return super().form_valid(form)


class BlogdeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

