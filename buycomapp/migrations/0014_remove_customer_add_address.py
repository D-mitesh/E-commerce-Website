# Generated by Django 4.0.3 on 2022-05-10 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buycomapp', '0013_remove_customer_ship_diff_customer_is_selected_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='add_address',
        ),
    ]
