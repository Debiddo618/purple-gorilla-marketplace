from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Product, Order
from decimal import Decimal

# Create your views here.


def order_create(request, user_id, product_id):
    product = Product.objects.get(id=product_id)
    product.status = True
    product.save()

    # Create the order and save it, status = pending
    order = Order.objects.create(
        user=request.user, product=product, total_price=Decimal(product.total_price()))
    return redirect('user', user_id=user_id)


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/detail.html', {'order': order})


def confirm_order(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'orders/confirm_order.html', {'product': product})


class OrderUpdate(UpdateView):
    model = Order
    fields = ['status']

    def get_success_url(self):
        order = self.object
        return reverse('user', kwargs={'user_id': order.product.user.id})


class OrderDelete(DeleteView):
    model = Order

    def get_success_url(self):
        user_id = self.object.user.id
        product = self.object.product
        product.status = False
        product.save()

        return reverse('user', kwargs={'user_id': user_id})


def index(request):
    products = Product.objects.filter(status=False)
    product_name = request.GET.get('product_name')
    product_category = request.GET.get('category')
    if product_name != '' and product_name is not None:
        products = Product.objects.filter(
            name__icontains=product_name, status=False)

    if product_category != '' and product_category is not None:
        products = Product.objects.filter(
            category=product_category, status=False)

    return render(request, 'purplegorilla/index.html', {'products': products})


def user(request, user_id):

    # get orders that belongs to the buyer and also associated with the seller
    orders = Order.objects.filter(
        Q(user_id=user_id) | Q(product__user_id=user_id))
    products = Product.objects.filter(user_id=user_id)
    return render(request, 'user.html', {'products': products, 'orders': orders})


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'image', 'description', 'category', 'price']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # form.instance is the product
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'image', 'description', 'category', 'price']


class ProductDelete(DeleteView):
    model = Product
    success_url = '/products'


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})


def signup(request):
    # Handle the POST request
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-index')
        else:
            error_message = 'Invalid sign up - try again'
    # Handle the GET request (render the form)
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})


class Home(LoginView):
    template_name = 'home.html'
