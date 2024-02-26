# Dockerfile
FROM python:3.9-slim

# Trabalhe no diretório /app no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos para o contêiner
COPY . /app

# Comando para rodar o servidor Flask quando o contêiner iniciar
CMD ["flask", "run", "--host=0.0.0.0"]
