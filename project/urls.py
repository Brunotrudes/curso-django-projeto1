"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# http request


# def _home(request):
#   return HttpResponse('HOME')
# http response


urlpatterns = [
    path('admin/', admin.site.urls),
    # o project inclui as urls do app recipes para ver urls de categorias,
    #  tem que abrir a pasta do app recipes
    path('', include('recipes.urls')),
    path('authors/', include('authors.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# para poder visualizar arquivos de imagem '
# e necessario instalar o pillow e fazer a concatenacao desses caminhos acima.


# ativar o shell
# python manage.py shell

# no shell efetuar comandos para poder acionar as tabelas do admin
#  para visualizacao no front end

# comando from recipes.models import Recipe, Category
# categories = Category.objects.all()
# categories

# ele retorna uma query com todas as categorias da base de dados

# categories.order_by('-id')
