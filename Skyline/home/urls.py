from django.urls import path, include
from .views import IndexView, ProductView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>', ProductView.as_view(), name="product"),
]
