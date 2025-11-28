# Imagem base
FROM python:3.11-slim

# Instalar dependências de sistema (necessário para cryptography, bcrypt, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar o requirements.txt do backend
COPY f5diarios-backend/requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código inteiro do backend
COPY f5diarios-backend/ .

# Expor porta da API
EXPOSE 8000

# Comando para arrancar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
