from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from . import forms, models
from apps.utils.function_aux.random import str_generator


def create_update_store(request, pk=None):
    page_title = 'CADASTRO DE LOJA' if not pk else "EDITAR LOJA"
    form = forms.StoreForm()
    store = None
    icon = None
    msg = None
    notification = None
    id_store = None

    if pk:
        store = models.Store.objects.filter(pk=pk).last()
        if store:
            form = forms.StoreForm(instance=store)

    if request.method == 'POST':
        if store:
            form = forms.StoreForm(request.POST, instance=store)
        else:
            form = forms.StoreForm(request.POST)

        if form.is_valid():
            if not store:
                form = form.save(commit=False)
                while True:
                    id_store = f"{str_generator()}"
                    id_equals = models.Store.objects.filter(id_store=id_store).last()
                    if not id_equals:
                        break
                icon = 'alert-success'
                msg = 'Loja cadastrada com sucesso!'
            else:
                icon = 'alert-success'
                msg = 'Informações editadas com sucesso!'

            form.id_store = id_store    
            form.save()
            form = forms.StoreForm()
        else:
            icon = 'alert-danger'
            msg = 'Ocorreu um erro, tente novamente!'

    notification={'icon': icon, 'msg': msg}
    context={
        'form': form, 'page_title': page_title, 'notification': notification, 'msg': msg
    }
    return render(request, 'create_update_store.html', context)

def panel_store(request):
    page_title = "Lojas cadastradas"
    icon = '<i class="fas fa-store"></i>'

    store = models.Store.objects.filter(is_active=True).order_by('nome')
    paginacao = Paginator(store, 8)
    page = request.GET.get('page')
    listagem = paginacao.get_page(page)

    num = 0
    for qtd in listagem:
        num += 1

    context={
        'store':listagem, 'page_title': page_title, 'icon': icon, 'num':num
    }

    return render(request, "lojas_cadastradas.html", context)

@csrf_exempt
def delete_store(request):
    response = {
        'success' : False
    }
    pk = None
    pk = request.POST.get('pk', pk)

    if pk:
        store = models.Store.objects.get(pk=pk)
        store.is_active = False
        store.save()
        response['success'] = True

    return JsonResponse(response, safe=False)
