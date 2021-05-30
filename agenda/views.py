from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.


@login_required(login_url='/login/')
def home(request):

    return render(request, 'agenda/home.html')


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
            messages.error(request, 'Usuário ou senha inválido!')
    
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
            messages.error(request, 'Erro! Já existe um usuário com o mesmo e-mail.')
            return render(request, 'agenda/register.html')
    except User.DoesNotExist:
        try:
            usuario_aux = User.objects.get(username=request.POST['username'])
            if usuario_aux:
                messages.error(request, 'Erro! Já existe um usuário com o mesmo nome.')
                return render(request, 'agenda/register.html')

        except User.DoesNotExist:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            novo_usuraio = User.objects.create_user(username=username, email=email, password=password)
            novo_usuraio.save()
            return render(request, 'agenda/success.html')