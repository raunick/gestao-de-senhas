from django.contrib import admin
from .models import CategoriaComputador, Localizacao, Computador, Fila, Chamada

@admin.register(CategoriaComputador)
class CategoriaComputadorAdmin(admin.ModelAdmin):
    list_display = ('nome', )

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'descricao')

@admin.register(Computador)
class ComputadorAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'nome', 'categoria', 'localizacao', 'data_criacao', 'data_atualizacao')

@admin.register(Fila)
class FilaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'data_criacao', 'data_atualizacao')

@admin.register(Chamada)
class ChamadaAdmin(admin.ModelAdmin):
    list_display = ('computador', 'fila', 'senha', 'horario_entrada', 'horario_saida', 'status')
