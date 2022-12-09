

from django.urls import path

from recipes.views import contato, home, sobre

# http request


# def _home(request):
#   return HttpResponse('HOME')
# http response


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
