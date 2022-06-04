from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models, forms


def cadastro_update_cliente(request, pk=None):
    page_title = 'Cadastro de Cliente' if not pk else 'Editar Cliente'
    msg = None
    icon = None
    name = None
    notification = None
    cliente = None
    form = forms.FormCliente()
    company = request.user.company if request.user.company else None

    if pk:
        cliente = models.Cliente.objects.get(pk=pk)
        if cliente:
            form = forms.FormCliente(instance=cliente)
        else:
            msg = 'Nenhum cliente encontrado!'
            icon = 'alert-danger'

    if request.method == 'POST':
        if cliente:
            form = forms.FormCliente(request.POST, instance=cliente)
        else:
            form = forms.FormCliente(request.POST)

        try:
            if form.is_valid():
                if cliente:
                    form.save()
                    msg = 'Cliente editado(a) com Sucesso!'
                    icon = 'alert-success'
                else:
                    new_cliente = form.save(commit=False)
                    cpf = new_cliente.cpf
                    username = new_cliente.email
                    new_cliente.company = company
                    new_cliente.username = username
                    new_cliente.save()
                    msg = 'Cliente Cadastrado(a) com sucesso!'
                    icon = 'alert-success'
                form = forms.FormCliente()
        except Exception as e:
            if 'username' in str(e):
                msg = 'Este E-mail está indisponível, escolha outro'
                icon = 'alert-warning'
            
    notification = {'icon': icon, 'msg': msg}

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'form': form
    }

    return render(request, 'cadastro_cliente.html', context)


def list_cliente(request):
    page_title = 'Clientes Cadastrados(as)'
    msg = None
    icon = None
    notification = None
    clientes = None
    clientes = models.Cliente.objects.filter(is_active=True)

    if not clientes:
        msg = 'Nenhum cliente Cadastrado(a)'
        icon = 'alert-warning'

    notification = {
        'msg': msg, 'icon': icon
    }
    context = {
        'clientes': clientes, 'notification': notification, 'msg': msg, 'page_title': page_title
    }

    return render(request, 'clientes_cadastrados.html', context)


@csrf_exempt
def delete_cliente(request):
    response = {
        'success': False
    }
    print(request.method)
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk:
            cliente = models.Cliente.objects.get(pk=pk)
            cliente.is_active = False
            cliente.save()
            response['success'] = True
    return JsonResponse(response, safe=False)
