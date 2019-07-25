from django.shortcuts import render, redirect
from .models import Client
from .form import ClienteModel

# Create your views here.


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def novo_cliente(request):
    form = ClienteModel(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'newC.html', {'form': form})

