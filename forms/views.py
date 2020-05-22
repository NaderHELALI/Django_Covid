from django.shortcuts import render
from django.http import *
from .forms import ContactForm, ConnexionForm, CreateNewDemande, CollectiviteForm, CreateNewProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Demande, Product, Compte, Collectivite, Item, Membre
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext 
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.db import connection
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import sqlite3
import pandas as pd
from matplotlib.figure import Figure
from datetime import datetime, timedelta
import folium
import json
import branca
import requests




def accueil(request):
    return render(request, 'forms/accueil.html', locals())
    #return HttpResponse("""<h1>Bienvenue sur le formulaire de collectivité !</h1>
    #""")

#def titre(request):
#    return HttpResponse("""<h1>Formulaire de création d'un compte</h1>
#    """)
    
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid(): 
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            numero_tel = form.cleaned_data['numero_tel']
            adresse = form.cleaned_data['adresse']
            ville = form.cleaned_data['ville']
            c = Compte(nom = nom, email = email, mot_de_passe = mot_de_passe, numero_tel = numero_tel, adresse = adresse, ville=ville)
            c.save()
        return HttpResponseRedirect("/%i/membres" %c.id)
    else:
        form = ContactForm()
        return render(request, 'forms/contact.html', locals())

def membres(response, id):
    c = Compte.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("newMembre"):
            nom = response.POST.get("nom")
            m=Membre(nom=nom)
            m.save()
            c.membres.add(m)
        c.save()
    return render(response, "forms/membres.html", locals())

def collectivite(request):
    if request.method == "POST":
        form = CollectiviteForm(request.POST or None)
        if form.is_valid(): 
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            numero_tel = form.cleaned_data['numero_tel']
            ville = form.cleaned_data['ville'] 
            c = Collectivite(nom = nom, email = email, mot_de_passe = mot_de_passe, numero_tel = numero_tel, ville = ville)
            c.save()
        return HttpResponseRedirect("/connexion")
    else:
        form = CollectiviteForm()
        return render(request, 'forms/collectivite.html', locals())

