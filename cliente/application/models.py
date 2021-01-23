from django.db import models
from django.utils import timezone
from django.urls import reverse


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(default=timezone.now)

    def get_absolute_url_update(self):
        return reverse('atualizarCliente', args=[self.pk])

    def get_absolute_url_delete(self):
        return reverse('excluirCliente', args=[self.pk])

    class Meta:
        ordering = ('data_cadastro',)

    def __str__(self):
        return self.nome
