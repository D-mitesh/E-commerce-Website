# Generated by Django 4.0.3 on 2022-04-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycomapp', '0004_cart_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(null=True, verbose_name='total_price'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pending',
            field=models.BooleanField(default=True),
        ),
    ]
