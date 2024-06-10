from django.contrib import admin
from sitio_web.models import Producto,  Precios


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("fecha", "nombre" )


class PreciosAdmin(admin.ModelAdmin):
    readonly_fields=("fecha", "lista", "producto")



admin.site.register(Producto, ProductoAdmin)
admin.site.register(Precios, PreciosAdmin)


