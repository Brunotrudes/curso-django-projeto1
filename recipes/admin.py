from django.contrib import admin

from .models import Category, Cliente, Recipe

# Register your models here.

# @admin.register


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)  # uma mandeira de importar
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)  # outra maneira de importar


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ['nome', 'cpf', 'dtNascimento', 'sexo',
                    'estado_civil', 'nrTelCelular', 'nrTelFixo']
    list_filter = ['sexo', 'estado_civil']
    search_fields = ['nome']


admin.site.register(Cliente, ClienteAdmin)
