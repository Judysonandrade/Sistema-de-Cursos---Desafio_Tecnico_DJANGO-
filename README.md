Desafio Técnico – Estagiário Python/Django 2026.1

Este projeto utiliza Docker e Docker Compose para configurar automaticamente o ambiente, incluindo a aplicação Django e o banco de dados PostgreSQL. Não é necessário instalar Python ou PostgreSQL localmente.

PRÉ-REQUISITOS

É necessário ter instalado:

Docker

Docker Compose

COMO EXECUTAR O PROJETO

Clone o repositório:

git clone <URL_DO_SEU_REPOSITORIO>
cd Desafio_Tecnico

Inicie os containers:

docker-compose up --build

Aguarde até que apareça no terminal:
Starting development server at http://0.0.0.0:8000/

As migrações do banco são executadas automaticamente.

ACESSO À APLICAÇÃO

Dashboard (Frontend): http://localhost:8000/

Lista de Alunos: http://localhost:8000/alunos/

API Root: http://localhost:8000/api/

Documentação Swagger: http://localhost:8000/swagger/

Painel Administrativo: http://localhost:8000/admin/

CRIAR UM USUÁRIO ADMINISTRADOR

Com os containers rodando, execute:

docker-compose exec web python manage.py createsuperuser

Siga as instruções para definir usuário e senha.
