from django.db import models

class Detalles_Producto(models.Model):
    descripcion = models.TextField(max_length=400)
    fecha_calidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

from categorias.models import Categoria

#Campos para relaciones
#OneToOneField ===> 1:1
#ForeignKey ===> 1:M
#ManyToManyField ===> M:M <----- Django genera automaticamente la tabla de interseccion
class Producto(models.Model):
    #Atributos de la clase
        #Mandar a construir un campo de los modelos de Django
    nombre = models.CharField(max_length=100) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    #Relacion de 1:1
    detalles_producto = models.OneToOneField(
        Detalles_Producto,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    #Relacion de 1:M
    categoria = models.ForeignKey(
        Categoria,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    #Relacion de M:M
    proveedores = models.ManyToManyField(
        Proveedor,
        #through='ProductoProveedor', Para uncluir campos nuevos
        null=True,
        blank=True
        )

    def __str__(self):
        return self.nombre
