from rest_framework import serializers
from .models import Rendezvous

class RendezvousSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    cout = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True, required=False)
    duree = serializers.IntegerField(allow_null=True, required=False)
    commentaire = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Rendezvous
        fields = ('id','idVehicule','idMecanicien','besoins','etat','confirmer','date','heure','duree','commentaire','estPayer','cout')

class EnvoiInfoRendezvousSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="idVehicule.idClient.user.first_name")
    mecanicien = serializers.CharField(source="idMecanicien.user.first_name")
    infoVehicule = serializers.SerializerMethodField()
    idClient = serializers.IntegerField(source="idVehicule.idClient.id")
    cout = serializers.FloatField(allow_null=True, required=False)
    duree = serializers.IntegerField(allow_null=True, required=False)
    commentaire = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Rendezvous
        fields = ('id','idClient','client','mecanicien','infoVehicule','idVehicule','idMecanicien','besoins','etat','confirmer','date','heure','duree','commentaire','estPayer','cout')

    def get_infoVehicule(self, obj):
        vehicule = obj.idVehicule
        return f"{vehicule.annee} {vehicule.fabricant} {vehicule.modele}"

class NouveauRendezvousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rendezvous
        fields = ('id','idVehicule','idMecanicien','besoins','etat','confirmer','date','heure','duree','commentaire','estPayer','cout')