from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('product/create', views.ProductCreate.as_view(), name="product-create")
]
