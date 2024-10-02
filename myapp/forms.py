from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_agregar(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'Precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'Talla': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, help_text='')

    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        help_text='',
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput,
        strip=False,
        help_text='',
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")