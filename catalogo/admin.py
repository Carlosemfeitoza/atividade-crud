from django.contrib import admin
from .models import Quadrinho

@admin.register(Quadrinho)
class HQAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'numero', 'editora', 'autor', 'data_lancamento', 'descricao')
    search_fields = ('titulo', 'autor')
