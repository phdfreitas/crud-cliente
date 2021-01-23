from django.contrib import admin
from . models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'data_nascimento', 'data_cadastro')
    list_filter = ('endereco', 'data_nascimento')
    date_hierarchy = 'data_cadastro'
    search_fields = ('nome', 'endereco', 'data_nascimento')