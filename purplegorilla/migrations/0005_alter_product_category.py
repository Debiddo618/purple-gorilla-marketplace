# Generated by Django 5.0.6 on 2024-06-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purplegorilla", "0004_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("G", "Generic"),
                    ("E", "Electronics"),
                    ("F", "Fashion"),
                    ("HF", "Home and Furnitures"),
                    ("BH", "Beauty and Health"),
                    ("BM", "Books and Media"),
                    ("SO", "Sports and Outdoor"),
                    ("TB", "Toys and Baby Products"),
                    ("FB", "Food and Beverages"),
                ],
                default="G",
                max_length=2,
            ),
        ),
    ]
