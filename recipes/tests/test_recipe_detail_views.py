

from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase

# Create your tests here.

# para criar um teste primeiro devemos criar uma classe que contera todos
#  os nossos testes

# ser super descritivos no testes para saber o que deu erro quanto for testar


@skip(' msg do porque estou pulando o teste')
class RecipeDetailTest(RecipeTestBase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
# acima eu quero saber se a funcao carregada na view ao abrir o navegador
# é a mesma funcao que temos no views.home

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)


class RecipeURLsTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    # def test_the_pytest_is_ok(self):
    #     assert 1 == 1, 'Um é igual a um'
    # SETUP

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_detail_template_loads_the_correct_recipes(self):
        needed_title = 'This is a detail page - it load one recipe'

        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:recipe', kwargs={
            'id': 1
        }))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_loads_recipe_not_published(self):
        """teste recipe is published false dont show"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': recipe.id
                }))

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_titel_and_escapad(self):
        url = reverse('recipes:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Pesquisa por &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )
