from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import Cliente

from django.contrib.auth.mixins import LoginRequiredMixin


class ClienteCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')

    model = Cliente
    fields = ['nome', 'endereco', 'telefone', 'data_nascimento']
    template_name = 'cliente/cadastrarClientes.html'
    success_url = reverse_lazy('listarClientes')


class ClienteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Cliente
    template_name = 'cliente/listarClientes.html'


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')

    model = Cliente
    fields = ['nome', 'endereco', 'telefone', 'data_nascimento']
    template_name = 'cliente/atualizarCliente.html'
    success_url = reverse_lazy('listarClientes')


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')

    model = Cliente
    template_name = 'cliente/excluirCliente.html'
    success_url = reverse_lazy('listarClientes')