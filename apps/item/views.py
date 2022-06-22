from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.categoria.models import Category

from . import models, forms


def create_update_item(request, pk=None):
    page_title = 'Cadastro de produto' if not pk else 'Editar Produto'
    msg = None
    notification = None
    icon = None
    form = forms.ItemForm()
    item = None
    company = request.user.company if request.user.company else None

    if pk:
        item = models.Item.objects.get(pk=pk, is_active=True)
        if item:
            form = forms.ItemForm(instance=item)
        else:
            msg = 'Nenhum Produto Encontrado'
            notification = 'alert-danger'

    if request.method == 'POST':
        if item:
            form = forms.ItemForm(request.POST, instance=item)
        else:
            form = forms.ItemForm(request.POST)

        if form.is_valid():
            if item:
                form.save()
                msg = 'Produto Atualizado com Sucesso!'
                icon = 'alert-success'
            else:
                new_item = form.save(commit=False)
                new_item.company = company
                new_item.save()
                msg = 'Produto Cadastrado com Sucesso!'
                icon = 'alert-success'
            form = forms.ItemForm()
        else:
            msg = form.errors
            icon = 'alert-danger'

    notification = {'msg': msg, 'icon': icon}

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'form': form
    }

    return render(request, 'cadastro_item.html', context)

def menos_itens(request):
    page_title = 'Produtos com menos de 10 unidades em estoque'

    itens = models.Item.objects.filter(is_active=True, quantidade__range=[0,10])

    resposicao = True

    context = {
        'page_title': page_title, 'itens': itens, 'resposicao': resposicao
    }

    return render(request, 'itens_cadastrados.html', context)


def list_item(request):
    page_title = 'Produtos Cadastrados'
    msg = None
    notification = None
    itens = None
    icon = None
    company = request.user.company if request.user.company else None
    category = Category.objects.all()
    select_category = request.POST.get('select_category', None)

    if company:
        if select_category:
            itens = models.Item.objects.filter(is_active=True, company=company, categoria__pk=int(select_category)).order_by('nome')
        else:
            itens = models.Item.objects.filter(is_active=True, company=company).order_by('nome')

    else:
        if select_category:
            itens = models.Item.objects.filter(is_active=True, categoria__pk=int(select_category)).order_by('nome')
        else:
            itens = models.Item.objects.filter(is_active=True).order_by('nome')

    if not itens:
        msg = "Nenhum Produto Cadastrado"
        icon = 'alert-warning'
    
    notification = {'msg': msg, 'icon': icon}

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'itens': itens, 'category': category
    }

    return render(request, 'itens_cadastrados.html', context)


@csrf_exempt
def delete_item(request):
    response = {
        'success': False
    }
    print(request.method)
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk:
            item = models.Item.objects.get(pk=pk)
            item.is_active = False
            item.save()
            response['success'] = True
    return JsonResponse(response, safe=False)