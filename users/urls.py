from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig

from users.views import LoginView, LogoutView, RegisterView, verify_email
# EmailVerify

app_name = UsersConfig.name

urlpatterns = [

    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/<str:token>/', verify_email, name='verify'),
]