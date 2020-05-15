"""formulaire_foyer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('forms/', include('forms.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from forms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', views.accueil),
    path('contact/', views.contact, name="contact"),
    path('collectivite/', views.collectivite),
    path('connexion/', views.connexion),
    path('', include("django.contrib.auth.urls")),
    path('deconnexion/', views.deconnexion),
    path('tableau_de_bord/', views.tableau_de_bord),
    path('<int:id>/create/', views.create),
    path("<int:id>/<int:idc>", views.index, name="index"),
    path('<int:id>/choix/', views.choix),
    path('graphe/', views.graphe),
    path('product/', views.product),
    path("<int:id>/demandes", views.demandes),
    path("<int:id>/membres", views.membres),
              ]
              
