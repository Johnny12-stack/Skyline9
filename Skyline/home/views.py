from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.

#def index(request):
#   return render(request, 'index.html', {})

class IndexView(ListView):
    model = Product
    template_name = 'index.html'


class ProductView(DetailView):
    model = Product
    template_name = 'product.html'