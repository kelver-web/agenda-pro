from django.contrib import admin
from agenda.models import Tarefas

# Register your models here.


class TarefasAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nome', 'descricao', 'data_de_criacao', 'data_de_execucuao', 'status']
    list_editable = ['status']
    list_filter = ['usuario', 'data_de_criacao']


admin.site.register(Tarefas, TarefasAdmin)
