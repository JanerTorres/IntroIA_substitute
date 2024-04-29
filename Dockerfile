# Usa la imagen base de Python
FROM python:3.8-slim

# Instala las dependencias desde requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia los archivos necesarios al directorio de trabajo del contenedor
COPY scripts/ /app/scripts/
COPY kaggle.json /root/.kaggle/

# Copiar el directorio donde se guardan los modelos
COPY models/ /app/models/

# Copiamos los archivos de data
COPY data/test.csv /app/data/test.csv

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y unzip

# CMD para ejecutar el script predict.py
CMD ["python", "./scripts/predict.py"]
