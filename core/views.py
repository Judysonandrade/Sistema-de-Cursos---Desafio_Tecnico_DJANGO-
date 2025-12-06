from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import connection

from .models import Aluno, Curso, matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'email', 'cpf']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome_do_curso', 'status']

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['aluno__nome', 'curso__nome_do_curso', 'status_do_pagamento']

    @action(detail=False, methods=['post'])
    def pagamento_curso(self, request, pk=None):
        matricula_id = request.data.get('matricula_id')
        try:
            matricula_instance = matricula.objects.get(id=matricula_id)
            matricula_instance.status_do_pagamento = 'PAGO'
            matricula_instance.save()
            return Response({'status': 'Pagamento realizado com sucesso.'})
        except matricula.DoesNotExist:
            return Response({'status': 'Matrícula não encontrada.'}, status=404)

class RelatorioSQL(APIView):
    def get(self, request):
        query = """
        SELECT C.nome_do_curso, COUNT(M.id) as qtd, SUM(C.valor_da_inscricao) as total_gerado
        FROM core_curso C
        JOIN core_matricula M ON C.id = M.curso_id
        WHERE M.status_do_pagamento = 'PAGO'
        GROUP BY C.nome_do_curso
        ORDER BY total_gerado DESC;
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            resultados = cursor.fetchall()
        
        data = [
            {
                'nome_do_curso': row[0],
                'qtd_matriculas': row[1],
                'total_gerado': row[2],
            }
            for row in resultados
        ]
    
        return Response(data)

def dashboard_view(request):
    total_pago = matricula.objects.filter(status_do_pagamento='PAGO').count()
    total_pendente = matricula.objects.filter(status_do_pagamento='PENDENTE').count()
    
    context = {
        'total_alunos': Aluno.objects.count(),
        'cursos_ativos': Curso.objects.filter(status='ATIVO').count(),
        'cursos_inativos': Curso.objects.filter(status='INATIVO').count(),
        'total_matriculas': matricula.objects.count(),
        'graficos_pago': total_pago,
        'graficos_pendente': total_pendente,
    }
    # CORREÇÃO AQUI: Adicionei 'core/' antes do nome do arquivo
    return render(request, 'core/dashboard.html', context)

def lista_alunos_view(request):
    alunos = Aluno.objects.prefetch_related('matriculas__curso').all()
    # CORREÇÃO AQUI TAMBÉM: Supondo que você moveu os dois arquivos para a pasta 'core'
    return render(request, 'core/lista_alunos.html', {'alunos': alunos})