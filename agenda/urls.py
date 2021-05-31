from django.urls import path
from agenda import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('register/', views.register),
    path('register/submit', views.register_submit),
    path('home/', views.home),
    path('lista/', views.lista),
    path('tarefa/<int:id>/', views.tarefa),
    path('adicionar/', views.adicionar),
    path('adicionar/submit', views.adicionar_submit),
    path('deletar/<int:id>/', views.deletar),
]
