# Generated by Django 5.0.6 on 2024-07-08 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_producto_precio_alter_venta_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='cantidad',
            new_name='cantidad_vendida',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
    ]
