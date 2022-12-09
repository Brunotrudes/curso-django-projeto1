from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # devo ir em projeto depois em settings em INSTALLED APPS e colocar
    # uma string com o nome do app criado
    # temos que criar uma pasta chamada de templates dentro da pasta do app
    # tem que criar o arquivo hmtl na pasta template que o django vai buscar
    # o arquivo automaticamente
    # global/home ou recipes/home
    return render(request, 'recipes/home.html', status=201)


def contato(request):
    return render(request,  'temp.html')


def sobre(request):
    return HttpResponse('SOBRE')
