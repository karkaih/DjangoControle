from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import ClientForm, ComptesForm, OperationsForm
from .models import Compte, Client, Operations


def index(request):
    clients = Client.objects.all()
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')

    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'clients': page_obj}

    return render(request, 'base.html', context)


def details(request, code):
    clients = Client.objects.get(code=code)
    context = {'client': clients}
    return render(request, 'details.html', context)


def operations(request, code):
    client = Client.objects.get(code=code)
    print("the code is = >" + client.nom)

    operations = Operations.objects.filter(client_op=client)
    context = {'operations': operations}
    return render(request, 'Operations.html', context)


def comptes(request):
    comptes = Compte.objects.all()
    paginator = Paginator(comptes, 10)
    page_number = request.GET.get('page')

    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'comptes': page_obj}

    return render(request, 'comptes.html', context)


def search(request):
    filteredClient = Client.objects.filter(nom__icontains=request.GET.get("search", ""))
    paginator = Paginator(filteredClient, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'clients': page_obj}
    return render(request, "base.html", context)


def search_Comptes(request):
    filteredComptes = Compte.objects.filter(id__icontains=request.GET.get("search", ""))
    paginator = Paginator(filteredComptes, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'comptes': page_obj}
    return render(request, "comptes.html", context)


def ClientF(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            code = request.POST.get("code", "")
            nom = request.POST.get("nom", "")
            prenom = request.POST.get("prenom", "")
            client = Client.objects.create(code=code, nom=nom, prenom=prenom)
            client.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientForm()

    return render(request, 'FormClient.html', {'form': form})


def CompteF(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ComptesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            id = request.POST.get("id", "")
            numero = request.POST.get("numero", "")
            date_creation = request.POST.get("date_creation", "")
            solde = request.POST.get("solde", "")
            client = Client.objects.get(code=request.POST.get("client", ""))
            client = client
            compte = Compte.objects.create(id=id, numero=numero, date_creation=date_creation, solde=solde,
                                           client=client)
            compte.save()

            # redirect to a new URL:
            return HttpResponseRedirect('comptes')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ComptesForm()

    return render(request, 'FormCompte.html', {'form': form})


def OperationF(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OperationsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            numOperation = request.POST.get("numOperation", "")
            type = request.POST.get("type", "")
            dateOperation = request.POST.get("dateOperation", "")
            montant = request.POST.get("montant", "")
            compte1 = Compte.objects.get(id=request.POST.get("compte", ""))
            compte = compte1
            client1 = Client.objects.get(code=request.POST.get("client_op", ""))
            client_op = client1
            operation = Operations.objects.create(numOperation=numOperation, type=type, dateOperation=dateOperation,
                                                  montant=montant, compte=compte,
                                                  client_op=client_op)
            operation.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OperationsForm()

    return render(request, 'OperationsForm.html', {'form': form})
