from django.db import models

# Create your models here.
class Pelicula(models.Model):

    titulo=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    duracion = models.IntegerField()


class Actor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad=models.IntegerField()

class Director(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)