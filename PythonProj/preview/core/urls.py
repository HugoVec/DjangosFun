
from django.urls import path, include
from .views import list_clients

# LINKS CADASTRADOS
urlpatterns = [
    path('', list_clients),
]
