
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Client
from catalog.forms import ProductForm, ClientForm




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
        form.instance.user = self.request.user
        return super().form_valid(form)





class ProductUpdateview(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


    def form_valid(self, form):
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

def our_clients(request):
    client_count = Client.objects.count()
    return render(request, 'catalog/home.html', {'client_count': client_count})