# Usamos la imagen base de Python
FROM python:3.12

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el archivo requirements.txt al directorio de trabajo del contenedor
COPY ../../requirements.txt /app/requirements.txt

# Instalamos las dependencias desde requirements.txt, incluyendo Kaggle
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && pip install kaggle
# Instalamos las dependencias para flask
RUN pip install --index-url=https://pypi.org/simple flask loguru


# Copiamos los scripts necesarios al directorio de trabajo del contenedor
COPY scripts/download_data.py /app/scripts/
COPY scripts/predict.py /app/scripts/
COPY scripts/train.py /app/scripts/

# Configuramos la ruta del archivo kaggle.json
COPY kaggle.json /root/.kaggle/kaggle.json

# Creamos el directorio data si no existe
RUN mkdir -p /app/data

# Añadimos mensajes de depuración
RUN echo "Contenido del directorio /app antes de descargar datos:" && ls -R /app

# Ejecutamos el script download_data.py para descargar los datos
RUN python /app/scripts/download_data.py

# Añadimos mensajes de depuración
RUN echo "Contenido del directorio /app después de descargar datos:" && ls -R /app

# Copiamos los modelos necesarios al directorio de trabajo del contenedor
COPY models/ /app/models/   
# Copiamos el archivo de apirest al directorio de trabajo del contenedor
COPY scripts/apirest.py /app         

# Actualizamos el sistema y instalamos unzip (si es necesario)
RUN apt-get update && apt-get install -y unzip

# Exponemos el puerto 5001
EXPOSE 5001

CMD ["python", "apirest.py"]
