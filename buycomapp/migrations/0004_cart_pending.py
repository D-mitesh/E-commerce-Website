# Generated by Django 4.0.3 on 2022-04-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycomapp', '0003_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
