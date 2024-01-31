# Generated by Django 4.2.7 on 2023-12-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aud_app', '0018_alter_razor_pay_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='varients',
            name='discount_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='varients',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
