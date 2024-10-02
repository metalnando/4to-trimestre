from django.contrib import admin
from .models import Producto,Cliente,inventario,Venta

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(inventario)
admin.site.register(Venta)