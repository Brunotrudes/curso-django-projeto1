

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
    # url final que aponta para recipe - devo colocar id na request
    # o int demostra o tipo de url que sera aceita inteiro, string, slug -  url
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
