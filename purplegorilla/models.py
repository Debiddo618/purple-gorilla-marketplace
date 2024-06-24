from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal


CATEGORIES = (
    ('G', 'Generic'),
    ('E', 'Electronics'),
    ('F', 'Fashion'),
    ('HF', 'Home and Furnitures'),
    ('BH', 'Beauty and Health'),
    ('BM', 'Books and Media'),
    ('SO', 'Sports and Outdoor'),
    ('TB', 'Toys and Baby Products'),
    ('FB', 'Food and Beverages')
)

STATUS = (
    ('Pending', 'Pending'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    image = models.CharField(
        max_length=250,
        default='https://i.imgur.com/DTQfCw5.png'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-index')

    def total_before_tax(self):
        return self.price + 10

    def estimated_tax(self):
        tax_rate = Decimal('0.06')
        return (self.price + 10) * tax_rate

    def total_price(self):
        tax_rate = Decimal('0.06')
        return self.price + 10 + (self.price + 10) * tax_rate


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
