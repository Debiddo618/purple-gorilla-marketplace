from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORIES = (
    ('G', 'Generic'),
    ('E', 'Electronics'),
    ('F', 'Fashion'),
    ('H&F', 'Home and Furnitures'),
    ('B&H', 'Beauty and Health'),
    ('B&M', 'Books and Media'),
    ('S&O', 'Sports and Outdoor'),
    ('T&B', 'Toys and Baby Products'),
    ('F&B', 'Food and Beverages')
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=250)
    category = models.CharField(
        max_length=3,
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
