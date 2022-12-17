

from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    # def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
    #     # validacao de campos, quando digitado a quantidade maior que a
    #     # permitida pelo max-length .full_clean()
    #     self.recipe.title = 'a' * 66

    #     with self.assertRaises(ValidationError):
    #         self.recipe.full_clean()  # Aqui a validacao ocorre

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Test Default category'),
            author=self.make_author(username='nesuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe preparation steps',
            # preparation_steps_is_html=False,
            # is_published=True,
            cover='recipes/covers/2022/12/15/'
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        # fields = [
        #     ('title', 65),
        #     ('description', 165),
        #     ('preparation_time_unit', 65),
        #     ('servings_unit', 65),
        # ]

        # for field, max_length in fields:
        #     with self.subTest(field=field, max_length=max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparatios_steps_is_html is not false'
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is published is not false'
        )

    def test_recipe_string_rerpresentation(self):
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), 'Testing Representation')
