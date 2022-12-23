

from unittest import skip
from unittest.mock import patch

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


@skip(' msg do porque estou pulando o teste')
class RecipehomeViewsTest(RecipeTestBase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
# acima eu quero saber se a funcao carregada na view ao abrir o navegador
# é a mesma funcao que temos no views.home

    def test_recipe_home_url_is_correct(self):
        # assert 1 == 2
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')
    # TEARDOWN

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_show_no_recipes_found_is_no_recipe(self):
        # apago a receita criada la em cima somente para esse teste
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8'),)

        # tenho que escrever alguma coisa a mais sobre teste
        # self.fail('Para que eu termine de digita-lo')

    def test_recipe_home_template_dont_loads_recipes_not_published(self):
        """teste recipe is published false dont show"""
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8'),)

    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_home_is_paginated(self):
        import recipes
        for i in range(24):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)
    # esse teste testa a quantidade de paginas feitas pelo paginator dependendo
    # da quantidade de recipes, mas nao esta funcionando corretamente

        recipes.views.PER_PAGE = 3
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 8)
        self.assertEqual(len(paginator.get_page(1)), 3)
        self.assertEqual(len(paginator.get_page(2)), 3)
