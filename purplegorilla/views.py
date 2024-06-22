from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        products = Product.objects.filter(name__icontains=product_name)
    return render(request, 'purplegorilla/index.html', {'products': products})


def base(request):
    return render(request, 'base.html')


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


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})


def signup(request):
    # Handle the POST request
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # STEP 1: Create a user in the databse from the UserCreationForm
            login(request, user)  # STEP 2: Log in as the craeted user
            return redirect('product-index')
        else:
            error_message = 'Invalid sign up - try again'
    # Handle the GET request (render the form)
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})


class Home(LoginView):
    template_name = 'home.html'
