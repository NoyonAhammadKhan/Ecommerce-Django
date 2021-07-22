from django.shortcuts import render
#Import Django  Views

from django.views.generic import ListView, DetailView

# Create your views here.

from App_Shop.models import Product

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'