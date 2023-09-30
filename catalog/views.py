
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Client
from catalog.forms import ProductForm, ClientForm

from catalog import forms

from blog.models import Blog


class Productlistview(LoginRequiredMixin,  ListView):
    model = Product
    template_name = 'catalog/home.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.has_perm('catalog.view_product'):
            return Product.objects.all()
        return super().get_queryset().filter(user=self.request.user)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        user = self.request.user
        blog = Blog.objects.all()
        active_clients_count = Product.objects.filter(user=user, active='yes').count()
        clients_count = Client.objects.filter(user=user).count()
        context['blog'] = blog
        context['active_clients_count'] = active_clients_count
        context['clients_count'] = clients_count
        return context



class Contactlistview(ListView):
    model = Product
    template_name = 'catalog/contacts.html'



class ProductByCategoryListView(DetailView):
    model = Product
    template_name = 'catalog/good_detail.html'


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





class ProductUpdateview(LoginRequiredMixin, UpdateView):

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    # permission_required = 'catalog.can_change_product_active'

    # def get_queryset(self):
    #     if self.request.user.is_staff or self.request.user.has_perm('catalog.update_product'):
    #         return Product.objects.all()
    #
    #     return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     for field_name in form.fields:
    #         if field_name != 'active':
    #             form.fields[field_name].widget = forms.HiddenInput()
    #     return form



class ProductdeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')





class Clientlistview(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'catalog/client_form.html'
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('catalog:client_list')



    def form_valid(self, form):
        new_user = form.save()
        new_user.save()

        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientUpdateview(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('catalog:client_list')

    def form_valid(self, form):
        self.object = form.save()


        return super().form_valid(form)


class ClientdeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('catalog:client_list')

