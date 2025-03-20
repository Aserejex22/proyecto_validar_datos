from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets#Vamos a crear una vista de varias al mismo tiempo
from rest_framework.renderers import JSONRenderer
from .forms import ProductoForm
from django.shortcuts import render
    
def agregar_producto(request):
    form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})

class ProductoViewSet(viewsets.ModelViewSet):
    #1)Permitir sabes a que objeto hace referencia
    queryset = Producto.objects.all()

    #2)Serializar los objetos
    serializer_class = ProductoSerializer

    #3)Renderizar las respuestas
    renderer_classes = [JSONRenderer]

    #4)Establecer que metodos puedo usar
    #http_method_names = ['GET', 'POST']

