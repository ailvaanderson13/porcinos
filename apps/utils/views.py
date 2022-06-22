from socket import create_server
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from apps.store.models import Store
from apps.pedido.models import Pedido
from django.views.decorators.csrf import csrf_exempt
from apps.item.models import Item
from django.db.models import Q
from time import sleep
import pandas as pd
from datetime import datetime


def dashboard_admin(request, id_store=None):
    page_title = 'DASHBOARD'

    if not request.user.is_authenticated:
        return redirect('utils:login')

    if id_store:
        store = Store.objects.filter(id_store=id_store).last()
        if store:
            if request.user.company == store.company:
                pass
    else:
        if not request.user.is_superuser:
            pass
        

    context = {
        'page_title': page_title
    }
    return render(request, 'dashboard/dashboard_admin.html', context)


def acesso(request):
    if request.user.is_authenticated:
        return redirect('utils:dashboard_admin')

    erro = False
    msg = None

    if request.method == 'POST':
        email = request.POST.get('email', None)
        senha = request.POST.get('password', None)
        user = authenticate(username=email, password=senha)

        if user:
            login(request, user)
            return redirect('utils:dashboard_admin')
        else:
            erro = True
            msg = 'Usuário ou senha inválidos!'

    context = {
        'erro': erro, 'msg': msg
    }
    return render(request, 'login/login.html', context)


def logout_(request):
    return logout_then_login(request, login_url='/login')


@csrf_exempt
def load_dashboard(request):
    today = datetime.today()
    user = request.user 
    response={}
    id = request.GET.get('id_card', None)
    sleep(1)

    if id:
        if id in ['1', 1]:
            pedidos = Pedido.objects.filter(is_active=True)
            df = pd.DataFrame(pedidos)
            response['info'] = 'Nenhum'
            
        elif id in ['2', 2]:

            itens = Item.objects.filter(is_active=True, quantidade__range=[0,10]).count()
            response['info'] = itens

        elif id in ['3', 3]:
            itens = Item.objects.filter(is_active=True).count()
            response['info'] = itens

        elif id in ['4', 4]:
            pedidos = Pedido.objects.filter(data__date=today.date(), is_active=True, dinheiro=True).count()
            response['info'] = pedidos

        elif id in ['5', 5]:
            pedidos = Pedido.objects.filter(Q(data__date=today.date(), is_active=True, credito=True) | Q(data__date=today.date(), is_active=True, debito=True)).count()
            response['info'] = pedidos
        elif id in ['6', 6]:
            pedidos = Pedido.objects.filter(data__date=today.date(), is_active=True, pix=True).count()
            response['info'] = pedidos
        elif id in ['7', 7]:
            pedidos = Pedido.objects.filter(data=today).count()
            response['info'] = pedidos
        elif id in ['8', 8]:
            pedidos = Pedido.objects.filter(data=today).count()
            response['info'] = pedidos
        elif id in ['9', 9]:
            pedidos = Pedido.objects.filter(data__date=today.date()).count()
            response['info'] = pedidos
    else:
        pass
    return JsonResponse(response, safe=False)


def checkout(request):
    return render(request, 'checkout/checkout.html')