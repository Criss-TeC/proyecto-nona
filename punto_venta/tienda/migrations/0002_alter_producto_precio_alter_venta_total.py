# Generated by Django 5.0.6 on 2024-07-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
