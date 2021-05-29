from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


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