from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import form_agregar, RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def Home(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'index.html', {"prod": productos})

def Crear(request):
    if request.method == 'POST':
        formulario = form_agregar(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('Home')
        else:
            messages.error(request, "Error al crear el producto. Verifica los datos ingresados.")
    else:
        formulario = form_agregar()
    return render(request, 'Crud/Crear.html', {'formulario': formulario})

def editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        formulario = form_agregar(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('Home')
        else:
            messages.error(request, "Error al actualizar el producto. Verifica los datos ingresados.")
    else:
        formulario = form_agregar(instance=producto)
    return render(request, 'Crud/Editar.html', {'formulario': formulario, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado.")
        return redirect('Home')
    return render(request, 'Crud/Eliminar.html', {'producto': producto})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect('Home')
        else:
            messages.error(request, "Error en el registro. Verifica los datos.")
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f"Bienvenido {usuario.username}")
            return redirect('Home')
        else:
            messages.error(request, "Error en el inicio de sesión.")
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def vender(request):
    productos = Producto.objects.all()
    total_precio = 0
    if request.method == 'POST':
        selected_ids = request.POST.getlist('productos')
        total_precio = sum(Producto.objects.filter(id__in=selected_ids).values_list('precio', flat=True))
    return render(request, 'myapp/vender.html', {'productos': productos, 'total_precio': total_precio})

def pagar(request):
    
    return render(request, 'myapp/pagar.html')


def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('Home')