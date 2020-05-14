from django.shortcuts import render
from django.http import *
from .forms import ContactForm
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Demande, Product, Compte
from .forms import CreateNewDemande
from django.http import HttpResponse, HttpResponseRedirect

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
            nombre = form.cleaned_data['nombre']
            membre1 = form.cleaned_data['membre1']
            membre2 = form.cleaned_data['membre2']  
            membre3 = form.cleaned_data['membre3']  
            membre4 = form.cleaned_data['membre4']  
            membre5 = form.cleaned_data['membre5']  
            membre6 = form.cleaned_data['membre6']  
            c = Compte(nom = nom, email = email, mot_de_passe = mot_de_passe, numero_tel = numero_tel, adresse = adresse, nombre = nombre, membre1 = membre1, membre2 = membre2, membre3 = membre3, membre4 = membre4, membre5 = membre5, membre6 = membre6)
            c.save()
        return HttpResponseRedirect("/connexion")
    else:
        form = ContactForm()
        return render(request, 'forms/contact.html', locals())

def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            c = Compte.objects.get(email = email)
            if mot_de_passe == c.mot_de_passe:
                return HttpResponseRedirect("/choix")
    else:
        form = ConnexionForm()
    return render(request, 'forms/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return render(request, 'forms/deconnexion.html', locals())

def tableau_de_bord(request):
    return render(request, 'forms/tableau_de_bord.html', locals())

def index(response, id):
	d = Demande.objects.get(id=id)
	allproducts = Product.objects.all()
	if response.method == "POST":
		print(response.POST)
		if response.POST.get("newProduct"):
			name = response.POST.get("name")
			d.produits.add(Product.objects.get(name=name))
	return render(response, "forms/list.html", {"d":d, "allproducts":allproducts})


def create(response):
	if response.method == "POST":
		form = CreateNewDemande(response.POST)

		if form.is_valid():
			t = form.cleaned_data["type"]
			d = Demande(type=t)
			d.save()
		return HttpResponseRedirect("/%i" %d.id)
	else:
		form = CreateNewDemande()
		return render(response, "forms/create.html", {"form" : form})

def choix(request):
    return render(request, 'forms/choix.html', locals())