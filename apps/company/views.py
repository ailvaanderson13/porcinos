from django.shortcuts import redirect, render
from . import forms, models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_update_company(request, pk=None):
    if not request.user.is_superuser:
        return redirect('utils:dashboard')

    page_title = 'CADASTRO DE EMPRESA' if not pk else "EDITAR EMPRESA"
    form = forms.EmpresaForms()
    icon = None
    msg = None
    empresa = None
    notification = None

    if pk:
        empresa = models.Company.objects.filter(is_active=True, pk=pk).last()
        if empresa:
            form = forms.EmpresaForms(instance=empresa)
        else:
            icon = 'alert-warning'
            msg = 'Nenhuma empresa encontrada!'

    if request.method == 'POST':
        if empresa:
            form = forms.EmpresaForms(request.POST, instance=empresa)
        else:
            form = forms.EmpresaForms(request.POST)

    if form.is_valid():
        if pk:
            icon = 'alert-success'
            msg = 'Empresa editada com sucesso!'
        else:
            icon = 'alert-success'
            msg = 'Empresa cadastrada com sucesso!'  

        form.save()
    else:
        icon = 'alert-danger'
        msg = form.errors

    if not pk:
        form = forms.EmpresaForms()

    notification = {'icon': icon, 'msg': msg}

    context={
        'page_title': page_title, 'form': form, 'notification': notification, 'msg': msg
    }
    return render(request, 'create_update_company.html', context)


def list_company(request):
    page_title = "EMPRESAS CADASTRADAS"

    if request.user.is_superuser:
        companys = models.Company.objects.filter(is_active=True)
    else:
        companys = models.Company.objects.filter(is_active=True, compnay=request.user.company)

    context = {
        'companys': companys, 'page_title': page_title,
    }

    return render(request, 'list_company.html', context)


@csrf_exempt
def delete_company(request):
    response = {
        'success': False
    }

    pk = request.POST.get('pk', None)

    if pk:
        user = models.Company.objects.get(pk=pk)
        if user:
            user.is_active = False
            user.save()
            response['success'] = True

    return JsonResponse(response, safe=False)