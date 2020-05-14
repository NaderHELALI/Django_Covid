from django.db import models

from .forms import type_choices

class Type(models.Model):
    type = models.CharField(max_length=200, choices=type_choices)

    def __str__(self):
        return self.type

    
# Create your models here.s
class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    
class Demande(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    produits = models.ManyToManyField(Product)
    def __str__(self):
        return self.type



class Compte(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    membre1 = models.CharField(max_length=100)
    membre2 = models.CharField(max_length=100)
    membre3 = models.CharField(max_length=100)
    membre4 = models.CharField(max_length=100)
    membre5 = models.CharField(max_length=100)
    membre6 = models.CharField(max_length=100)
    def __str__(self):
        return self.nom