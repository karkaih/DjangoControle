from django.db import models

# Create your models here.


class Client(models.Model):
    code = models.IntegerField(primary_key=True, max_length=100)
    nom = models.CharField(max_length=10, blank=True, null=True)
    prenom = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.nom)


class Compte(models.Model):
    id = models.IntegerField(primary_key=True, max_length=100)
    numero = models.IntegerField(max_length=100)
    date_creation = models.DateField()
    solde = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Operations(models.Model):
    numOperation = models.IntegerField(primary_key=True, max_length=100)
    type = models.CharField(max_length=10, blank=True, null=True)
    dateOperation = models.DateField()
    montant = models.FloatField()
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    client_op = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numOperation)

