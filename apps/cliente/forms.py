from django import forms
from .models import Cliente


class FormCliente(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o nome:'
            }
        )
    )

    last_name = forms.CharField(
        label="Sobrenome",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o sobrenome: '
            }
        )
    )

    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o CPF:'
            }
        )
    )

    telefone = forms.CharField(
        label="Telefone",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone com DDD:'
            }
        )
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o e-mail'
            }
        )
    )
    class Meta:
        model = Cliente
        fields = [
            'first_name', 'last_name', 'cpf', 'telefone', 'email'
        ]
