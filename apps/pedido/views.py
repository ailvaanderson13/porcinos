from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import forms, models
from apps.cliente.models import Cliente
from apps.item.models import Item
from apps.utils.function_aux.random import str_generator
import json


@csrf_exempt
def safe_pedido(request):
    response = {
        'success': False
    }
    list_pedido = None
    pk_cliente = None
    forma_pag = None
    obs = None
    funcionario = request.user
    loja = request.user.loja

    if request.method == 'POST':
        list_pedido = json.loads(request.POST['list_pedido'])
        pk_cliente = request.POST.get('id_cliente', None)
        forma_pag = request.POST.get('forma_pag', None)
        obs = request.POST.get('obs', None)

    if list_pedido and pk_cliente:
        pk_cliente = int(pk_cliente)
        cod = str_generator().upper()
        equals = models.Pedido.objects.filter(codigo=cod)
        while equals:
            cod = str_generator().upper()
        cod = f"#{cod}"

        new_pedido = models.Pedido.objects.create(codigo=cod, employee=funcionario, cliente_id=pk_cliente, loja=loja,
                                                  forma_pag=forma_pag, obs=obs, detalhes=list_pedido)

        for l in list_pedido:
            if type(l) == dict:
                for k, v in l.items():
                    for i in v:
                        for x in i['id-produto']:
                            new_pedido.item.add(int(x))

        new_pedido.save()

        response['success'] = True

    return JsonResponse(response, safe=False)


def create_update_pedido(request, pk=None):
    page_title = 'Novo Pedido' if not pk else 'Editar Pedido'
    notification = None
    msg = None
    line = ''
    col0 = ''
    col1 = ''
    col2 = ''
    col3 = ''
    col4 = ''
    obs = ''
    pag = None
    clientes = None
    produto = None

    produtos = Item.objects.filter(is_active=True).order_by('nome')
    clientes = Cliente.objects.filter(is_active=True)

    if pk:
        pedido = models.Pedido.objects.get(pk=pk)
        if pedido:
            pag = pedido.forma_pag
            obs = pedido.obs
            detalhes = eval(pedido.detalhes)

            for i in detalhes:
                if type(i) == dict:
                    for k, v in i.items():
                        if type(v) == list:
                            for ii in v:
                                if type(ii) == dict:
                                    for kk, vv in ii.items():
                                        if kk == 'id-produto':
                                            produto = models.Item.objects.get(pk=vv)
                                            col0 = f"""
                                                <td>
                                                    <div class="button-group">
                                                        <button class='btn btn-danger btn-apagar list-cart btn-sm shadow
                                                         list-cart' value='{produto.pk}'>
                                                            <i class='fas fa-trash'></i>
                                                        </button>
                                                    </div>
                                                </td>
                                            """
                                            col1 = f"<td>{produto.nome}</td>"
                                        if kk == 'qtd':
                                            col2 = f"<td><input type='tel' class='form-control qtd-item calc " \
                                                   f"id-{produto.pk}' style='width:60px; height:30px' min='1' " \
                                                   f"value='{vv}'></td>"
                                        if kk == 'valor_uni':
                                            col3 = f"<td><input type='tel' class='form-control price calc' " \
                                                   f"id='id-{produto.pk}' style='width:100px; height:30px' min='1' " \
                                                   f"value={vv}></td>"
                                            col4 = f"<td><span class='form-control total-item mult-total-{produto.pk}' " \
                                                   f"style='width:100px; height:30px'></span></td>"

                                    line += f"<tr class='line' id_line={produto.pk}>{col0}{col1}{col2}{col3}{col4}</tr>"

            if pag == '0':
                pag = 'Nenhum'
            elif pag == '1':
                pag = 'Dinheiro'
            elif pag == '2':
                pag = 'Débito'
            elif pag == '3':
                pag = 'Crédito'

            if obs in [None, '', ' ', 'null']:
                obs = 'Nenhuma Observação'

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'clientes': clientes, 'produtos': produtos,
        'pk': pk, 'pag': pag, 'line': line, 'obs': obs
    }

    return render(request, 'cadastro_pedido.html', context)


def list_pedidos(request):
    page_title = 'Pedidos Cadastrados'
    msg = None
    notification = None

    pedidos = models.Pedido.objects.filter(is_active=True)

    if not pedidos:
        msg = 'Nenhum Pedido Cadastrado!'
        notification = 'danger'

    context = {
        'page_title': page_title, 'pedidos': pedidos, 'msg': msg, 'notification': notification
    }
    return render(request, 'pedidos_cadastrados.html', context)


@csrf_exempt
def detail_pedido(request):
    response = {
        'success': False
    }
    pag = None
    obs = None
    line = ''
    col1 = ''
    col2 = ''
    col3 = ''
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk:
            pedido = models.Pedido.objects.filter(pk=pk)

            if pedido:
                pedido = pedido.last()
                pag = pedido.forma_pag
                obs = pedido.obs
                detalhes = eval(pedido.detalhes)

                for i in detalhes:
                    if type(i) == dict:
                        for k, v in i.items():
                            if type(v) == list:
                                for ii in v:
                                    if type(ii) == dict:
                                        for kk, vv in ii.items():
                                            if kk == 'id-produto':
                                                produto = models.Item.objects.get(pk=vv)
                                                col1 = f"<td>{produto.nome}</td>"
                                            if kk == 'valor_uni':
                                                col2 = f"<td>{vv}</td>"
                                            if kk == 'qtd':
                                                col3 = f"<td>{vv}</td>"
                                        line += f"<tr>{col1}{col2}{col3}</tr>"
            if pag == '0':
                pag = 'Nenhum'
            elif pag == '1':
                pag = 'Dinheiro'
            elif pag == '2':
                pag = 'Débito'
            elif pag == '3':
                pag = 'Crédito'

            if obs in [None, '', ' ', 'null']:
                obs = 'Nenhuma Observação'

            pedido = models.Pedido.objects.filter(pk=pk).values('codigo', 'employee__first_name',
                                                                'cliente__nome')
            response['obs'] = obs
            response['line'] = line
            response['pedido'] = list(pedido)
            response['pag'] = str(pag)
            response['success'] = True

    return JsonResponse(response, safe=False)


@csrf_exempt
def get_product(request):
    response = {
        'success' : False
    }

    code = request.POST.get('code', None)
    qtd = request.POST.get('qtd', None)

    qtd_line = 0

    if not qtd:
        qtd = 1
    if code:
        item = Item.objects.filter(code_bar=code, is_active=True).last()
        if item:
            line = f"""
                <tr>
                    <td class="qtd_line">{qtd_line}</td>
                    <td>{item.nome}</td>
                    <td class="qtd_item">{int(qtd)}</td>
                    <td class="val_uni">{int(item.valor_venda)}</td>
                    <td class="val_total">{int(qtd)*item.valor_venda}</td>
                    <td>
                        <div class="button-group">
                            <button type="button" class="btn btn-white btn_trash"><i class="fas fa-trash text-danger"></i></button>
                        </div>
                    </td>
                </tr>
            """
            response['item'] = str(line)
            response['success'] = True

    return JsonResponse(response, safe=False)
