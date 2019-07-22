from django.http import HttpResponse
import random
from django.shortcuts import render


def randNum():
    return random.randint(1, 10)


def randPages(request):
    rand = randNum()
    pessoas = ['Gabriel','Carvalho','Lyon','Renato','Montovani','Nathan','Yan','Lucas','Tarcisio','Marcelo','Renan Faj'
        ,'Victor','Rickson','Gustavo','Shadow','Nevaska']
    return render(request, 'home.html', {'rand': rand, 'pessoas': pessoas})


def home_site(request):
    return HttpResponse('Ola!')
