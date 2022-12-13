
from django.shortcuts import render

from recipes.models import Recipe
from utils.recipe.factory import make_recipe

# Create your views here.


# def home(request):
#     # devo ir em projeto depois em settings em INSTALLED APPS e colocar
#     # uma string com o nome do app criado
#     # temos que criar uma pasta chamada de templates dentro da pasta do app
#     # tem que criar o arquivo hmtl na pasta template que o django vai buscar
#     # o arquivo automaticamente
#     # global/home ou recipes/home
#     return render(request, 'recipes/pages/home.html', status=201)

# toda view precisa receber um request e retornar algo
# request como argumento da funcao

# retona o metodo render() sempre com primeiro parametro o request
# segundo parametro o template - endereco do template

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # 'name': 'Luiz Otávio',
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        # 'name': 'Luiz Otávio',
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category |',
    })


def recipe(request, id):

    return render(request, 'recipes/pages/recipe-view.html', context={
        # 'name': 'Luiz Otávio',
        'recipe': make_recipe(),

        'is_detail_page': True,
    })
