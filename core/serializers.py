from rest_framework import serializers
from django.db.models import Sum
from .models import Aluno, Curso, matricula


class AlunoSerializer(serializers.ModelSerializer):
    
    total_pago = serializers.SerializerMethodField()
    total_devido = serializers.SerializerMethodField()


    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'cpf', 'data_de_ingresso', 'total_pago', 'total_devido']
    
    def validar_cpf(self, cpf):
        if not cpf.isdigit() or len(cpf) != 11:
            raise serializers.ValidationError("CPF inválido.")
    
        return cpf

    def get_total_pago(self, obj):
        total = obj.matriculas.filter(status_do_pagamento='PAGO').aggregate(
            total_pago=Sum('curso__valor_da_inscricao')
        )['total_pago'] or 0.00
        return total
    
    def get_total_devido(self, obj):
        total = obj.matriculas.filter(status_do_pagamento='PENDENTE').aggregate(
            total_devido=Sum('curso__valor_da_inscricao')
        )['total_devido'] or 0.00
        return total

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome_do_curso', 'carga_horaria', 'valor_da_inscricao', 'status']


class MatriculaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome') 
    curso_nome = serializers.ReadOnlyField(source='curso.nome_do_curso')

    class Meta:
        model = matricula
        fields = ['id', 'aluno', 'aluno_nome', 'curso', 'curso_nome', 'data_da_matricula', 'status_do_pagamento']

    def validate(self, data):
        aluno = data.get('aluno')
        curso = data.get('curso')
        if matricula.objects.filter(aluno=aluno, curso=curso).exists():
            raise serializers.ValidationError("O aluno já está matriculado neste curso.")
        return data

