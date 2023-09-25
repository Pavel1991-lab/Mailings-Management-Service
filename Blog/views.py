from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from Blog.models import Blog


class Blogcreateview(CreateView):

    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('Blog:list')


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


# class Clientlistview(LoginRequiredMixin, ListView):
#     model = Client
#     template_name = 'catalog/client_form.html'
#
#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)

class BloglistView(ListView):
     model = Blog
     template_name = 'Blog/blog_form.html'


     def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# class Productlistview(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'catalog/home.html'
#
#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)

class Blogdetaileview(DetailView):


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object



class Blogupdateview(UpdateView):

        fields = ['title', 'content', 'preview']

        def get_success_url(self):
            return reverse('Blog:view', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class BlogdeleteView(DeleteView):

    success_url = reverse_lazy('Blog:list')


