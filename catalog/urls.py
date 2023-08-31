from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import (Contactlistview, ProductByCategoryListView,
                           Productlistview, ProductCreate, ProductUpdateview, ProductdeleteView)
from django.contrib.auth.views import LoginView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', Productlistview.as_view(), name='product_list'),
    path('contacts/', Contactlistview.as_view(), name = 'contact_list'),
    path('good/<int:pk>', ProductByCategoryListView.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name = 'create_product'),
    path('update/<int:pk>/', ProductUpdateview.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductdeleteView.as_view(), name='delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


