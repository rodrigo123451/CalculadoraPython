"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, despedida, dameFecha, calculaEdad
from Proyecto1.views1 import fibonacci, saludo1, saludo2, calcu, fibonacci, par, factorial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('fecha/',dameFecha),
    path('edad/<int:agno>', calculaEdad),
    #-----------------------------vista2-------
    path('saludo1/', saludo1),
    path('saludo2/', saludo2),
    path('calculadora/', calcu),
    path('fibonacci/', fibonacci),
    path('par/', par),
    path('factorial/', factorial),
    
    
    
    
]
