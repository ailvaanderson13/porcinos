from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import forms, models


def new_category(request, pk=None):
    page_title = "Cadastro de Categoria" if not pk else "Editar Categoria"
    form = forms.CategoriaForm()
    msg = None
    notification = None
    icon=None
    categoria = None
    company = request.user.company

    if pk:
        categoria = models.Category.objects.get(pk=pk)

        if categoria:
            form = forms.CategoriaForm(instance=categoria)

    if request.method == 'POST':
        if categoria:
            form = forms.CategoriaForm(request.POST, instance=categoria)
        else:
            form = forms.CategoriaForm(request.POST)

        try:
            if form.is_valid():
                if categoria:
                    form.save()
                else:
                    new_categoria = form.save(commit=False)
                    new_categoria.company = company
                    new_categoria.save()
                msg = 'Categoria cadastrada com sucesso!'
                icon = 'alert-success'
            else:
                msg = 'Categoria cadastrada com sucesso!'
                icon = 'alert-success'
        except Exception as e:
            msg = e
            icon = 'alert-danger'

        if not categoria:
            form = forms.CategoriaForm()
    notification = {
        'icon': icon, 'msg': msg 
    }
    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'form': form
    }
    return render(request, 'cadastro_categoria.html', context)


def list_categoria(request):
    page_title = 'Categorias Cadastradas'
    categorias = None
    msg = None
    icon=None
    notification = None
    company = request.user.company if request.user.company else None

    if company:
        categorias = models.Category.objects.filter(is_active=True, company=company)
    else:
        categorias = models.Category.objects.filter(is_active=True)

    if not categorias:
        msg = 'Nenhuma categoria cadastrada'
        icon = 'alert-warning'

    notification = {'msg': msg, 'icon': icon}

    context = {
        'page_title': page_title, 'categorias': categorias, 'msg': msg, 'notification': notification
    }

    return render(request, 'categorias_cadastradas.html', context)


@csrf_exempt
def delete_categoria(request):
    response = {
        'success': False
    }
    print(request.method)
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk:
            categoria = models.Category.objects.get(pk=pk)
            categoria.is_active = False
            categoria.save()
            response['success'] = True
    return JsonResponse(response, safe=False)