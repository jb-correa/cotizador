import json
from django.db import models
from django.forms import ModelForm

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio_promedio=models.FloatField(null=True)
    precio_maximo=models.FloatField(null=True)
    precio_minimo=models.FloatField(null=True)  
    created=models.DateField(auto_now_add=True)  
    precios = models.FloatField(max_length=200, null=True)

    def set_precios(self, x):
        self.precios = json.dumps(x)

    def set_precios(self):
        return json.loads(self.precios)
    class Meta:
        db_table='productos'
        ordering=['created']
        verbose_name='producto'
        verbose_name_plural='productos'
    def __str__(self):
        return f'Busqueda del producto {self.nombre}, de la fecha {self.created}'
    

class productoForm(ModelForm):
    class Meta:
        model=Producto
        fields=['nombre',]
    
