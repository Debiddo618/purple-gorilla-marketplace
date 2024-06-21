from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'purplegorilla/index.html', {'products': products})


def base(request):
    return render(request, 'base.html')
