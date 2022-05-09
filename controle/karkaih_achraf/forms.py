from django import forms
from django.db.models import Choices

from .models import Compte, Client


class ClientForm(forms.Form):
    code = forms.IntegerField(label='Code')
    nom = forms.CharField(label='Nom')
    prenom = forms.CharField(label='Prenom')


class ComptesForm(forms.Form):
    id = forms.IntegerField(label='ID')
    numero = forms.IntegerField(label='Numero')
    date_creation = forms.DateField(label='Date')
    solde = forms.FloatField(label='solde')
    client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select)


class OperationsForm(forms.Form):
    numOperation = forms.IntegerField(label='Numero_Operation')
    types = (
        ("Retrait", "Retrait"),
        ("Virsement", "Virsement"),
    )
    type = forms.ChoiceField(label='Types', choices=types)
    dateOperation = forms.DateField(label='Date_Operations')
    montant = forms.FloatField(label='Montant')
    compte = forms.ModelChoiceField(queryset=Compte.objects.all(), widget=forms.Select)
    client_op = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select)
