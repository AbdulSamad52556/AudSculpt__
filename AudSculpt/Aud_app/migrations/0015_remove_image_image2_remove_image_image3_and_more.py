# Generated by Django 4.2.7 on 2023-12-16 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aud_app', '0014_order_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image4',
        ),
    ]