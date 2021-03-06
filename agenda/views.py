from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http.response import Http404
from agenda.models import Tarefas
from agenda.forms import FormTarefa

# Create your views here.


@login_required(login_url='/login/')
def home(request):
    usuario = request.user
    items = Tarefas.objects.filter(usuario=usuario).count()
    context = {'items': items}
    return render(request, 'agenda/home.html', context=context)

@login_required(login_url='/login/')
def lista(request):
    usuario = request.user
    items = Tarefas.objects.filter(usuario=usuario)
    context = {'items': items}
    return render(request, 'agenda/lista-tarefas.html', context=context)

@login_required(login_url='/login/')
def tarefa(request, id):
    items = Tarefas.objects.filter(id=id)
    context = {'items': items}
    return render(request, 'agenda/tarefas.html', context=context)


@login_required(login_url='/login/')
def adicionar(request):
    id = request.GET.get('id')
    dados = {}
    if id:
        dados['evento'] = Tarefas.objects.get(id=id)
    return render(request, 'agenda/cria-tarefa.html', dados)

@login_required(login_url='/login/')
def adicionar_submit(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_de_criacao = request.POST.get('data_de_criacao')
        descricao = request.POST.get('descricao')
        usuario = request.user
        # update agenda
        id = request.POST.get('id')
        if id:
            evento = Tarefas.objects.get(id=id)
            if evento.usuario == usuario:
                evento.nome = nome
                evento.descricao = descricao
                evento.data_de_criacao = data_de_criacao
                evento.save()
        else:
            Tarefas.objects.create(nome=nome,
                                  data_de_criacao=data_de_criacao,
                                  descricao=descricao,
                                  usuario=usuario)
    return render(request, 'agenda/cria-tarefa.html')


@login_required(login_url='/login/')
def deletar(request, id):
    usuario = request.user
    try:
        items = Tarefas.objects.get(id=id)
    except Exception:
        raise Http404()

    if usuario == items.usuario:
        items.delete()
    else:
        raise Http404()
    return redirect('/lista')

def login_user(request):
    return render(request, 'agenda/login.html')

def submit_login(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/home')
        
        else:
            messages.error(request, 'Usu??rio ou senha inv??lido!')
    
    return redirect('/home')

def logout_user(request):
    logout(request)
    return redirect('/login')

def register(request):
    return render(request, 'agenda/register.html')

@require_POST
def register_submit(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
        if usuario_aux:
            messages.error(request, 'Erro! J?? existe um usu??rio com o mesmo e-mail.')
            return render(request, 'agenda/register.html')
    except User.DoesNotExist:
        try:
            usuario_aux = User.objects.get(username=request.POST['username'])
            if usuario_aux:
                messages.error(request, 'Erro! J?? existe um usu??rio com o mesmo nome.')
                return render(request, 'agenda/register.html')

        except User.DoesNotExist:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            novo_usuraio = User.objects.create_user(username=username, email=email, password=password)
            novo_usuraio.save()
            return render(request, 'agenda/success.html')