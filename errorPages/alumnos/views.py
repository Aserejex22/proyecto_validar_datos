from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets#Vamos a crear una vista de varias al mismo tiempo
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

class AlumnoViewSet(viewsets.ModelViewSet):
    #1)Permitir sabes a que objeto hace referencia
    queryset = Alumno.objects.all()

    #2)Serializar los objetos
    serializer_class = AlumnoSerializer

    #3)Renderizar las respuestas
    renderer_classes = [JSONRenderer]

    #4)Establecer que metodos puedo usar
    #http_method_names = ['GET', 'POST']

def formulario(request):
    return render(request, 'Hernandez_Adrian.html')