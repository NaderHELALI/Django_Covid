from django.db import models

# Create your models here.

type_choices = (
    ("Nourriture", u"Nourriture"),
    ("Hygiène", u"Hygiène"),
    ("Nettoyage", u"Nettoyage")
    )

class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    type = models.CharField(max_length=200,default="Nourriture", choices=type_choices)
    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product, related_name='product',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, default=2)
    
    def __str__(self):
        return self.product.name+' '+str(self.quantity)

class Demande(models.Model):
    type = models.CharField(max_length=200,default="Nourriture", choices=type_choices)
    items= models.ManyToManyField(Item)
    date_demande = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.type)

class Membre(models.Model):
    nom=models.CharField(max_length=100)
    
class Compte(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    date_inscription = models.DateField(auto_now=True)
    membres = models.ManyToManyField(Membre)
    demandes = models.ManyToManyField(Demande)
    def __str__(self):
        return self.nom

class Collectivite(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)