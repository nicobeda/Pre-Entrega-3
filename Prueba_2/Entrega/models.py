from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombre= models.CharField(max_length=15)
    email=models.EmailField(max_length=15)


class   Clientes(models.Model):
    nombre= models.CharField(max_length=15)
    edad=models.IntegerField()


class Locales(models.Model):
    calle= models.CharField(max_length=15)
    altura=models.IntegerField()
