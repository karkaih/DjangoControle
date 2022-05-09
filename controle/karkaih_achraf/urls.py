from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comptes', views.comptes),
    path('details/<int:code>', views.details),
    path('operations/<int:code>', views.operations),
    path('search', views.search),
    path('searchCompte', views.search_Comptes),
    path('createClient', views.ClientF),
    path('createComptes', views.CompteF),
    path('createOperation', views.OperationF),

]
