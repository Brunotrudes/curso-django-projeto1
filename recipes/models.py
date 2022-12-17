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
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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


class Cliente(models.Model):
    # nome, sobrenome, cpf, email, fone, endereço, contratos.

    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField()
    dtNascimento = models.DateField(
        blank=True, null=True, verbose_name='Data de nascimento')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(
        max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    nrTelCelular = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    nrTelFixo = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')

    def __str__(self):
        return self.nome


#     cliente admin.py

#     class ClienteAdmin(admin.ModelAdmin):
#     model = Cliente
#     list_display = ['nome','cpf', 'dtNascimento', 'sexo',
#                     'estado_civil', 'nrTelCelular', 'nrTelFixo']
#     list_filter = ['sexo', 'estado_civil']
#     search_fields = ['nome']
# admin.site.register(Cliente, ClienteAdmin)
