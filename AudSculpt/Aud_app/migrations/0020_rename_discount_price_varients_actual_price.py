# Generated by Django 4.2.7 on 2023-12-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aud_app', '0019_product_discount_varients_discount_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='varients',
            old_name='discount_price',
            new_name='actual_price',
        ),
    ]
