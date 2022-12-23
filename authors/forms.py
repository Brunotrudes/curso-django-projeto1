import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from django.forms import widgets

# aqui importamos o formulario do django para usuarios


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    # field.widget.attrs['placeholder'] = placeholder_val
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    # expressao regular conferindo se os campos tem?
    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='Invalid'
        )


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['placeholder'] = 'Que Legal'
        # self.fields['Email'].widget.attrs['placeholder'] = 'Que Legal'
        add_placeholder(self.fields['username'], 'seu nome de usuário')
        add_placeholder(self.fields['email'], 'seu nome email')
        add_placeholder(self.fields['first_name'], 'Ex. Bruno')
        # add_placeholder(self.fields['last_name'], 'Ex. Trudes')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[strong_password]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'username',
            'password',
        ]
        # fields = '__all__'
        # passando o __all__ buscamos todos os campos do model User do django.
        # depois coloco o formulario na view

        # exclude = ['first_name']
        labels = {
            'username': 'Digite seu usuario',
            'first_name': 'Nome',
            'email': 'Email',
            'password': 'Senha',
        }
        error_messages = {
            'username': {
                'required': 'Esse campo é obrigatório',
                'max_length': 'Quantidade de caracteres',
                'invalid': 'Email nao é válido',

            }
        }
        widgets = {
            'username': forms.TextInput(attrs={

                'placeholder': 'Digite seu nome de usuário',
                'class': 'text-input',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha'
            })
        }


# validacao de formularios
# clean_nome_do_campo é especifico do campo
# clean usado para validar o formulario com um todo. normalmente
# chamado depois do metodo com nome do campo

#     def clean_password(self):
#         data = self.cleaned_data.get('password')
# # se houver a palavra atencao no campo password escreva nao digite no erro
#         if 'atenção' in data:
#             raise ValidationError(
#                 'Não digite %(value)s no campo password',
#                 code='invalid',
#                 params={'value': '"atenção"'}
#             )

#         return data

#     def clean_first_name(self):
#         data = self.cleaned_data.get('first_name')
# # se houver a palavra atencao no campo password escreva nao digite no erro
#         if 'Bruno' in data:
#             raise ValidationError(
#                 'Não digite %(value)s no campo password',
#                 code='invalid',
#                 params={'value': '"Bruno"'}
#             )

#         return data

# validacao de dois campos senhas
# clean validacao do formulario com um todo
# outra maneira de validar
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password2 = cleaned_data.get('password2')

    #     password_confirmation_error = ValidationError(
    #         'Password and password2 must be qual',
    #         code='invalid'
    #     )

    #     if password != password2:
    #         raise ValidationError({
    #             'password': 'Password and Password2 must be equal ',
    #             # 'password2': 'Password and Password2 must be equal ',
    #             'password2': [
    #                 password_confirmation_error,
    #                 'Another error'
    #             ]
    #         })

# outra forma de fazer a validacao de campos
# essas sao opcoes que podemos usar, a melhor depende da situacao
