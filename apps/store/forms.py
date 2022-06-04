from django import forms
from apps.company.models import Company
from . import models


class StoreForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        label="EMPRESA",
        queryset=Company.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    nome = forms.CharField(
        label='NOME',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o Nome da Unidade'
            }
        )
    )

    endereco = forms.CharField(
        label='ENDEREÇO',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o Endereço da Unidade'
            }
        )
    )
    
    class Meta:
        model = models.Store
        fields = ('__all__')
        exclude = ['is_active', 'id_store']

