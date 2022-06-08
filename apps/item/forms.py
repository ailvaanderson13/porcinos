from django import forms
from .models import Item
from apps.categoria.models import Category
from apps.company.models import Company


class ItemForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        label='CATEGORIA',
        queryset=Category.objects.filter(is_active=True),
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
                'class': 'form-control', 'placeholder': 'Insira um nome: '
            }
        )
    )

    
    quantidade = forms.CharField(
        label="QTD.",
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira a quantidade:'
            }
        )
    )


    valor_custo = forms.FloatField(
        label="VALOR DE CUSTO",
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o valor de custo'
            }
        )
    )

    valor_venda = forms.FloatField(
        label="VALOR DE VENDA",
        widget= forms.NumberInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o valor de venda'
            }
        )
    )

    code_bar = forms.CharField(
        label="CÓDIGO DE BARRAS",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira o Código de barras (DEVE CONTER NO MÍNIMO 5 DIGITOS!)'
            }
        )
    )
    
    descricao = forms.CharField(
        required=False,
        label='DESCRIÇÃO',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'placeholder': 'Insira uma descrição: '
            }
        )
    )

    class Meta:
        model = Item
        fields = ['categoria', 'nome', 'quantidade', 'valor_custo', 'valor_venda', 'code_bar', 'descricao']
        exclude = ['is_active', 'company', 'empty']
