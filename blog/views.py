
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



# class Blogdetaileview(DetailView):
#
#
#     def get_object(self, queryset=None):
#         self.object = super().get_object(queryset)
#         self.object.views_count += 1
#         self.object.save()
#         return self.object


class Blogupdateview(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        return super().form_valid(form)


class BlogdeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

