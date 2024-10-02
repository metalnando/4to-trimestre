# myapp/signals.py

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Producto

@receiver(post_delete, sender=Producto)
def reorder_ids(sender, instance, **kwargs):
    productos = Producto.objects.all().order_by('id')
    for index, producto in enumerate(productos, start=1):
        if producto.id != index:
            producto.id = index
            producto.save()

