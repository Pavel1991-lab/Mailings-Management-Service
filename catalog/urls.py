from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import (Contactlistview, ProductByCategoryListView,
                           Productlistview, ProductCreate, ProductUpdateview, ProductdeleteView, Clientlistview, ClientCreate, ClientUpdateview, ClientdeleteView)
from django.contrib.auth.views import LoginView
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60) (Productlistview.as_view()), name='product_list'),
    path('contacts/', Contactlistview.as_view(), name = 'contact_list'),
    path('good/<int:pk>', ProductByCategoryListView.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name = 'create_product'),
    path('update/<int:pk>/', ProductUpdateview.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductdeleteView.as_view(), name='delete'),
    path('client/', Clientlistview.as_view(), name='client_list'),
    path('clupdate/<int:pk>/', ClientUpdateview.as_view(), name='update_client'),
    path('add_client/', ClientCreate.as_view(), name='add_client'),
    path('cldelete/<int:pk>/', ClientdeleteView.as_view(), name='cl_delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


