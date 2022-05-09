from django.contrib import admin

# Register your models here.
from .models import Compte, Operations, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
    pass


@admin.register(Operations)
class OperationsAdmin(admin.ModelAdmin):
    pass

