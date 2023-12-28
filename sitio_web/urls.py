from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.home, name="Home"),
    path('resultado', views.resultado, name="Resultado"),
    path('loading', views.busqueda, name="Loading")
]