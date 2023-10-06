"""
URL configuration for Prueba_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import inicio, clientes,locales,proveedores, buscar_clie


urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('clientes/', clientes, name="Clientes"),
    path('locales/', locales, name="Locales"),
    path('proveedores/', proveedores, name="Proveedores"),
    path('buscar_cliente/', buscar_clie, name="Buscar-Cliente")
]
