from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tarefas(models.Model):
    data_de_criacao = models.DateTimeField(auto_now_add=True, verbose_name='data de criação')
    data_de_execucuao = models.DateTimeField(blank=True, null=True, verbose_name='data de execução')
    nome = models.CharField(max_length=200, verbose_name='nome')
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='finalizado')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_de_criacao']
        verbose_name_plural = 'Tarefa'

    def __str__(self):
        return self.nome