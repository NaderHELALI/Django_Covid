from django.db import models

type_choices = (
    (1, u"Nourriture"),
    (2, u"Hygiène"),
    (3, u"Nettoyage")
    )
# Create your models here
class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    type = models.IntegerField( null=True, choices=type_choices)
    def __str__(self):
        return self.name
    
class Item (models.Model):
    product = models.ForeignKey(Product, related_name='product',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, default=2)
    
    def __str__(self):
        return self.product.name+' '+str(self.quantity)
    
class Demande(models.Model):
    type = models.IntegerField(default=1, choices=type_choices)
    items= models.ManyToManyField(Item)
    def __str__(self):
        return str(self.type)



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