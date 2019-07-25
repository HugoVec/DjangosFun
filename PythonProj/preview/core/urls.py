
from django.urls import path, include
from .views import list_clients, novo_cliente

# LINKS CADASTRADOS
urlpatterns = [
    path('', list_clients, name='lista'),
    path('new/', novo_cliente, name='new')
]
