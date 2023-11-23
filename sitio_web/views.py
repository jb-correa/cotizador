from django.shortcuts import render

from django.db import models
from django.shortcuts import render

def home(request):

    return render(request, 'sitio_web/home.html') 