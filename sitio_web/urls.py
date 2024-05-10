from django.contrib import admin
from django.urls import path
from sitio_web import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('resultado',views.async_view, name="Resultado"),
    path('async', views.async_view, name="Async"),

]
