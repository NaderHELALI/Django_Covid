from django.contrib import admin

# Register your models here.
from .models import Compte, Demande, Product, Item,Collectivite

admin.site.register(Compte)
admin.site.register(Demande)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Collectivite)