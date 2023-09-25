from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Blog.apps import FidbeckConfig

from Blog.views import Blogcreateview, BloglistView, Blogdetaileview, Blogupdateview, BlogdeleteView



app_name = FidbeckConfig.name



urlpatterns = [
    path('create/', Blogcreateview.as_view(), name='create'),
    path('', BloglistView.as_view(), name='list'),
    path('view/<int:pk>/<slug:slug>', Blogdetaileview.as_view(), name='view'),
    path('edit/<int:pk>/<slug:slug>', Blogupdateview.as_view(), name='edit'),
    path('delete/<int:pk>/<slug:slug>', BlogdeleteView.as_view(), name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


