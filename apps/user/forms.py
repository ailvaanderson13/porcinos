from django import forms
from .models import User
from apps.company.models import Company
from apps.permissoes.models import Perfil


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='NOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu primeiro nome:'
            }
        )
    )

    last_name = forms.CharField(
        label='SOBRENOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu sobrenome:'
            }
        )
    )

    telefone = forms.CharField(
        label='TELEFONE',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone:'
            }
        )
    )

    email = forms.CharField(
        label='EMAIL',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone:'
            }
        )
    )

    perfil = forms.ModelChoiceField(
        required=False,
        label="PERFIL",
        queryset=Perfil.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    cpf = forms.CharField(
        label='CPF',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o cpf:'
            }
        )
    )

    company = forms.ModelChoiceField(
        label="EMPRESA",
        queryset=Company.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        exclude = ['is_active', 'is_staff', 'date_joined']
        fields = [
            'first_name', 'last_name', 'telefone', 'email', 'is_active', 'perfil', 'cpf'
        ]


class UserOwnerForm(forms.ModelForm):
    first_name = forms.CharField(
        label='NOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu primeiro nome:'
            }
        )
    )

    last_name = forms.CharField(
        label='SOBRENOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu sobrenome:'
            }
        )
    )

    telefone = forms.CharField(
        label='TELEFONE',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone:'
            }
        )
    )

    email = forms.CharField(
        label='EMAIL',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone:',
            }
        )
    )

    perfil = forms.ModelChoiceField(
        required=False,
        label="PERFIL",
        queryset=Perfil.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    cpf = forms.CharField(
        label='CPF',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o cpf:'
            }
        )
    )

    class Meta:
        model = User
        exclude = ['is_active', 'is_staff', 'date_joined', 'company']
        fields = [
            'first_name', 'last_name', 'telefone', 'email', 'is_active', 'perfil', 'cpf'
        ]

        
class MyProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='NOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu primeiro nome:'
            }
        )
    )

    last_name = forms.CharField(
        label='SOBRENOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira seu sobrenome:'
            }
        )
    )

    telefone = forms.CharField(
        label='TELEFONE',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o telefone:'
            }
        )
    )

    email = forms.CharField(
        required=False,
        label='EMAIL',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o email:', 'disabled': 'true'
            }
        )
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'telefone', 'email']