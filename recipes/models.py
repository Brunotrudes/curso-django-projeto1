from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# criar os modulos do banco dew dados aqui
# basicamente iremos criar uma classe

# vamos pensar na classe em si sendo a tabela do banco de dados


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    # coloco a juncao entre as tabelas com forei Key, on_delete é quanto
    #  deletar, seta nulo o campo, e True para que o campo possa ser nulo

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
# python manage.py migrate
# python manage.py makemrigrations
# python manage.py migrate

# criar usuarios para acessar o admin do django
# python manage.py createsuperuser
# cria o super usuario, o usuario que podera fazer tudo
