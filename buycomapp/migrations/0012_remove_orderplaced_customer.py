# Generated by Django 4.0.3 on 2022-04-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buycomapp', '0011_alter_orderplaced_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='customer',
        ),
    ]
