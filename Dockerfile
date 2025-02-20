FROM python:3.13-slim

WORKDIR /app

# Copiar los archivos de requerimientos primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando por defecto para ejecutar los tests
CMD ["pytest", "-v"] 