# Generated by Django 4.0.3 on 2022-05-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buycomapp', '0002_alter_orderplaced_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='ordered_date',
            field=models.DateField(null=True, verbose_name='Order date'),
        ),
    ]