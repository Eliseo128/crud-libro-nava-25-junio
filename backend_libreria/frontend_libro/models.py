from django.db import models

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=150)
    precio = models.IntegerField()
    autor = models.CharField(max_length=100)