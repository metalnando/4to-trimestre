from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='Home'),
    path('CRUD/crear/', views.Crear, name='crear'),
    path('CRUD/editar/<int:producto_id>/', views.editar, name='editar'),
    path('CRUD/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('vender/', views.vender, name='vender'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('pagar/', views.pagar, name='pagar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

