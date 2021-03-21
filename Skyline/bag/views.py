from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from home.models import Product
from home.forms import ProductForm, EditForm
from django.urls import reverse_lazy
# Create your views here.


class BagView(ListView):
    model = Product
    template_name = 'bag/bag.html'
    success_url = reverse_lazy('BagView')

