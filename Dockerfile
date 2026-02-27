# 1. Imagen base de Python
FROM python:3.11-slim

# 2. Instalamos dependencias del sistema para PostgreSQL y compilación
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. Directorio de trabajo
WORKDIR /app

# 4. Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente
COPY . .

# 6. Exponer el puerto de Flask
EXPOSE 5000

# 7. Comando para arrancar (usaremos app.py por defecto)
CMD ["python", "app.py"]