# Generated by Django 4.2.7 on 2023-12-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aud_app', '0004_image_code_product_code_varients_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image2',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='image',
            name='image3',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='image',
            name='image4',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
