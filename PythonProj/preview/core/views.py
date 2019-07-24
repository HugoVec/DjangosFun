from django.shortcuts import render
from .models import Client

# Create your views here.


def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})
