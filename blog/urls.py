from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig

from blog.views import BlogListView, Blogcreateview, Blogupdateview, BlogdeleteView, Blogdetaileview
from django.views.decorators.cache import cache_page

app_name = BlogConfig.name

urlpatterns = [
                  path('createblog/', Blogcreateview.as_view(), name='create_blog'),
                  path('', cache_page(60) (BlogListView.as_view()), name='blog_list'),
                  path('update/<int:pk>/', Blogupdateview.as_view(), name='update_blog'),
                  path('view/<int:pk>/', Blogdetaileview.as_view(), name='view'),
                  path('delete/<int:pk>/', BlogdeleteView.as_view(), name='delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
