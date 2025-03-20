from .models import Alumno
from django import forms

class AlumnoForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        widgets = {

        }