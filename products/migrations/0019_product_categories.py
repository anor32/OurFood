# Generated by Django 5.0.13 on 2025-05-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products_categories', to='products.category'),
        ),
    ]
