from django.urls import path, include
from .views import IndexView, ProductView, AddProductView, UpdateProductView, DeleteProductView, ProductsView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>', ProductView.as_view(), name="product_detail"),
    path('products/', ProductsView.as_view(), name="products"),
    path('add_product/', AddProductView.as_view(), name="add_product"),
    path('product/edit/<int:pk>', UpdateProductView.as_view(), name="edit_product"),
    path('product/<int:pk>/delete', DeleteProductView.as_view(), name="delete_product"),

]
