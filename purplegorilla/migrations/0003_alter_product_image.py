# Generated by Django 5.0.6 on 2024-06-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purplegorilla", "0002_remove_product_price1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.CharField(
                default="https://i.imgur.com/DTQfCw5.png", max_length=250
            ),
        ),
    ]
