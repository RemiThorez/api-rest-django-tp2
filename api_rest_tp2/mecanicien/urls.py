from django.urls import path,include
from .views import obtenir,obtenirTout,ajouter,supprimer,modifier,connexion
from rest_framework import routers

urlpatterns =[
    path(r"obtenir/<int:idMecanicien>",obtenir,name="obtenir-mecanicien"),
    path(r"obtenirTout/",obtenirTout,name="obtenir-mecaniciens"),
    path(r"ajouter/",ajouter,name="ajouter-mecanicien"),
    path(r"supprimer/<int:idMecanicien>",supprimer,name="supprimer-mecanicien"),
    path(r"modifier/",modifier,name="modifier-mecanicien"),
    path(r"connexion/",connexion,name="connexion-mecanicien"),
]