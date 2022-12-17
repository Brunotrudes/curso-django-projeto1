

from django.urls import path

from recipes import views

# from recipes.views import home

# from . import views -isso significa que o . é da pasta em que eu estou
#  import views


# importa o modulo inteiro das urls

# http request


# def _home(request):
#   return HttpResponse('HOME')
# http response

# para criar urls é necessário criar views se nao dara erro

# cria-se app name para poder colocar nas urls
# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    # url vazia para apontar para home
    path('', views.home, name="home"),
    path('recipes/search/', views.search,  name="search"),

    # url final que aponta para recipe - devo colocar id na request
    # o int demostra o tipo de url que sera aceita inteiro, string, slug -  url
    path('recipes/category/<int:category_id>/',
         # int:category_id
         views.category, name="category"),

    path('recipes/<int:id>/', views.recipe, name="recipe"),

    path('contato/', views.contato,  name="contato"),
    path('sobre/', views.sobre,  name="sobre"),
    path('clientes/', views.cliente,  name="cliente"),
    path('cadastro/', views.cadastro,  name="cadastro"),

]

# name serve para chamar a view em determinadas partes do project pelo seu nome
