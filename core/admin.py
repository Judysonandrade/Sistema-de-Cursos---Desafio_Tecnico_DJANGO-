from django.contrib import admin
from .models import Aluno, Curso, matricula



@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'data_de_ingresso')
    search_fields = ('nome', 'email', 'cpf')
    ordering = ('nome',)
    list_filter = ('data_de_ingresso',)
    list_per_page = 20
    


@admin.register(Curso)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_curso', 'carga_horaria', 'valor_da_inscricao', 'status')
    search_fields = ('nome_do_curso',)
    ordering = ('nome_do_curso',)
    list_filter = ('status',)
    list_per_page = 20

@admin.register(matricula)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_da_matricula', 'status_do_pagamento')
    search_fields = ('aluno__nome', 'curso__nome_do_curso')
    ordering = ('-data_da_matricula',)
    list_filter = ('status_do_pagamento', 'data_da_matricula')
    list_per_page = 20






# Register your models here.
