# Django_Covid
Pour faire fonctionner la plateforme, 
il suffit de taper ces commandes 
dans l'invité de commandes.

Déplacez vous dans le répertoire formulaire_foyer
grâce à la commande cd

1) pip install -r requirements.txt
2) python manage.py makemigrations
3) python manage.py migrate
4) python manage.py runserver

Ouvrez un navigateur et entrez l'adresse :
http://127.0.0.1:8000/


Afin d'avoir accès à la partie administrateur,
il suffit de taper cette commande dans l'invité
de commandes:

python manage.py createsuperuser

et de suivre les instructions,
puis accéder à la page :

http://127.0.0.1:8000/admin/login/?next=/admin/
