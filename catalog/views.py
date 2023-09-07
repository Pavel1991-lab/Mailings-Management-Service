from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Client
from pytils.translit import slugify

from catalog.forms import ProductForm, ClientForm

from config import settings


class Productlistview(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)




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
        new_user = form.save()
        new_user.save()
        user_profile = Client.objects.filter(user=self.request.user)
        recipient_list = []
        for user in user_profile:
            recipient_email = user.email
            recipient_list.append(recipient_email)

        send_mail(
            subject=new_user.topic,
            message=new_user.description,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_email]
        )

        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateview(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        self.object = form.save()



        return super().form_valid(form)



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