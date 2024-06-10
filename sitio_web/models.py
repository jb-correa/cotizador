from django.db import models
from django.forms import ModelForm

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    fecha=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        db_table='productos'

    def __str__(self):
        return self.nombre
    
class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=["nombre"]

class Precios(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    lista = models.CharField(max_length=500)
    fecha=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name='Precio'
        verbose_name_plural='Precios'
        db_table='precios'

    def __str__(self):
        return f'Precios del {self.producto.nombre}' 
    
class PreciosForm(ModelForm):
    class Meta:
        model=Precios
        fields=[ "lista"]    
    
