# Generated by Django 5.0.6 on 2024-06-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purplegorilla", "0003_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
