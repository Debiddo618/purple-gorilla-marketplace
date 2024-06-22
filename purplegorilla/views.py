from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'purplegorilla/index.html', {'products': products})


def base(request):
    return render(request, 'base.html')

# create a product


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'image', 'description', 'category', 'price']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # form.instance is the product
        # Let the CreateView do its job as usual
        return super().form_valid(form)

# show a product by id


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})
