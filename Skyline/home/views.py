from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

#def index(request):
#   return render(request, 'index.html', {})

class IndexView(ListView):
    model = Product
    template_name = 'index.html'


class ProductView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    success_url = reverse_lazy('product_detail')


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'



class UpdateProductView(UpdateView):
    model = Product
    form_class = EditForm 
    template_name = 'edit_product.html'


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('index')


class ProductsView(ListView):
    model = Product
    template_name = 'products.html'