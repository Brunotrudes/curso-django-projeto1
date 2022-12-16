from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

# Create your tests here.

# para criar um teste primeiro devemos criar uma classe que contera todos
#  os nossos testes

# ser super descritivos no testes para saber o que deu erro quanto for testar


class RecipeURLsTest(TestCase):
    # def test_the_pytest_is_ok(self):
    #     assert 1 == 1, 'Um é igual a um'
    def test_recipe_home_url_is_correct(self):
        # assert 1 == 2
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
