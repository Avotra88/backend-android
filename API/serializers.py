from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id' ,'reference', 'designation', 'prixU', 'quantite')

class ClientSerializer(serializers.ModelSerializer):
    produits = ProduitSerializer(many=True,read_only=True)
    class Meta:
        model = Client
        fields = ('id','nom', 'prenom','email','telephone','adresse','produits')

class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achat
        fields = ('id','date_Achat', 'quantite', 'client', 'produit')
