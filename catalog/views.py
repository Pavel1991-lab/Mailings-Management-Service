from datetime import datetime, date, time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from catalog.classDB_meneger_ import DBManager
from catalog.utils import my_scheduled_job
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Client

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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ClientFormset = inlineformset_factory(Product, Client, ClientForm, extra=100)
        if self.request.method == 'POST':
            context_data['formset'] = ClientFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ClientFormset(instance=self.object)

        return context_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_manager = DBManager()

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        new_user = form.save()
        new_user.save()

        if not self.db_manager.is_mail_sent:
            info = my_scheduled_job()

            for info in info:
                subject = info[0]
                message = info[1]
                recipient_list = [info[2]]

                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=recipient_list,
                    fail_silently=False
                )
            self.db_manager.is_mail_sent = True

        return super().form_valid(form)








class ProductUpdateview(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')



    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ClientFormset = inlineformset_factory(Product, Client, ClientForm, extra=100)
        if self.request.method == 'POST':
            context_data['formset'] = ClientFormset(self.request.POST, instance = self.object)
        else:
            context_data['formset'] = ClientFormset(instance = self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        new_user = form.save()
        new_user.save()
        client_email = formset.cleaned_data[0]['email']
        send_mail(
            subject=new_user.topic,
            message=new_user.description,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client_email]
        )

        form.instance.user = self.request.user

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