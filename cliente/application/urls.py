from django.urls import path
from . import views


urlpatterns = [
    path('', views.ClienteListView.as_view(), name='listarClientes'),
    path('cadastrarCliente', views.ClienteCreateView.as_view(), name='cadastrarCliente'),
    path('atualizar/<int:pk>', views.ClienteUpdateView.as_view(), name='atualizarCliente'),
    path('excluir/<int:pk>', views.ClienteDeleteView.as_view(), name='excluirCliente'),
]