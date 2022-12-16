
# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe

# from utils.recipe.factory import make_recipe

# Create your views here.


# def home(request):
#     # devo ir em project depois em settings em INSTALLED APPS e colocar
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


def contato(request):
    recipe = Recipe.objects.filter(
        is_published=True,
        recipe_id=4
    )
    return render(request, 'recipes/pages/contato.html', context={
        # 'id':recipe,
    })


def sobre(request):
    return render(request, 'recipes/pages/sobre.html', context={

    })


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True,
    # ).order_by('-id')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category_id=category_id,
            is_published=True,
        ).order_by('-id'),
    )

    # category_name = getattr(
    #     getattr(recipes.first(), 'category', None),
    #     'name',
    #     'Not found'
    # )

    # if not recipes:
    #     # return HttpResponse(content='Not found', status=404)
    #     raise Http404('Not found :(')

    return render(request, 'recipes/pages/category.html', context={
        # 'name': 'Luiz Otávio',
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
        # 'title': f'{recipes.first().category_name} - Category |',
        'title': f'{recipes[0].category.name} - Category |',
    })


def recipe(request, id):
    # recipe = Recipe.objects.filter(
    #     # id=id,
    #     pk=id,
    #     is_published=True,
    # ).order_by('-id').first()

    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        # 'name': 'Luiz Otávio',
        # 'recipe': make_recipe(),
        'recipe': recipe,

        'is_detail_page': True,
    })
