# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:57:42 2020

@author: sohan
"""

from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label = "Nom de famille du foyer", required = True)
    email = forms.EmailField(max_length=100, label="E-mail", required = True)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput,max_length=100, label = "Mot de passe", required = True)
    numero_tel = forms.CharField(max_length=100, label = "Numéro de téléphone", required=False)
    adresse = forms.CharField(widget=forms.Textarea, max_length=300, label = "Adresse du domicile", required = True)
    departement = forms.CharField(max_length=2, label = "Numéro de Dépatement", required = True)
    ville = forms.CharField(max_length=100, label="Ville", required=True)
    
class CollectiviteForm(forms.Form):
    nom = forms.CharField(max_length=100, label = "Nom", required = True)
    email = forms.EmailField(max_length=100, label="E-mail", required = True)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput,max_length=100, label = "Mot de passe", required = True)
    numero_tel = forms.CharField(max_length=100, label = "Numéro de téléphone", required=False)
    ville = forms.CharField(max_length=100, label = "Ville", required = True)

#    sujet = forms.CharField(max_length=100)
#    message = forms.CharField(widget=forms.Textarea)
#    envoyeur = forms.EmailField(label="Votre adresse e-mail")
#    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
class ConnexionForm(forms.Form):
    email = forms.EmailField(max_length=100, label="E-mail", required = True)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput,max_length=100, label = "Mot de passe", required = True)
    collectivite = forms.BooleanField(required= False)
    

class CreateNewDemande(forms.Form):
    type_choices = (
            ("Nourriture", u"Nourriture"),
            ("Hygiène", u"Hygiène"),
            ("Nettoyage", u"Nettoyage")
            )
    type = forms.ChoiceField(choices = type_choices)

class CreateNewProduct(forms.Form):
    type_choices = (
            (1, u"Nourriture"),
            (2, u"Hygiène"),
            (3, u"Nettoyage")
            )
    type = forms.ChoiceField(choices = type_choices,label="Type")
    name = forms.CharField(max_length=200,label="Nom du produit")
    unit = forms.CharField(max_length=200, label="Unité du produit")

    