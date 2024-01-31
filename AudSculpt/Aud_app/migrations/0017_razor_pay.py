# Generated by Django 4.2.7 on 2023-12-19 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aud_app', '0016_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='razor_pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razopay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razopay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='razor_pay', to='Aud_app.order')),
            ],
        ),
    ]