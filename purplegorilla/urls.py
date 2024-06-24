from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products', views.index, name='product-index'),
    path('user/<int:user_id>', views.user, name='user'),
    path('product/create', views.ProductCreate.as_view(), name="product-create"),
    path('product/<int:pk>/update',
         views.ProductUpdate.as_view(), name="product-update"),
    path('products/<int:pk>/delete/',
         views.ProductDelete.as_view(), name='product-delete'),
    path('product/<int:product_id>', views.product_detail, name="product-detail"),
    path('order/<int:product_id>', views.confirm_order, name="order-confirm"),
    path('order/<int:pk>/delete', views.OrderDelete.as_view(), name="order-delete"),
    path('order/<int:order_id>/detail', views.order_update, name="order-detail"),
    path('order/create/<int:user_id>/<int:product_id>',
         views.order_create, name="order-create"),
    path('accounts/signup/', views.signup, name='signup'),

]
