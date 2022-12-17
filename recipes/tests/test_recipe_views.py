

from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase

# Create your tests here.

# para criar um teste primeiro devemos criar uma classe que contera todos
#  os nossos testes

# ser super descritivos no testes para saber o que deu erro quanto for testar


@skip(' msg do porque estou pulando o teste')
class RecipeViewsTest(RecipeTestBase):
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


class RecipeURLsTest(RecipeTestBase):

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

    def test_recipe_category_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn('Recipe Title', content)

    def test_category_view_returns_status_code_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_status_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_show_no_recipes_found_is_no_recipe(self):
        # apago a receita criada la em cima somente para esse teste
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8'),)

        # tenho que escrever alguma coisa a mais sobre teste
        # self.fail('Para que eu termine de digita-lo')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_category_template_dont_loads_recipes_not_published(self):
        """teste recipe is published false dont show"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id}))
        self.assertEqual(response.status_code, 404)

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

    def test_recipe_home_template_dont_loads_recipes_not_published(self):
        """teste recipe is published false dont show"""
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8'),)

    def test_recipe_detail_template_dont_loads_recipe_not_published(self):
        """teste recipe is published false dont show"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': recipe.id
                }))