def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            collectivite = form.cleaned_data['collectivite']
            if collectivite:
                c = Collectivite.objects.get(email = email)
                if mot_de_passe == c.mot_de_passe:
                    return HttpResponseRedirect("/tableau_de_bord")
            else:   
                c = Compte.objects.get(email = email)
                if mot_de_passe == c.mot_de_passe:
                    return HttpResponseRedirect("/%i/choix" %c.id)
    else:
        form = ConnexionForm()
    return render(request, 'forms/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return render(request, 'forms/deconnexion.html', locals())

def tableau_de_bord(request):
    nbMembres = len(Membre.objects.all())
    nbProduits = len(Product.objects.all())
    nbDemandes = len(Demande.objects.all())
    nbCollectivite = len(Collectivite.objects.all())
    
    return render(request,'forms/tableau_de_bord.html', locals())

def tableau_de_bord_membres(request):
    c = Compte.objects.filter(date_inscription__lte=datetime.now() + timedelta(days=7))
    return render(request,'forms/tableau_de_bord_membres.html', locals())
     
def index(response, id, idc):
    d = Demande.objects.get(id=idc)
    c = Compte.objects.get(id=id)
    allproducts = Product.objects.all()
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("newProduct"):
            name = response.POST.get("name")
            product = Product.objects.get(name=name)
            quantity = response.POST.get("quantity")
            i=Item(product=product,quantity=int(quantity))
            i.save()
            d.items.add(i)
        d.save()   
            
    return render(response, "forms/list.html", locals())


def create(response,id):
    if response.method == "POST":
        form = CreateNewDemande(response.POST)

        if form.is_valid():
            c = Compte.objects.get(id=id)
            t = form.cleaned_data["type"]
            d = Demande(type=t)
            d.save()
            c.demandes.add(d)
            c.save()

        return HttpResponseRedirect("/%i/demandes" %c.id)
    else:
        form = CreateNewDemande()
        return render(response, "forms/create.html", locals())

def demandes(request, id):
    c = Compte.objects.get(id=id)
    return render(request, 'forms/demandes.html', locals())

def product(response):
    if response.method == "POST":
        form = CreateNewProduct(response.POST)

        if form.is_valid():
            t = form.cleaned_data["type"]
            n = form.cleaned_data["name"]
            u = form.cleaned_data["unit"]
            p = Product(type=t,name=n, unit=u)
            p.save()
        return HttpResponseRedirect("/product")
    else:
        form = CreateNewProduct()
        return render(response, "forms/product.html", {"form" : form})

def choix(request,id):
    c = Compte.objects.get(id=id)
    nbDemandes = len(c.demandes.all())
    return render(request, 'forms/choix.html', locals())
def graphe(request):
   
    return request



def stat1(request):
    f = plt.figure()
    co = sqlite3.connect('./db.sqlite3')
    data = pd.read_sql_query('SELECT DISTINCT(type),count(type) FROM forms_demande GROUP BY type;',co)
    df = pd.DataFrame(data)
    f, ax = plt.subplots()
   
    df.plot(kind = 'bar', color = 'firebrick',ax=ax, x = 'type',figsize=(11,11), title = "Nombre de commandes par type de produits" )
    plt.xlabel('Type de produits')
    plt.ylabel("Nombre de commandes")
    plt.legend('')
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    plt.close(f)
    #plt.savefig('output.png')
    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image\png')
    canvas.print_png(response)
    plt.close(f)
    return response

def stat2(request):
    f = Figure()
    co = sqlite3.connect('./db.sqlite3')
    data = pd.read_sql_query('SELECT count(nom), ville FROM forms_compte GROUP BY nom;',co)
    df = pd.DataFrame(data)
    f, ax = plt.subplots()
    df.plot(kind = 'bar', color = 'gold',ax=ax, x = 'ville',figsize=(11,11), title = "Nombre de foyers par ville" )
    plt.xlabel('Ville')
    plt.ylabel("Nombre de foyers")
    plt.legend('')
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image\jpg')
    canvas.print_jpg(response)
    plt.close(f)
    return response

def stat3(request):
    f = Figure()
    co = sqlite3.connect('./db.sqlite3')
    data = pd.read_sql_query('SELECT count(date_demande),date_demande FROM forms_demande GROUP BY date_demande;',co)
    df = pd.DataFrame(data)
    f, ax = plt.subplots()
    df.plot(kind = 'bar', color = 'limegreen',ax=ax, x = 'date_demande',figsize=(11,11), title = "Nombre de commandes par jour" )
    plt.xlabel('Date')
    plt.ylabel("Nombre de commandes")
    plt.legend('')
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image\jpg')
    canvas.print_jpg(response)
    plt.close(f)
    return response



def map(request):
    #Pour la répartion on a utilisé des données autre que celle dans la base de donnée 
    
    """
    # Créer la Map en zoomant sur la France
    m = folium.Map(location=[45, 1], zoom_start=6)

    # Récupère les données des communes
    state_geo = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departementartements.geojson'
            
    print(state_geo)
    # Récupère les données de la base de donnée
    co = sqlite3.connect('./db.sqlite3')
    data = pd.read_sql_query('SELECT departement FROM `forms_compte`;',co)
    print(data)
    
    # Nb Personne par departement
    g1 = data.groupby(["departement"]).size().reset_index(name='Number of people')
    g1.set_index('departement')
    print(g1)
    


    g1['departement']=g1['departement'].astype(str)
    print(g1['departement'].dtypes)
    a=max(g1['Number of people'])
    bins = [0,0.25*a,0.5*a,0.75*a,a]
    print(bins)

    choropleth=folium.Choropleth(
        geo_data=state_geo,
        name='Nb membres',
        data=g1,
        columns =['departement','Number of people'],
        key_on='feature.properties.code',
        fill_color='BuPu',
        fill_opacity=0.7,
        line_opacity=0.5,
        highlight=True,
        legend_name='Nombres de foyer enregistrée',
        bins=bins,
        ).add_to(m)


    

    m.save(".forms/a_departement.html")
    
    
    """
    
    return render(request,  'forms/a_departement.html')
