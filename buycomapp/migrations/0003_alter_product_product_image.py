# Generated by Django 4.0.3 on 2022-04-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycomapp', '0002_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product_image', verbose_name='Product_image'),
        ),
    ]
