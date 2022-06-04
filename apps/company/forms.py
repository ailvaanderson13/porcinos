from django import forms
from . import models


class EmpresaForms(forms.ModelForm):
    razao_social = forms.CharField(
        label="RAZÃO SOCIAL",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira a Razão Social'
            }
        )
    )

    nome_fantasia = forms.CharField(
        label="NOME FANTASIA",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o Nome Fantasia'
            }
        )
    )

    cnpj = forms.CharField(
        label="CNPJ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o CNPJ'
            }
        )
    )

    rua = forms.CharField(
        label="RUA",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira a Rua'
            }
        )
    )

    numero_endereco = forms.CharField(
        label="Nº",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    cep = forms.CharField(
        label="CEP",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


    email = forms.CharField(
        label="E-MAIL",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o E-mail'
            }
        )
    )

    telefone = forms.CharField(
        label="TELEFONE",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Telefone para contato'
            }
        )
    )

    class Meta:
        model = models.Company
        fields = ('__all__')
        exclude = ['is_active']