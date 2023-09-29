
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Client
from catalog.forms import ProductForm, ClientForm




class Productlistview(LoginRequiredMixin,  ListView):
    model = Product
    template_name = 'catalog/home.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        # Подсчет количества активных клиентов
        active_clients_count = Product.objects.filter(active='yes').count()
        clients_count = Client.objects.all().count()

        # Сохранение результата в контексте
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





class ProductUpdateview(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.can_change_product_active'


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        # Подсчет количества активных клиентов

        clients_count = Client.objects.all().count()

        # Сохранение результата в контексте
        context['clients_count'] = clients_count
        return context

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
    client_count = Client.objects.all().count()
    return render(request, 'catalog/home.html', {'client_count': client_count})



def active(request):
    active_products = Product.objects.filter(active='yes')
    context = {
        'active_products_count': active_products.count()
    }
    return render(request, 'catalog/home.html', context)