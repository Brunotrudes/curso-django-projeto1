from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm

# Create your views here.


def register_view(request):
    # request.session['number'] = request.session.get('number') or 1
    # request.session['number'] += 1
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,

    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    # return render(request, 'authors/pages/register_view.html', {
    # #     'form': form,
    # })

    if form.is_valid():
        # data = form.save(commit=False) #guarda os valores mas nao salva
        #  na base de dados
        #    data.outro_campo = 'outro_valor'
        form.save()
        messages.success(
            request, 'Seu usuário foi criado, por favor faça o login')

        del (request.session['register_form_data'])
    return redirect('authors:register')
