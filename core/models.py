from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_de_ingresso = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    

    
    def __str__(self):
        return self.nome


class Curso(models.Model):
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]    
    nome_do_curso = models.CharField(max_length=255)
    carga_horaria = models.IntegerField(help_text="Carga horária em horas")
    valor_da_inscricao = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVO')

    class Meta:
        ordering = ['nome_do_curso']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


    def __str__(self):
        return self.nome_do_curso
    

class matricula(models.Model):
    STATUS_CHOICES = [
        ('PAGO', 'Pago'),
        ('PENDENTE', 'Pendente'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_da_matricula = models.DateTimeField(auto_now_add=True)
    status_do_pagamento = models.CharField(max_length=8, choices=STATUS_CHOICES, default='PENDENTE')

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas' 
        ordering = ['-data_da_matricula']
        unique_together = ('aluno', 'curso')

    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome_do_curso}"


