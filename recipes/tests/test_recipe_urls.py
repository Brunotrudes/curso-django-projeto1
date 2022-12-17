
from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeURLsTest(RecipeTestBase):
    def setUp(self) -> None:

        return super().setUp()
    # teremos um setaup e um teardown para cada teste
    #

    def tearDown(self) -> None:
        return super().tearDown()

    # def test_the_pytest_is_ok(self):
    #     assert 1 == 1, 'Um é igual a um'
    # SETUP

    def test_recipe_home_url_is_correct(self):
        # assert 1 == 2
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')
    # TEARDOWN

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
