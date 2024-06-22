from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products', views.index, name='product-index'),
    path('base', views.base, name='base'),
    path('product/create', views.ProductCreate.as_view(), name="product-create"),
    path('product/<int:pk>/update',
         views.ProductUpdate.as_view(), name="product-update"),
    path('product/<int:product_id>', views.product_detail, name="product-detail"),
    path('accounts/signup/', views.signup, name='signup'),

]
