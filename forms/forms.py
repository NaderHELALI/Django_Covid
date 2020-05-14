# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:57:42 2020

@author: sohan
"""

from django import forms

type_1 = 'Nourriture'
type_2 = 'Hygiène'
type_3 = 'Nettoyage'
type_choices = (
        (type_1, u"Nourriture"),
        (type_2, u"Hygiène"),
        (type_3, u"Nettoyage")
        )
class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label = "nom de famille du foyer", required = True)
    email = forms.EmailField(max_length=100, label="email", required = True)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput,max_length=100, label = "mot de passe", required = True)
    numero_tel = forms.CharField(max_length=100, label = "numéro de téléphone", required=False)
    adresse = forms.CharField(widget=forms.Textarea, max_length=300, label = "adresse du domicile", required = True)
    nombre = forms.ChoiceField(widget=forms.RadioSelect, choices = [("1", "1 membre"),("2", "2 membres"),("3", "3 membres"),("4", "4 membres"),("5", "5 membres"),("6", "6 membres"),("7", "7+ membres")], required = False)
    membre1 = forms.CharField(max_length=100, label = "prénom du premier membre du foyer", required = False)
    membre2 = forms.CharField(max_length=100, label = "prénom du deuxième membre du foyer", required = False)
    membre3 = forms.CharField(max_length=100, label = "prénom du troisième membre du foyer", required = False)
    membre4 = forms.CharField(max_length=100, label = "prénom du quatrième membre du foyer", required = False)
    membre5 = forms.CharField(max_length=100, label = "prénom du cinquième membre du foyer", required = False)
    membre6 = forms.CharField(max_length=100, label = "prénom du sixième membre du foyer", required = False)
    
#    sujet = forms.CharField(max_length=100)
#    message = forms.CharField(widget=forms.Textarea)
#    envoyeur = forms.EmailField(label="Votre adresse e-mail")
#    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
class ConnexionForm(forms.Form):
    email = forms.EmailField(max_length=100, label="email", required = True)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput,max_length=100, label = "mot de passe", required = True)

class CreateNewDemande(forms.Form):

    type = forms.ChoiceField(choices = type_choices)


    