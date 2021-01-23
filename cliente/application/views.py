from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'endereco', 'telefone', 'data_nascimento']
    template_name = 'cliente/cadastrarClientes.html'
    success_url = reverse_lazy('listarClientes')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/listarClientes.html'


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'endereco', 'telefone', 'data_nascimento']
    template_name = 'cliente/atualizarCliente.html'
    success_url = reverse_lazy('listarClientes')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/excluirCliente.html'
    success_url = reverse_lazy('listarClientes')