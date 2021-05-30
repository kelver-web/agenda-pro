from django import forms
from agenda.models import Tarefas


class FormTarefa(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['nome', 'descricao', 'status']
