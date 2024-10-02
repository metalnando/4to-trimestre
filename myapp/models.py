from django.db import models

# Create your models here.
class Producto(models.Model):
    Marca = models.CharField(max_length=225)
    Cantidad = models.IntegerField() 
    Precio = models.DecimalField(max_digits=10, decimal_places=2)  
    Tipo = models.CharField(max_length=225)
    Talla = models.CharField(max_length=225)

    def __str__(self):
        return f"Marca: {self.Marca}, Cantidad: {self.Cantidad}, Precio: {self.Precio}, Tipo: {self.Tipo}, Talla: {self.Talla}"


class Cliente(models.Model):
    Nombre=models.CharField(max_length=225)
    Celular=models.CharField(max_length=225)
    Direccion=models.CharField(max_length=225)
    Correo=models.CharField(max_length=225)

    def __str__(self):
        return self.Nombre
    
class inventario(models.Model):
    Codigo=models.CharField(max_length=225)
    Producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Inventario: {self.Codigo}, Producto: {self.Producto.Marca}"
    
class Venta(models.Model):
    Factura=models.CharField(max_length=225)
    Producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    Cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Venta: {self.Factura}, Producto: {self.Producto.Marca}, Cliente: {self.Cliente.Nombre}"