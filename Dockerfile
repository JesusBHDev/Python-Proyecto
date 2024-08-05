# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y de la aplicación
COPY requirements.txt ./
COPY app.py ./

# Instala los requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que tu aplicación usará
EXPOSE 8000

# Comando para ejecutar tu aplicación
CMD ["python", "app.py"]
