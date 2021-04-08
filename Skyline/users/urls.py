from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UserCreationView, UserRegisterView


urlpatterns = [
    path('login/', UserCreationView.as_view(), name="login"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]