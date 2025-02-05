from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'required': True,
                'pattern': '^[a-zA-Z 0-9]+@utez\.edu\.mx$',
                'minlength': 5,
                'title': 'Debes ingresar un correo de la UTEZ',
                
            }
        ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': True,
                    'title': 'Ingresa tu nombre',
            }
        ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'required': True,
                    'title': 'Ingresa tu apellido',                
            }
        ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de control',
                    'required': True,
                    'minlength': 8,
                    'title': 'Ingresa tu número de control',
            }
        ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'title': 'Ingresa tu edad',
                }
        ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'title': 'Ingresa tu teléfono',
                    'minlength': 10,
            }
        ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                    'pattern': '^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]){8,}$',
                    'title': 'Ingresa una contraseña',
            }
        ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirmar contraseña',
                    'required': True,
                    'title': 'Confirma tu contraseña',
            }
        ),
    }


class CustomUserLoginForm(AuthenticationForm):
    pass