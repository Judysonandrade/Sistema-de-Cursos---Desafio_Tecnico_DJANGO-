Desafio Técnico - Estagiário Python/Django 2026.1

Sistema de gestão acadêmica desenvolvido para o processo seletivo de estágio. A aplicação gerencia alunos, cursos e matrículas, oferecendo uma API REST completa, relatórios visuais e controle financeiro, totalmente containerizada com Docker.

Funcionalidades

Cadastro de Alunos: Gerenciamento de dados pessoais (Nome, E-mail, CPF) e data de ingresso.

Cadastro de Cursos: Controle de cursos com carga horária, valor de inscrição e status (ativo/inativo).

Matrículas: Vínculo entre alunos e cursos com controle de status de pagamento (Pago/Pendente).

Dashboard e Relatórios: Interface HTML para visualização de métricas gerais e histórico detalhado de alunos.

API REST: Endpoints para todas as entidades, documentados via Swagger.

Consultas SQL: Implementação de consultas puras (Raw SQL) para relatórios analíticos.

Tecnologias Utilizadas

Python 3.11

Django 5.2

Django Rest Framework

PostgreSQL 15

Docker & Docker Compose

HTML/CSS (Templates Django)

Pré-requisitos

Para executar este projeto, é necessário ter instalado:

Docker

Docker Compose

Não é necessário instalar Python ou PostgreSQL localmente, pois o ambiente é configurado automaticamente via containers.

Como Executar o Projeto

Siga os passos abaixo para iniciar a aplicação:

Clone o repositório:

git clone <URL_DO_SEU_REPOSITORIO>
cd Desafio_Tecnico

Inicie os containers:
Execute o comando abaixo na raiz do projeto para construir e iniciar os serviços:

docker-compose up --build

Aguarde até que o terminal exiba a mensagem indicando que o servidor iniciou (ex: "Starting development server at http://0.0.0.0:8000/"). O processo de migração do banco de dados é executado automaticamente na inicialização.

Acesse a Aplicação:

Dashboard (Frontend): http://localhost:8000/

Lista de Alunos (Frontend): http://localhost:8000/alunos/

API Root: http://localhost:8000/api/

Documentação Swagger: http://localhost:8000/swagger/

Painel Administrativo: http://localhost:8000/admin/

Criando um Usuário Administrador

Para acessar o painel administrativo (/admin), crie um superusuário executando o seguinte comando em um novo terminal (com os containers rodando):

docker-compose exec web python manage.py createsuperuser

Siga as instruções no terminal para definir nome de usuário e senha.

Estrutura do Repositório

core/: Aplicação principal contendo modelos, views, serializers e testes.

config/: Configurações globais do projeto Django.

templates/: Arquivos HTML para as interfaces de usuário.

Dockerfile: Definição da imagem Docker da aplicação.

docker-compose.yml: Orquestração dos serviços web e banco de dados.

meu_database.sql: Script SQL contendo a estrutura das tabelas e a consulta de análise solicitada no desafio.
