# Generated by Django 5.1.1 on 2024-09-27 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_producto_id_alter_producto_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='orden',
        ),
    ]
