# Generated by Django 5.1.1 on 2024-09-26 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=225)),
                ('Celular', models.CharField(max_length=225)),
                ('Direccion', models.CharField(max_length=225)),
                ('Correo', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=225)),
                ('Cantidad', models.CharField(max_length=225)),
                ('Precio', models.CharField(max_length=225)),
                ('Tipo', models.CharField(max_length=225)),
                ('Talla', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=225)),
                ('Producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factura', models.CharField(max_length=225)),
                ('Cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.cliente')),
                ('Producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.producto')),
            ],
        ),
    ]
