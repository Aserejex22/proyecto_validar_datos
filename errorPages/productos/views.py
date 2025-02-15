from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm

#Metodo que devuelve el JSON
def lista_productos(request):
    productos = Producto.objects.all()

    #Contruir una variable en formato de diccionario porque el JSONResponse lo requiere
    data = [
        {
            #Objeto producto construido al aire
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    #Devolver la respuesta en JSON
    return JsonResponse(data, safe=False)

#Funcion para mandar a la vista del form
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})
