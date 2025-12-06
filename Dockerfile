# Usa uma imagem leve do Python
FROM python:3.11-slim

# Evita arquivos .pyc e logs presos no buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema para o Postgres
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]