# Generated by Django 4.2.7 on 2023-12-03 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aud_app', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercart', to=settings.AUTH_USER_MODEL),
        ),
    ]
