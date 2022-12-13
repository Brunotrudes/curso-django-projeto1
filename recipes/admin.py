from django.contrib import admin

from .models import Category, Recipe

# Register your models here.

# @admin.register


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)  # uma mandeira de importar
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)  # outra maneira de importar
