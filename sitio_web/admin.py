from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "nombre", "precios", "precio_promedio")
    

admin.site.register(Producto, ProductoAdmin)
