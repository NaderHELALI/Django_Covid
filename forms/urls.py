# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:18:25 2020

@author: sohan
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('deconnexion/', views.deconnexion),
    path('tableau_de_bord/', views.tableau_de_bord),
    path('create/', views.create),
    path("<int:id>", views.index, name="index"),
    path('choix/', views.choix),
    path('accueil/', views.accueil),
    path('contact/', views.contact),
    path('connexion/', views.connexion),
]
