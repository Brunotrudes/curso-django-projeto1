

from django.urls import path

from recipes.views import home

# http request


# def _home(request):
#   return HttpResponse('HOME')
# http response


urlpatterns = [
    path('', home),
]
