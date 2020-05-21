from django.shortcuts import render
from django.http import *
from .forms import ContactForm, ConnexionForm, CreateNewDemande, CollectiviteForm, CreateNewProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Demande, Product, Compte, Collectivite, Item, Membre
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext 
from matplotlib.backends.backend_agg import FigureCanvasAgg

import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

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
    nbProduits = len(Product.objects.all())
    nbDemandes = len(Demande.objects.all())
    nbCollectivite = len(Collectivite.objects.all())
    c = Compte.objects.all()
    return render(request, 'forms/tableau_de_bord.html', locals())

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
    f = plt.figure()
    abscisse = np.arange(10)
    ordonnee = [0,1,2,3,5,6,10,23,43,65]
    plt.title('Title')
    plt.xlim(0, 10)
    plt.ylim(0, 70)
    plt.xlabel('Temps (jours)')
    plt.ylabel('Nombre de clients inscrits')
    bar1 = plt.plot(abscisse,ordonnee,color='Green')

    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    matplotlib.pyplot.close(f)
    return response