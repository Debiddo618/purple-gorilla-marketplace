from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('product-index')
