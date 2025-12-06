Desafio Técnico - Estagiário Python/Django 2026.1

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
