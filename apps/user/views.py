from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from . import forms, models


def create_update_user(request, pk=None):
    page_title = "NOVO USUÁRIO" if not pk else "EDITAR USUÁRIO"
    form = forms.UserOwnerForm() if request.user.owner else forms.UserForm()
    msg = None
    icon = None
    notification = None
    user = None
    company = request.user.company if request.user.company else None

    if pk:
        user = models.User.objects.filter(pk=pk, company=company).last()
        if user:
            form = forms.UserOwnerForm(instance=user) if request.user.owner else forms.UserForm(instance=user)
        else:
            msg = 'Nenhum Usuário encontrado!'
            icon = 'alert-warning'

    if request.method == 'POST':
        if user:
            form = forms.UserOwnerForm(request.POST, instance=user) if request.user.owner else forms.UserForm(request.POST, instance=user)
        else:
            form = forms.UserOwnerForm(request.POST) if request.user.owner else forms.UserForm(request.POST)
        try:
            if form.is_valid():
                form = form.save(commit=False)
                email = form.email
                senha = form.telefone
                form.set_password(senha)
                form.username = email
                if user:
                    msg = 'Usuário editado com sucesso!'
                    icon = 'alert-success'
                else:
                    msg = 'Usuário criado com sucesso!'
                    icon = 'alert-success'
                form.save()
        except Exception as e:
            msg = e
            icon = "alert-danger"
    if user:
        form = forms.UserOwnerForm(instance=user) if request.user.owner else forms.UserForm(instance=user)
    else:
        form = forms.UserOwnerForm() if request.user.owner else forms.UserForm()


    notification = {'icon': icon, 'msg': msg}

    context = {
        'page_title': page_title, 'form': form, 'msg': msg, 'notification': notification
    }

    return render(request, 'create_update_user.html', context)


def my_profile(request):
    page_title = "MINHAS INFORMAÇÕES"
    old_email = None
    msg = None
    icon = None
    msg = None
    my_profile = models.User.objects.get(pk=request.user.pk)

    if my_profile:
        form = forms.MyProfileUserForm(instance=my_profile)
        old_email = my_profile.email

    if request.method == 'POST':
        form = forms.MyProfileUserForm(request.POST, instance=my_profile)

        if form.is_valid():
            form = form.save(commit=False)
            form.email = old_email
            form.save()
            my_profile.refresh_from_db()

            form = forms.MyProfileUserForm(instance=my_profile)
            msg = "Informação Alterada com sucesso!"
            icon = "alert-success"

        else:
            print(form.errors)
            msg = "Informação inválida! Revise o formulário e tente novamente."
            icon = "alert-warning"
    
    notification = {'msg': msg, 'icon': icon}

    context = {
        'page_title': page_title, 'form': form, 'msg': msg, 'notification': notification
    }

    return render(request, 'create_update_user.html', context)

def list_user(request):
    page_title = 'LISTA DE USUÁRIOS'

    if request.user.is_superuser:
        users = models.User.objects.filter(is_active=True)
    else:
        users = models.User.objects.filter(is_active=True, company=request.user.company)

    context = {
        'page_title': page_title, 'users': users
    }

    return render(request, 'list_user.html', context)


@csrf_exempt
def delete_user(request):
    response = {
        'success': False
    }

    pk = request.POST.get('pk', None)

    if pk:
        user = models.User.objects.get(pk=pk)
        if user:
            user.is_active = False
            user.save()
            response['success'] = True

    return JsonResponse(response, safe=False)




    