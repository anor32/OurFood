# Generated by Django 5.0.13 on 2025-06-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_remove_product_composition_product_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='composition',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='composition'),
        ),
    ]
